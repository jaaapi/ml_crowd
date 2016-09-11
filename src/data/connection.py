# -*- coding: utf-8 -*-
import os
import logging
import sqlite3 as sqlite
from sqlalchemy import create_engine


class Connection:
    def __init__(self, database_path):
        log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(level=logging.INFO, format=log_fmt)
        self.logger = logging.getLogger(__name__)
        self.connection = self.load_database(database_path)
        self.cursor = None

    def load_database(self, absolute_path):
        self.logger.info('loading database from: %s', absolute_path)
        disk_engine = create_engine('sqlite:///{path}'.format(path=absolute_path))
        return disk_engine

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        if self.cursor is None:
            self.cursor = self.connection.cursor()

        return self.cursor

    def close_cursor(self):
        self.cursor.close()
        self.cursor = None

    def close_database(self):
        self.connection.close()

