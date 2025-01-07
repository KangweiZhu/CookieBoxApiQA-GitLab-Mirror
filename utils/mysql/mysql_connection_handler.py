# -*- encoding: utf-8 -*-
"""
    @File    :   mysql_connection_handler.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    1/6/25 05:00    Anicaa (Kangwei Zhu)  1.0      
"""
import queue
import threading

import mysql.connector

from config import config

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
    def fetch_one(connection, sql):
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
        except mysql.connector.Error as err:
            pass

    @staticmethod
    def fetch_all(connection, sql):
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            pass

# class MysqlConnectionPool:
#
#     def __init__(self):
#         self.pool = queue.Queue(maxsize=50)
#         self.lock = threading.Lock()

class MysqlConnection:

    def __init__(self):
        self.connection = MysqlUtil.init_connection()



