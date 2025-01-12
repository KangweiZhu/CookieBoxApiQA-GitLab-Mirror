import requests

from typing import Optional, Dict, Any, Union

from modal.enum.sql_enum import SQLEnum
from modal.test_case import ApiTestCase
from context.context import context
from utils.misc.json_util import JsonUtil
from utils.misc.string_util import StringUtil
from utils.mysql.mysql import MysqlUtil, MysqlConnection


def url_formatter(**kwargs) -> str:
    return "{protocol}://{host}{api}".format(**kwargs)


class BaseRequest:

    def __init__(self, apitestcase: ApiTestCase):
        self.apitestcase = apitestcase

    @staticmethod
    def sanitize_data_fields(json_obj: dict, field: Union[str, Dict[str, str], None], error_identifier) -> \
    Union[str, Dict, None]:
        if not field or not json_obj:
            return field

        if isinstance(field, Dict):
            for key, s in field.items():
                value = StringUtil.replace_jsonpath_in_string(json_obj, s, error_identifier)
                field[key] = value
        elif isinstance(field, str):
            field = StringUtil.replace_jsonpath_in_string(json_obj, field, error_identifier)

        return field

    def setup_request(self):
        MysqlUtil.execute_setup_teardown_sql(MysqlConnection, )

    def teardown_request(self, resp: requests.Response) -> None:
        """
            request 结束后需要做的事

                1. 将整个resp转换成json，将testcase_id 和 这个json存放到上下文容器中。方便后面别的测试用例，依赖此测试用例的结果时，直接用这个测试用例的id取到json，并配合
                jsonpath拿到数据

                2. 自定义一些context，context可以有范围，比如global-全局，module-模块。这样，context['response']['global']['token'] = xxx; context['response']['module']['token'] = yyy,
                更加灵活一点。这里因为是request，所以context类型只有response。未来也可以自定义context类型，给定作用域以及名称，更灵活地控制上下文存的值。


        :param resp:
        :return:
        """
        apitestcase = self.apitestcase
        if not resp or not resp.text:
            return

        json_resp = resp.json()
        context[apitestcase.identifier] = json_resp

        """
            如果测试用例的上下文字段不为空，就按照指定的名字，存入上下文
        """
        if apitestcase.context:
            for context_type, context_scopes in apitestcase.context.items():
                context.setdefault(context_type, {})
                for scope, attributes in context_scopes.items():
                    context[context_type].setdefault(scope, {})
                    for name, json_expr in attributes.items():
                        extracted_value = JsonUtil.parse_jsonpath(json_resp, json_expr,
                                                                  f'{apitestcase.identifier}-{scope}-{name}')
                        context[context_type][scope][name] = extracted_value

        """
            Setup SQL 与 Teardown SQL
            
            各自默认都有两种：
                - persist: 保存sql执行的结果到context
                    persist这个key对应一个dict，dict的key是存放在context中的key。dict的value则是sql，sql执行后，会把结果和key进行映射，放在context里。
                    
                    目前只支持insert和select。 update, delete应该也和insert一样处理吧，但是我还没试过，python实在不熟（java其实也不熟。。）。不过持久化并用到delete结果的场景我还暂时想不出来
                    
                    还有一个要做的？解析的时候不仅仅要解析jsonpath，还要解析sql？有必要这样子做吗？要不直接放setup sql，然后持久化。要用的时候直接从context里面取？
                    
                    presist:
                        test_login_01_sql_01: 
                            - insert into post (xxx,xxx) values (xxx, xxx)
                            - [('Title 1', 'Content 1'), ('Title 2', 'Content 2')]
                
                    
                - execute: 仅执行
                    execute这个key对应的是一个list，就是一系列的需要被执行的sql，但是并不关心执行结果
                    
                我们允许SQL中，包含jsonpath。 比如 select id from post where content = {$.test_comment_01.data.content}
                
                一些小tips:
                    >>> LAST_ROW_ID(): cursor.lastrowid => 获取插入后，auto increment生成的id，可以保存这个id，或者可以通过这个id，查询到新插入的行的记录
                    
                    >>> INSERT INTO post (title, content) VALUES ('Test Title', 'Test Content')
                        RETURNING *; --同样能够获取到执行一条插入后的结果
                        
                    >>> execute()和executeall()返回的都是受影响的行数。使用executemany()进行插入时，我们可以通过 
                        select * from table where id >= lastrowid - affectedid + 1 && id <= lastrowid
                        配合上fetchall(), for row in cursor.fetchall(). 来存储fetch到的结果。
                         
        """
        if apitestcase.sql:
            teardown_sqls = apitestcase.sql.get("teardown")
            if teardown_sqls:
                MysqlUtil.execute_setup_teardown_sql(MysqlConnection(), apitestcase, SQLEnum.SQL_EXECUTION_TIMING_TEARDOWN.value)




