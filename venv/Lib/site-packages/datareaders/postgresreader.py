import psycopg2
from psycopg2 import extras

class PostgresReader:
    def __init__(self, *args, **kwargs):
        if 'host' in kwargs:
            self.host = kwargs['host']
        else:
            print 'missing host argument, using localhost'
            self.host = 'localhost'
        if 'database' in kwargs:
            self.db_postgres = kwargs['database']
        else:
            print 'missing database argument, using data'
            self.db_postgres = 'data'
        if 'user' in kwargs:
            self.user_postgres = kwargs['user']
        else:
            print 'missing user argument, using postuser'
            self.user_postgres = 'postuser'
        if 'password' in kwargs:
            self.pass_postgres = kwargs['password']
        else:
            print 'missing password argument, using postpass'
            self.pass_postgres = 'postpass'
        if 'table' in kwargs:
            self.db_table = kwargs['table']
        else:
            print 'missing table argument, using DataTable'
            self.db_table = 'DataTable'

    def read(self, *args, **kwargs):
        db = psycopg2.connect("dbname='"+self.db_postgres+"' user='"+self.user_postgres+"' host='"+self.host+"' password='"+self.pass_postgres+"'")
        cursor = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        SELECT_SQL = ("SELECT * FROM "+self.db_table)
        
        cursor.execute(SELECT_SQL)
        rows = cursor.fetchall()
        return [row for row in rows]
