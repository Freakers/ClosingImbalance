import mysql.connector

class MysqlReader:
    def __init__(self, *args, **kwargs):
        if 'database' in kwargs:
            self.db_mysql = kwargs['database']
        else:
            print 'missing database argument, using data'
            self.db_mysql = 'data'
        if 'user' in kwargs:
            self.user_mysql = kwargs['user']
        else:
            print 'missing user argument, using root'
            self.user_mysql = 'root'
        if 'table' in kwargs:
            self.db_table = kwargs['table']
        else:
            print 'missing table argument, using DataTable'
            self.db_table = 'DataTable'

    def read(self, *args, **kwargs):
        db = mysql.connector.connect(user=self.user_mysql, database=self.db_mysql)
        cursor = db.cursor(dictionary=True)
        
        SELECT_SQL = (
            "SELECT * FROM "+self.db_table
        )
        
        cursor.execute(SELECT_SQL)
        return [row for row in cursor]

