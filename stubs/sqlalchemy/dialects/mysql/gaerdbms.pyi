# Stubs for sqlalchemy.dialects.mysql.gaerdbms (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from .mysqldb import MySQLDialect_mysqldb as MySQLDialect_mysqldb

class MySQLDialect_gaerdbms(MySQLDialect_mysqldb):
    @classmethod
    def dbapi(cls): ...
    @classmethod
    def get_pool_class(cls, url): ...
    def create_connect_args(self, url): ...

dialect: Any = ...
