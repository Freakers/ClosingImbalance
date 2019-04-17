import sqlite3

class SqliteReader:
    def __init__(self, *args, **kwargs):
        if 'database' in kwargs:
            self.db_sqlite3 = kwargs['database']
        else:
            print 'missing database argument, using data.sqlite'
            self.db_sqlite3 = 'data.sqlite'
        if 'table' in kwargs:
            self.db_table = kwargs['table']
        else:
            print 'missing table argument, using DataTable'
            self.db_table = 'DataTable'

    def read(self, *args, **kwargs):
        db = sqlite3.connect(self.db_sqlite3)
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        
        SELECT_TABLE = '''SELECT * FROM '''+self.db_table
        
        cursor.execute(SELECT_TABLE)
        existing_rows = [{key:row[row.keys().index(key)] for key in row.keys()} for row in cursor.fetchall()]
        return existing_rows
        
