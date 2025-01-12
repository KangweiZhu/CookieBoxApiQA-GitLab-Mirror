# -*- encoding: utf-8 -*-
"""
    @File    :   mysql.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    1/6/25 05:00    Anicaa (Kangwei Zhu)  1.0      
"""
import queue
import threading
from typing import Literal

import mysql.connector

from config import config
from context.context import context
from modal.enum.sql_enum import SQLEnum
from modal.test_case import ApiTestCase
from mysql.connector.pooling import MySQLConnectionAbstract

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
            connection.cursor().close()
            connection.close()
        except mysql.connector.Error as err:
            pass

    @staticmethod
    def execute(connection, sql: str):
        try:
            connection.cursor().execute(sql)
            connection.commit()
        except mysql.connector.Error as err:
            print("执行sql出现错误")

    @staticmethod
    def execute_many(connection: MySQLConnectionAbstract, sql, data):
        try:
            cursor = connection.cursor()
            cursor.executemany(sql, data)
            connection.commit()
        except mysql.connector.Error as err:
            pass

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
        cursor = connection.cursor()
        result = None
        if not num or num > 1:
            result = cursor.fetchall()
        elif num == 1:
            result = cursor.fetchone()
        else:
            pass #raise excpetion
        return result

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
    def execute_setup_teardown_sql(connection, apitestcase: ApiTestCase, timing: Literal['setup', 'teardown']):
        timing_sqls = apitestcase.sql.get(timing)
        for task_type, sql_containers in timing_sqls:
            if task_type is None or sql_containers is None:
                return
            if task_type == 'persist':
                if isinstance(sql_containers, dict):
                    for context_key, sql_expr in sql_containers.items():
                        data, sql = StringUtil.sanitize_sql(sql_expr)
                        MysqlUtil.execute_many(connection, sql, data)
                        execute_result = None
                        if MysqlUtil.get_sql_typing(sql) == SQLEnum.SQL_TYPE_SELECT:
                            execute_result = MysqlUtil.get_select_result(connection)

                        context['sql']['persist'][timing] = execute_result
                else:
                    pass
            elif task_type == 'execute':
                if isinstance(sql_containers, list):
                    for sql_expr in sql_containers:
                        data, sql = StringUtil.sanitize_sql(sql_expr)
                        MysqlUtil.execute_many(connection, sql, data)
                else:
                    pass
            else:
                pass

# class MysqlConnectionPool:
#
#     def __init__(self):
#         self.pool = queue.Queue(maxsize=50)
#         self.lock = threading.Lock()

class MysqlConnection:

    def __init__(self):
        self.connection = MysqlUtil.init_connection()