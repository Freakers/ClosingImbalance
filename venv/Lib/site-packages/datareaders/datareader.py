readers = {}

from notimplementedreader import FailedReader

try:
    from mysqlreader import MysqlReader
    readers['mysql'] = MysqlReader
except ImportError:
    readers['mysql'] = FailedReader
try:
    from sqlitereader import SqliteReader
    readers['sqlite'] = SqliteReader
except ImportError:
    readers['sqlite'] = FailedReader
try:
    from csvreader import CsvReader
    readers['csv'] = CsvReader
except ImportError:
    readers['csv'] = FailedReader
try:
    from redisreader import RedisReader
    readers['redis'] = RedisReader
except ImportError:
    readers['redis'] = FailedReader
try:
    from mongoreader import MongoReader
    readers['mongo'] = MongoReader
except ImportError:
    readers['mongo'] = FailedReader
try:
    from postgresreader import PostgresReader
    readers['postgres'] = PostgresReader
except ImportError:
    readers['postgres'] = FailedReader
try:
    from aerospikereader import AerospikeReader
    readers['aerospike'] = AerospikeReader
except ImportError:
    readers['aerospike'] = FailedReader
try:
    from datawriters.datawriter import DataWriter
except ImportError:
    pass

class DataReader:

    readers = readers

    def __init__(self, *args, **kwargs):
        self.reader_name = kwargs['reader']
        self.reader = self.readers[kwargs['reader']](*args, **kwargs)
        try:
            self.writer = DataWriter(writer=self.reader_name, *args, **kwargs)
        except:
            pass
        
    def reinit(self, *args, **kwargs):
        self.__init__(*args, **kwargs)
        
    def read(self, *args, **kwargs):
        list_of_dicts = self.reader.read(*args, **kwargs)
        if isinstance(list_of_dicts, list):
            print 'Data read from '+self.reader_name
        return list_of_dicts
        
    def save(self, list_of_dicts, *args, **kwargs):
        try:
            self.writer.save(list_of_dicts, *args, **kwargs)
            print 'Data writen to '+self.write_name
        except:
            print "Can't save without DataWriter"
        
    def test(self, *args, **kwargs):
        try:
            data = [{"column1":"row1-item1", "column2":"row1-item2"},
                    {"column1":"row2-item1", "column2":"row2-item2"},
                    {"column1":"row3-item1", "column2":"row3-item2"}]
            self.writer.save(data)
            return self.reader.read()
        except:
            print "Can't test without DataWriter"

if __name__ == "__main__":
    print DataReader(reader='sqlite').test()

