import aerospike

class AerospikeReader:
    def __init__(self, *args, **kwargs):
        if 'host' in kwargs:
            self.host = kwargs['host']
        else:
            print 'missing host argument, using 127.0.0.1'
            self.host = '127.0.0.1'
        if 'port' in kwargs:
            self.port = kwargs['port']
        else:
            print 'missing port argument, using 3000'
            self.port = 3000
        if 'namespace' in kwargs:
            self.namespace = kwargs['namespace']
        else:
            print 'missing namespace argument, using data'
            self.namespace = 'data'
        if 'set' in kwargs:
            self.set = kwargs['set']
        else:
            print 'missing set argument, using DataTable'
            self.set = 'DataTable'

    def read(self, *args, **kwargs):
        config = {'hosts': [ (self.host, self.port) ]}
        client = aerospike.client(config).connect()
        
        list_of_dicts = []
        scan = client.scan(self.namespace, self.set)
        def append_result((key, metadata, record)):
            list_of_dicts.append(record)
        scan.foreach(append_result)
        
        return list_of_dicts

