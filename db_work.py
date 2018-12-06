#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import psycopg2
import settings


class Postgres(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            # Конфиг подключения к базе -> вынести в отдельный файл

            db_config = {
                'dbname': settings.NAME,
                'user': settings.USER,
                'host': settings.HOST,
                'password': settings.PWD}
            try:
                print('connecting to PostgreSQL database...')
                connection = Postgres._instance.connection = psycopg2.connect(**db_config)
                cursor = Postgres._instance.cursor = connection.cursor()
                cursor.execute('SELECT VERSION()')
                db_version = cursor.fetchone()

            except Exception as error:
                print('Error: connection not established {}'.format(error))
                Postgres._instance = None

            else:
                print('connection established\n{}'.format(db_version[0]))

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def update(self, i_id, i_sys):
        try:
            i_sys = i_sys.lower()
            result = self.cursor.execute(
                "INSERT INTO sys_sel(id,system) VALUES(%(id)s, %(sys)s) ON CONFLICT (id) DO UPDATE SET system = %(sys)s",
                {'id': i_id, 'sys': i_sys})
            self.connection.commit()
            if result is None:
                res = 'Система ' + i_sys + ' выбрана'
            else:
                res = result
        except Exception as error:
            print('error: {}'.format(error))
            return 'error: {}'.format(error)
        else:
            return str(res)

    def read(self, i_id):
        try:
            system = self.cursor.execute(
                "SELECT system FROM sys_sel WHERE  id = %s", (i_id,))
            system = self.cursor.fetchone()
            if system is None:
                res = 0
            else:
                res = system[0]
        except Exception as error:
            print('error: {}'.format(error))
            return 'error: {}'.format(error)
        else:
            return str(res)

    def __del__(self):
        self.connection.close()
        self.cursor.close()