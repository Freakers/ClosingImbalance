import urllib.request
import urllib.response
import time
import threading
import os
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol


class calculatemedian:

    def __init__(self, min=0, max=1, value=0.5):
        self.min = float(min)
        self.max = float(max)
        self.spread = float(max) - float(min)
        self.minmedian = self.spread * 0.25 + self.min
        self.maxmedian = self.spread * 0.75 + self.max
        self.value = float(value)
        # print("Min   : " + str(self.min))
        # print("Max   : " + str(self.max))
        # print("Spread: " + str(self.spread))
        # print("Value : " + str(self.value))
        # print("MinMedian: " +str(self.minmedian))
        # print("MaxMedian: " +str(self.maxmedian))

    def getminmedian(self):
        return self.minmedian

    def getmaxmedian(self):
        return self.maxmedian

    def ismedianvalue(self):
        if self.value >= self.minmedian and self.value <= self.maxmedian:
            return True
        else:
            return False


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
        self.totalbidvolume = self.totalbidvolume + int(bidvol)
        self.totalaskvolume = self.totalaskvolume + int(askvol)
        msg['msgtime'] = msgtime
        msg['bidpr'] = bidpr
        msg['askpr'] = askpr
        msg['bidvol'] = bidvol
        msg['askvol'] = askvol
        msg['totbidvol'] = self.totalbidvolume
        msg['totaskvol'] = self.totalaskvolume
        #print("Processing L1 Message")
        self.l1[symbol] = msg
        #self.list()`

    def list(self):
        print(self.l1.items().__str__())

class Symbols:

    def __init__(self, file="C:\\Users\\tctech\\Desktop\\Trading Assignments\\Stock List\\SymbolLists\\TestSymbol.txt"):
        print("Initiate Symbols")
        self.symbols = {}
        self.loadsymbols(file)
        print(self.symbols.__len__())
        self.listsymbols()
        # self.deregistersymbol()
        self.registersymbols()

    def setsymbols(self, record, sym):
        self.symbols[record] = sym

    def getsymbols(self):
        return self.symbols

    def registersymbols(self):
        print("Starting THREADS to register L1 AND TOS for Symbol List")
        for record, symbol in self.symbols.items():
            print(symbol)
            t = threading.Thread(target=self.registersymbol, args=(symbol, "L1", "5555", ))
            t.start()
            t = threading.Thread(target=self.registersymbol, args=(symbol, "TOS", "5555", ))
            t.start()

    def deregistersymbols(self):
        print("Starting THREADS to deregister L1 AND TOS for Symbol List")
        for record, symbol in self.symbols.items():
            print(symbol)
            t = threading.Thread(target=self.deregistersymbol, args=(symbol, "L1", "1", ))
            t.start()
            t = threading.Thread(target=self.deregistersymbol, args=(symbol, "TOS", "1", ))
            t.start()

    def registersymbol(self, symbol, feedType, output):
        print('Register Symbol Request  : http://localhost:8080/Register?symbol='+symbol+'&feedtype='+feedType)
        with urllib.request.urlopen('http://localhost:8080/Register?symbol='+symbol+'&feedtype='+feedType) \
                as response1:
            html1: object = response1.read()
            print("Register Symbol Response : " + html1.__str__())
        print('http://localhost:8080/SetOutput?symbol='+symbol +'&feedtype='+feedType+'&output='+output+'&status=on')
        with urllib.request.urlopen('http://localhost:8080/SetOutput?symbol='+symbol +
                                    '&feedtype='+feedType+'&output='+output+'&status=on') as response2:
            html2: object = response2.read()
            print("Register Output: "+html2.__str__())

    def deregistersymbol(self, symbol, feedType, region):
        print('Deregister Symbol Request  : http://localhost:8080/Deregister?symbol='+symbol+'&region=' +
              region+'&feedtype='+feedType)
        with urllib.request.urlopen('http://localhost:8080/Deregister?symbol='+symbol+'&region='+region +
                                    '&feedtype='+feedType) as response1:
            html1: object = response1.read()
            print("Deregister Symbol Response : " + html1.__str__())

    def loadsymbols(self, file):
        print("Start Load File: " + time.asctime())
        print("Current Working Directory: " + file)
        file = open(file, "r")
        recordcount = 1
        for symbol in file:
            #print(symbol.rstrip())
            self.symbols[recordcount] = symbol.rstrip()
            recordcount += 1

    def listsymbols(self):
        for rec, symbol in self.symbols.items():
            print("Symbol["+str(rec)+"]: " + symbol)


class ppro_datagram(DatagramProtocol):

    def __init__(self, s="GOOS.NY"):
        self.level1 = L1()
        self.bidpr = ""
        self.askpr = ""
        self.askvolume = ""
        self.bidvolume = ""
        self.asks = 0
        self.bids = 0
        self.neutrals = 0
        self.time = ""
        self.this_symbol = s
        self.symbol = ""

    def startProtocol(self):
        # code here what you want to start upon listner creation..
        # I use this space to connect to my logging backend and inter process communication library
        print('starting up..')

    def datagramReceived(self, data, addr):
        # decode byte data from UDP port into string, and replace spaces with NONE
        msg = data.decode("utf-8").replace(' ', 'NONE')

        # empty dict we will populate with the string data
        message_dict = {}

        # when processing PPro8 data feeds, processing the line into a dictionary is very useful:
        for item in msg.split(','):
            couple = item.split('=')
            message_dict[couple[0]] = couple[1]
        #print(message_dict.__str__())
        # now you can call specific data by name in the line you're processing instead of counting colums
        # See the print statement below for examples

        #print('{} {} {}'.format(message_dict['Symbol'], message_dict['Message'], msg))
        if message_dict['Message'] == "L1":
            self.symbol = message_dict['Symbol']
            if self.symbol == self.this_symbol.__str__():
                self.bidpr = message_dict['BidPrice']
                self.askpr = message_dict['AskPrice']
                self.asksize = message_dict['AskSize']
                self.bidsize = message_dict['BidSize']
                self.time = message_dict['MarketTime']
                # print("L1 Time: "+message_dict['MarketTime'] + " Symbol: " + message_dict['Symbol'])
                # print("     Bid Price: " + message_dict['BidPrice'] + " Bid Size: " + message_dict['BidSize'])
                # print("     Ask Price: " + message_dict['AskPrice'] + " Ask Size: " + message_dict['AskSize'])
                # x = 1
                self.level1.update(message_dict['Symbol'], message_dict['BidPrice'], message_dict['AskPrice'], message_dict['BidSize'], message_dict['AskSize'], message_dict['MarketTime'])

        if message_dict['Message'] == "TOS":
            # print("TOS Time: " + message_dict['MarketTime'] + " Price: " + message_dict['Price'] +
            #       " Size: " + message_dict['Size'])
            self.symbol = message_dict['Symbol']
            if self.symbol == self.this_symbol:
                tosprice = message_dict['Price']
                tosmarkettime = message_dict['MarketTime']
                #print("TOS Price = "+tosprice)
                print(tosmarkettime+": L1 Bid @ " + self.bidpr + "\tSize: " + self.bidsize + "\tAsk @ " + self.askpr + "\tSize: " + self.asksize)

                if float(tosprice) <= float(self.askpr) and float(tosprice) >= float(self.bidpr):
                    if float(tosprice) != float(self.askpr) and float(tosprice) != float(self.bidpr):
                        print(tosmarkettime+": Mid Point Trade: " + tosprice + " Trade Size: " + message_dict['Size'])
                        if calculatemedian(self.bidpr, self.askpr, tosprice).ismedianvalue():
                            self.neutrals = self.neutrals + int(message_dict['Size'])
                        else:
                            if float(tosprice) <= calculatemedian(self.bidpr, self.askpr, tosprice).getminmedian():
                                self.bids = self.bids + int(message_dict['Size'])
                            if float(tosprice) <= calculatemedian(self.bidpr, self.askpr, tosprice).getmaxmedian():
                                self.asks = self.asks + int(message_dict['Size'])
                    else:
                        print(tosmarkettime+": Traded @ " + tosprice + " Size: " + message_dict['Size'])
                        if float(tosprice) == float(self.askpr):
                            self.asks = self.asks + int(message_dict['Size'])
                        if float(tosprice) == float(self.bidpr):
                            self.bids = self.bids + int(message_dict['Size'])
                    print("     Bid Price: " + self.bidpr + "\t Bid Size: " + self.bidsize)
                    print("     Ask Price: " + self.askpr + "\t Ask Size: " + self.asksize)
                    print("     Bid Trade: " + self.bids.__str__())
                    print("     Ask Trade: " + self.asks.__str__())
                    print("     Mid Trade: " + self.neutrals.__str__())
            # but any named column will not be callable:
            # message_dict['MarketTime'] " + message_dict['Symbol'])
            #             print("     Bid Price: " + message_dict['BidPrice'] + " Bid Size: " + message_dict['BidSize'])
            #             print("     Ask Price: " + message_dict['AskPrice'] + " Ask Size: " + message_dict['AskSize'])
            # message_dict['Price']

    def connectionRefused(self):
        print("No one listening")

Symbols()
time.sleep(5)
reactor.listenUDP(5555, ppro_datagram())
reactor.run()
