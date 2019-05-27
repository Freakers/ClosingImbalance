class L1:
    def __init__(self):
        self.numofbids = 0
        self.numofasks = 0
        self.numoftrades = 0
        self.totalbidvolume = 0
        self.totalaskvolume = 0
        self.totaldownticks = 0
        self.totalupticks = 0
        print("Init L1 Object")
        self.l1 = {}

    def update(self, symbol, bidpr, askpr, bidvol, askvol, msgtime):
        msg = {}
        self.totalbidvolume = self.totalbidvolume + bidvol
        self.totalaskvolume = self.totalaskvolume + askvol
        msg['msgtime'] = msgtime
        msg['bidpr'] = bidpr
        msg['askpr'] = askpr
        msg['bidvol'] = bidvol
        msg['askvol'] = askvol
        print("Processing L1 Message")
        self.l1[symbol] = msg


    def list(self):
        print("List")

