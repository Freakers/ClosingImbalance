class FailedReader:
    def __init__(self, *args, **kwargs):
        self.reader_name = kwargs['reader']
        print self.reader_name + " failed, did you install its requirements?"

    def read(self, *args, **kwargs):
        print 'Could not read using ' + self.reader_name + ", import failed"
