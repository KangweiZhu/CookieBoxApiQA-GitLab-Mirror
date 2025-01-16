# -*- encoding: utf-8 -*-
"""
    @File    :   mysql_util.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    1/6/25 05:00    Anicaa (Kangwei Zhu)  1.0      
"""
from typing import Literal, Union

import mysql.connector

from config import config
from context.context import application_context
from modal.enum.sql_enum import SQLEnum
from modal.test_case import ApiTestCase

from utils.misc.string_util import StringUtil


class MysqlUtil:

    @staticmethod
    def init_connection():
        try:
            connection = mysql.connector.connect(
                host=config['mysql']['host'],
                port=config['mysql']['port'],
                user=config['mysql']['username'],
                password=config['mysql']['password'],
                database=config['mysql']['database']
            )
            return connection
        except mysql.connector.Error as err:
            print("连接MySQL数据库出现错误")

    @staticmethod
    def __del__(connection):
        try:
            MysqlUtil.create_dict_cursor(connection).close()
            connection.close()
        except mysql.connector.Error as err:
            pass

    @staticmethod
    def get_sql_typing(sql: str):
        sql = sql.strip().lower()
        sql_type = None
        if sql.startswith(SQLEnum.SQL_TYPE_SELECT.value):
            sql_type = SQLEnum.SQL_TYPE_SELECT
        elif sql.startswith(SQLEnum.SQL_TYPE_INSERT.value):
            sql_type = SQLEnum.SQL_TYPE_INSERT
        elif sql.startswith(SQLEnum.SQL_TYPE_UPDATE.value):
            sql_type = SQLEnum.SQL_TYPE_UPDATE
        elif sql.startswith(SQLEnum.SQL_TYPE_DELETE.value):
            sql_type = SQLEnum.SQL_TYPE_DELETE
        else:
            pass
        return sql_type

    @staticmethod
    def default_execute(connection, sql: str):
        try:
            MysqlUtil.create_dict_cursor(connection).execute(sql)
            connection.commit()
        except mysql.connector.Error as err:
            print("执行sql出现错误")

    @staticmethod
    def execute_by_method(connection, sql, data) -> Union[list[int], dict[str, list[any]]]:
        """
        根据 SQL 的 SELECT， UPDATE， DELETE， INSERT来执行。

        :param connection: 连接
        :param sql: sql表达式
        :param data: list形式的数据
        :return: 要么是list， 里面放的是比如插入后的自增id。要么是dict，key是字段名， value是多行（单行）的值，list类型。
        """
        sql_type = MysqlUtil.get_sql_typing(sql)
        result = None
        if sql_type == SQLEnum.SQL_TYPE_SELECT:
            MysqlUtil.execute_select(connection, sql, data)
        elif sql_type == SQLEnum.SQL_TYPE_INSERT:
            result = MysqlUtil.execute_insert(connection, sql, data)
        elif sql_type == SQLEnum.SQL_TYPE_UPDATE:
            MysqlUtil.execute_update(connection, sql, data)
        elif sql_type == SQLEnum.SQL_TYPE_DELETE:
            MysqlUtil.execute_delete(connection, sql, data)
        else:
            pass
        return result

    @staticmethod
    def default_execute_many(connection, sql, data):
        """
        用ids存放所有执行的用例的id。

        :param connection:
        :param sql:
        :param data:
        :return:
        """
        try:
            cursor = MysqlUtil.create_dict_cursor(connection)
            cursor.executemany(sql, data)
            connection.commit()
        except mysql.connector.Error as err:
            pass

    @staticmethod
    def execute_select(connection, sql, data):
        pass

    @staticmethod
    def execute_insert(connection, sql, datas) -> list[int]:
        """
        把数据拆开来，按行来解析。然后每行都execute一下，并且获取到lastrowid，将其加入存放lastrowid的容器。
        等所有的数据都执行完后，根据每个lastrowid，select，然后挨个fetchone, 把结果加入到容器中。容器为dict，字段名-list格式的每行数据

        :param connection:
        :param sql:
        :param datas:
        :return: 插入的新进去的id
        """
        lastrowids = list()
        cursor = MysqlUtil.create_dict_cursor(connection)
        for data in datas:
            print('executing: ', sql, data)
            cursor.execute(sql, data)
            lastrowid = cursor.lastrowid
            lastrowids.append(lastrowid)
        connection.commit()
        return lastrowids

    @staticmethod
    def execute_update(connection, sql, data):
        pass

    @staticmethod
    def execute_delete(connection, sql, data):
        pass

    @staticmethod
    def create_dict_cursor(connection):
        return connection.cursor(dictionary=True)

    #todo
    @staticmethod
    def get_delete_result(connection):
        pass

    #todo
    @staticmethod
    def get_insert_result(connection):
        pass

    #todo
    @staticmethod
    def get_update_result(connection):
        pass

    @staticmethod
    def get_select_result(connection, num=None):
        cursor = MysqlUtil.create_dict_cursor(connection)
        result = None
        if not num or num > 1:
            result = cursor.fetchall()
        elif num == 1:
            result = cursor.fetchone()
        else:
            pass #raise exception
        return result

    @staticmethod
    def execute_setup_teardown_sql(connection, apitestcase: ApiTestCase, timing: Literal['setup', 'teardown']):
        # 看是否有sql field
        if not apitestcase.sql:
            return
        # 尝试获取timing(setup, teardown)
        timing_sqls = apitestcase.sql.get(timing)
        if not timing_sqls:
            return
        # task_type(persist, normal)对应的sql_containers. persist是context值对应sql. normal则是一个list
        for task_type, sql_containers in timing_sqls.items():
            # 如果是persist，就需要获取到
            if task_type == 'persist':
                if isinstance(sql_containers, dict):
                    for context_key, sql_expr in sql_containers.items():
                        if not sql_expr:
                            return
                        datas, sql = StringUtil.sanitize_sql(sql_expr, apitestcase.identifier)
                        execute_result = MysqlUtil.execute_by_method(connection, sql, datas)
                        application_context['sql'][timing]['persist'][context_key] = execute_result
                else:
                    pass
            elif task_type == 'execute':
                if isinstance(sql_containers, list):
                    for sql_expr in sql_containers:
                        datas, sql = StringUtil.sanitize_sql(sql_expr, apitestcase.identifier)
                        MysqlUtil.default_execute_many(connection, sql, datas)
                else:
                    pass
            else:
                pass

class MysqlConnection:

    def __init__(self):
        self.connection = MysqlUtil.init_connection()