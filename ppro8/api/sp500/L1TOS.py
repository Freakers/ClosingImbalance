import urllib.request
import urllib.response
import time
import threading
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


class OrderStatus:

    def __init__(self):
        self.LocalTime = ""
        self.MarketDateTime = ""
        self.Currency = ""
        self.Symbol = ""
        self.Gateway = ""
        self.Side = ""
        self.OrderNumber = ""
        self.Price = ""
        self.Shares = ""
        self.Position = ""
        self.OrderState = ""
        self.MarketID = ""
        self.CurrencyChargeGway = ""
        self.ChargeGway = ""
        self.CurrencyChargeAct = ""
        self.ChargeAct = ""
        self.CurrencyChargeSec = ""
        self.ChargeSec = ""
        self.CurrencyChargeExec = ""
        self.ChargeExec = ""
        self.CurrencyChargeClr = ""
        self.ChargeClr = ""
        self.OrderFlags = ""
        self.CurrencyCharge = ""
        self.Account = ""
        self.InfoCode = ""
        self.InfoText = ""
        self.OrderStatus = {}

    def update(self, symbol, localtime, msgtime, side, price, shares, position, order_state, order_flags):
        msg = {}
        msg['LocalTime'] = localtime
        msg['MarketDateTime'] = msgtime
        msg['Symbol'] = symbol
        msg['Side'] = side
        msg['Price'] = price
        msg['Shares'] = shares
        msg['Position'] = position
        msg['OrderState'] = order_state
        msg['OrderFlags'] = order_flags
        print("Processing Order Status Message")
        self.OrderStatus[symbol + msgtime] = msg


class OrderEvents:

    def __init__(self):
        self.LocalTime = ""
        self.Messaage = ""
        self.MarketDateTime = ""
        self.OrderNumber = ""
        self.OriginatorSeqId = ""
        self.EventMessageType = ""
        self.EventFlavour = ""
        self.EventOriginatorId = ""
        self.Price = ""
        self.Size = ""
        self.Description = ""
        self.OrderEvent = {}

    def update(self, localtime, msg, msgtime, ordnum, orginatorseqid, eventmsgtype, eventflavour, eventorginatorid,
               price, size, description):
        msg = {}
        msg['LocalTime'] = localtime
        msg['Message'] = msg
        msg['MarketDateTime'] = msgtime
        msg['EventMessageType'] = eventmsgtype
        msg['EventFlavour'] = eventflavour
        msg['EventOriginatorId'] = eventorginatorid
        msg['OriginatorSeqId'] = orginatorseqid
        msg['Size'] = size
        msg['Price'] = price
        msg['Description'] = description
        print("Processing Order Event Message")
        self.OrderEvent[orginatorseqid] = msg

    def get_events(self):
        for key, event in self.OrderEvent.items():
            print(key, event)


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
        # print("Processing L1 Message")
        self.l1[symbol] = msg
        # self.list()`

    def list(self):
        print(self.l1.items().__str__())


class Orders:

    def __init__(self, feed_type="5555", region="1"):
        print("Order Status Object")
        self.registerorderstatus(feed_type, region)
        self.registerorderevent(feed_type, region)

    def registerorderstatus(self, feedtype, region):
        print("Register Order Status - Region: " + region + "\tFeed: " + feedtype)
        # Register?region=1&feedtype=OSTAT&output=[bytype]
        print('Register Order Status Request  : http://localhost:8080/Register?region=' +
              region + '&feedtype=ORDEREVENT&output=' + feedtype)
        with urllib.request.urlopen('http://localhost:8080/Register?region=' +
                                    region + '&feedtype=ORDEREVENT&output=' + feedtype) as response1:
            html1: object = response1.read()
            print("Register Order Status Response : " + html1.__str__())

    def registerorderevent(self, feedtype, region):
        print("Register Order Event - Region: " + region + "\tFeed: " + feedtype)
        # Register?region=1&feedtype=ORDEREVENT & output=[bykey|bytype]
        print('Register Order Request  : http://localhost:8080/Register?region=' +
              region + '&feedtype=ORDEREVENT&output=' + feedtype)
        with urllib.request.urlopen('http://localhost:8080/Register?region=' +
                                    region + '&feedtype=ORDEREVENT&output=' + feedtype) as response1:
            html1: object = response1.read()
            print("Register Order Event Response : " + html1.__str__())


class Symbols:

    def __init__(self, file="C:\\Users\\tctech\\Desktop\\Trading Assignments\\Stock List\\SymbolLists\\L1TOS_ASIA.txt"):
        print("Initiate Symbols from " + file.__str__())
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
            t = threading.Thread(target=self.registersymbol, args=(symbol, "L1", "5555",))
            t.start()
            t = threading.Thread(target=self.registersymbol, args=(symbol, "TOS", "5555",))
            t.start()

    def deregistersymbols(self):
        print("Starting THREADS to deregister L1 AND TOS for Symbol List")
        for record, symbol in self.symbols.items():
            print(symbol)
            t = threading.Thread(target=self.deregistersymbol, args=(symbol, "L1", "1",))
            t.start()
            t = threading.Thread(target=self.deregistersymbol, args=(symbol, "TOS", "1",))
            t.start()

    def registersymbol(self, symbol, feedType, output):
        print('Register Symbol Request  : http://localhost:8080/Register?symbol=' + symbol + '&feedtype=' + feedType)
        with urllib.request.urlopen('http://localhost:8080/Register?symbol=' + symbol + '&feedtype=' + feedType) \
                as response1:
            html1: object = response1.read()
            print("Register Symbol Response : " + html1.__str__())
        print(
            'http://localhost:8080/SetOutput?symbol=' + symbol + '&feedtype=' + feedType + '&output=' + output + '&status=on')
        with urllib.request.urlopen('http://localhost:8080/SetOutput?symbol=' + symbol +
                                    '&feedtype=' + feedType + '&output=' + output + '&status=on') as response2:
            html2: object = response2.read()
            print("Register Output: " + html2.__str__())

    def deregistersymbol(self, symbol, feedType, region, output):
        print('Deregister Symbol Request  : http://localhost:8080/Deregister?symbol=' + symbol + '&region=' +
              region + '&feedtype=' + feedType)
        with urllib.request.urlopen('http://localhost:8080/SetOutput?symbol=' + symbol +
                                    '&feedtype=' + feedType + '&output=' + output + '&status=off') as response0:
            html0: object = response0.read()
            print("Deregister Symbol Response : " + html0.__str__())
        with urllib.request.urlopen('http://localhost:8080/Deregister?symbol=' + symbol + '&region=' + region +
                                    '&feedtype=' + feedType) as response1:
            html1: object = response1.read()
            print("Deregister Symbol Response : " + html1.__str__())

    def loadsymbols(self, file):
        print("Start Load File: " + time.asctime())
        print("Current Working Directory: " + file)
        file = open(file, "r")
        recordcount = 1
        for symbol in file:
            # print(symbol.rstrip())
            self.symbols[recordcount] = symbol.rstrip()
            recordcount += 1

    def listsymbols(self):
        for rec, symbol in self.symbols.items():
            print("Symbol[" + str(rec) + "]: " + symbol)


class SellFutures:
    """Submit Futures Contract to sell based on the symbol and contract size, default is ES|M19.CM 1 Contract"""

    def __init__(self, symbol="MES\M19.CM", shares="1"):
        print("Sell " + shares + " Contract Market:" + symbol)
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=' + symbol +
                                    '&ordername=CME%20Sell%20CME%20Market%20DAY' +
                                    '&shares=' + shares) as response1:
            html1: object = response1.read()
            print("API - Execute Order Response : " + html1.__str__())


class CancelFuture:
    """Submit Futures Contract to cancel the order based on
        the order number associated to the symbol, default is ES|M19.CM"""

    def __init__(self, ordernumber="1234567890", symbol="MES\M19.CM"):
        print("Cancel Order Number: " + ordernumber + " for symbol: " + symbol)
        with urllib.request.urlopen('http://localhost:8080/CancelOrder?type=ordernumber' +
                                    '&ordernumber=' + '&symbol=' + symbol) as response1:
            html1: object = response1.read()
            print("API - Cancel Order Response : " + html1.__str__())


class BuyFutures:
    """Submit Futures Contract to buy based on the symbol and contract size, default is ES|M19.CM 1 Contract"""

    def __init__(self, symbol="MES\\U19.CM", shares="1"):
        print("Sell " + shares + " Contract Market:" + symbol)
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=' + symbol +
                                    '&ordername=CME%20Buy%20CME%20Market%20DAY' +
                                    '&shares=' + shares) as response1:
            html1: object = response1.read()
            print("API - Execute Order Response : " + html1.__str__())


class ppro_datagram(DatagramProtocol):

    def __init__(self, s="XLF.AM"):
        self.level1 = L1()
        self.order_status = OrderStatus()
        self.order_event = OrderEvents()
        self.bidpr = ""
        self.askpr = ""
        self.asksize = ""
        self.bidsize = ""
        self.asks = 0
        self.bids = 0
        self.neutrals = 0
        self.time = ""
        self.this_symbol = s
        self.symbol = ""
        self.starttime = time.time()
        print("\nStarting L1TOS monitor for symbol: " + self.this_symbol.__str__())

    def startProtocol(self):
        # code here what you want to start upon listener creation..
        # I use this space to connect to my logging backend and inter process communication library
        print('starting up..')

    def datagramReceived(self, data, addr):
        self.elapsedtime()
        # decode byte data from UDP port into string, and replace spaces with NONE
        msg = data.decode("utf-8").replace(' ', 'NONE')

        # empty dict we will populate with the string data
        message_dict = {}

        # when processing PPro8 data feeds, processing the line into a dictionary is very useful:
        for item in msg.split(','):
            # print(item)
            if "=" in item:
                couple = item.split('=')
                message_dict[couple[0]] = couple[1]
        # print(message_dict.__str__())
        # now you can call specific data by name in the line you're processing instead of counting colums
        # See the print statement below for examples

        # print('{}\t{}\t{}'.format(message_dict['Symbol'], message_dict['Message'], msg))
        if message_dict['Message'] == "OrderEvent":
            print("Order Event Message")

        if message_dict['Message'] == "OrderStatus":
            ltime = str(message_dict['LocalTime'])
            mtime = str(message_dict['MarketDateTime'])
            sym = str(message_dict['Symbol'])
            side = str(message_dict['Side'])
            price = str(message_dict['Price'])
            shares = str(message_dict['Shares'])
            position = str(message_dict['Position'])
            orderstate = str(message_dict['OrderState'])
            orderflags = str(message_dict['OrderFlags'])
            self.order_status.update(message_dict['LocalTime'],
                                     message_dict['MarketDateTime'],
                                     message_dict['Symbol'],
                                     message_dict['Side'],
                                     message_dict['Price'],
                                     message_dict['Shares'],
                                     message_dict['Position'],
                                     message_dict['OrderState'],
                                     message_dict['OrderFlags'])
        if message_dict['Message'] == "L1":
            self.symbol = message_dict['Symbol']
            if self.symbol == self.this_symbol.__str__():
                self.bidpr = message_dict['BidPrice']
                self.askpr = message_dict['AskPrice']
                self.asksize = message_dict['AskSize']
                self.bidsize = message_dict['BidSize']
                self.time = message_dict['MarketTime']
                # print("L1 Time: "+message_dict['MarketTime'] + " Symbol: " + message_dict['Symbol'])
                # print("L1-> Bid Price:\t" + message_dict['BidPrice'] + "\tBid Size: " + message_dict['BidSize'])
                # print("L1-> Ask Price:\t" + message_dict['AskPrice'] + "\tAsk Size: " + message_dict['AskSize'])
                # print(self.time+"\tBid Price:\t" + self.bidpr + "\tBid Size:\t" + self.bidsize + "\tAsk Price:\t" +
                #       self.askpr + "\tAsk Size:\t" + self.asksize)
                # # x = 1
                self.level1.update(message_dict['Symbol'], message_dict['BidPrice'], message_dict['AskPrice'],
                                   message_dict['BidSize'], message_dict['AskSize'], message_dict['MarketTime'])

        if message_dict['Message'] == "TOS":
            # print("TOS Time: " + message_dict['MarketTime'] + " Price: " + message_dict['Price'] +
            #       " Size: " + message_dict['Size'])
            self.symbol = message_dict['Symbol']
            if self.symbol == self.this_symbol:
                tosprice = message_dict['Price']
                tosmarkettime = message_dict['MarketTime']
                # print("TOS Price = "+tosprice)
                print(tosmarkettime + ": L1 Bid @ " + self.bidpr + "\tSize: " + self.bidsize +
                      "\tAsk @ " + self.askpr + "\tSize: " + self.asksize)

                if float(tosprice) <= float(self.askpr) and float(tosprice) >= float(self.bidpr):
                    if float(tosprice) != float(self.askpr) and float(tosprice) != float(self.bidpr):
                        print(tosmarkettime + ": Mid Point Trade: " + tosprice + " Trade Size: " + message_dict['Size'])
                        if calculatemedian(self.bidpr, self.askpr, tosprice).ismedianvalue():
                            self.neutrals = self.neutrals + int(message_dict['Size'])
                        else:
                            if float(tosprice) <= calculatemedian(self.bidpr, self.askpr, tosprice).getminmedian():
                                self.bids = self.bids + int(message_dict['Size'])
                            if float(tosprice) <= calculatemedian(self.bidpr, self.askpr, tosprice).getmaxmedian():
                                self.asks = self.asks + int(message_dict['Size'])
                    else:
                        print(tosmarkettime + ": Traded @ " + tosprice + " Size: " + message_dict['Size'])
                        if float(tosprice) == float(self.askpr):
                            self.asks = self.asks + int(message_dict['Size'])
                        if float(tosprice) == float(self.bidpr):
                            self.bids = self.bids + int(message_dict['Size'])
                    print("Bid Price:\t" + self.bidpr + "\tBid Size:\t" + self.bidsize + "\tAsk Price:\t" +
                          self.askpr + "\tAsk Size:\t" + self.asksize)
                    print("Trade into Bid:\t" + self.bids.__str__())
                    print("Trade into Ask:\t" + self.asks.__str__())
                    print("Trade MidPoint:\t" + self.neutrals.__str__() + '\n')
            # but any named column will not be callable:
            # message_dict['MarketTime'] " + message_dict['Symbol'])
            #             print("     Bid Price: " + message_dict['BidPrice'] + " Bid Size: " + message_dict['BidSize'])
            #             print("     Ask Price: " + message_dict['AskPrice'] + " Ask Size: " + message_dict['AskSize'])
            # message_dict['Price']

    def connectionRefused(self):
        print("No one listening")

    def elapsedtime(self):
        if time.time() - self.starttime > 60.00:
            self.starttime = time.time()
            self.asks = 0
            self.bids = 0
            self.neutrals = 0


class ppro_order_datagram(DatagramProtocol):

    def __init__(self, s="MES\\U19.CM"):
        self.level1 = L1()
        self.order_status = OrderStatus()
        self.order_event = OrderEvents()
        self.bidpr = ""
        self.askpr = ""
        self.asksize = ""
        self.bidsize = ""
        self.asks = 0
        self.bids = 0
        self.neutrals = 0
        self.time = ""
        self.this_symbol = s
        self.symbol = ""
        self.starttime = time.time()
        print("\nStarting L1TOS monitor for symbol: " + self.this_symbol.__str__())

    def startProtocol(self):
        # code here what you want to start upon listner creation..
        # I use this space to connect to my logging backend and inter process communication library
        print('starting up..')

    def datagramReceived(self, data, addr):
        self.elapsedtime()
        # decode byte data from UDP port into string, and replace spaces with NONE
        msg = data.decode("utf-8").replace(' ', 'NONE')

        # empty dict we will populate with the string data
        message_dict = {}

        # when processing PPro8 data feeds, processing the line into a dictionary is very useful:
        for item in msg.split(','):
            # print(item)
            if "=" in item:
                couple = item.split('=')
                message_dict[couple[0]] = couple[1]
        # print(message_dict.__str__())
        # now you can call specific data by name in the line you're processing instead of counting colums
        # See the print statement below for examples

        # print('{}\t{}\t{}'.format(message_dict['Symbol'], message_dict['Message'], msg))
        # def update(self, localtime, msg, msgtime, ordnum, orginatorseqid, eventmsgtype, eventflavour, eventorginatorid,
        #            price, size, description):

        if message_dict['Message'] == "OrderEvent":
            message = message_dict['Message']
            ltime = str(message_dict['LocalTime'])
            mtime = str(message_dict['MarketDateTime'])
            ordernum = str(message_dict['OrderNumber'])
            originatorseqid = str(message_dict['OriginatorSeqId'])
            eventtype = str(message_dict['EventMessageType'])
            eventoriginid = str(message_dict['EventOriginatorId'])
            eventflavor = str(message_dict['EventFlavour'])
            price = str(message_dict['Price'])
            size = str(message_dict['Size'])
            description = str(message_dict['Description'])
            self.order_event.update(ltime, message, mtime, ordernum, originatorseqid, eventtype, eventflavor,
                                    eventoriginid, price, size, description)
            print("Incomming OE Message: " + msg)
            # print("Order Event Objects get events")
            # print(self.order_event.get_events())

        if message_dict['Message'] == "OrderStatus":
            ltime = str(message_dict['LocalTime'])
            mtime = str(message_dict['MarketDateTime'])
            sym = str(message_dict['Symbol'])
            side = str(message_dict['Side'])
            price = str(message_dict['Price'])
            shares = str(message_dict['Shares'])
            position = str(message_dict['Position'])
            orderstate = str(message_dict['OrderState'])
            orderflags = str(message_dict['OrderFlags'])
            self.order_status.update(message_dict['LocalTime'],
                                     message_dict['MarketDateTime'],
                                     message_dict['Symbol'],
                                     message_dict['Side'],
                                     message_dict['Price'],
                                     message_dict['Shares'],
                                     message_dict['Position'],
                                     message_dict['OrderState'],
                                     message_dict['OrderFlags'])
            print("Order Status Message: " + msg)
        if message_dict['Message'] == "L1":
            self.symbol = message_dict['Symbol']
            if self.symbol == self.this_symbol.__str__():
                self.bidpr = message_dict['BidPrice']
                self.askpr = message_dict['AskPrice']
                self.asksize = message_dict['AskSize']
                self.bidsize = message_dict['BidSize']
                self.time = message_dict['MarketTime']
                # print("L1 Time: "+message_dict['MarketTime'] + " Symbol: " + message_dict['Symbol'])
                # print("L1-> Bid Price:\t" + message_dict['BidPrice'] + "\tBid Size: " + message_dict['BidSize'])
                # print("L1-> Ask Price:\t" + message_dict['AskPrice'] + "\tAsk Size: " + message_dict['AskSize'])
                # print(self.time+"\tBid Price:\t" + self.bidpr + "\tBid Size:\t" + self.bidsize + "\tAsk Price:\t" +
                #       self.askpr + "\tAsk Size:\t" + self.asksize)
                # # x = 1
                self.level1.update(message_dict['Symbol'], message_dict['BidPrice'], message_dict['AskPrice'],
                                   message_dict['BidSize'], message_dict['AskSize'], message_dict['MarketTime'])

        if message_dict['Message'] == "TOS":
            # print("TOS Time: " + message_dict['MarketTime'] + " Price: " + message_dict['Price'] +
            #       " Size: " + message_dict['Size'])
            self.symbol = message_dict['Symbol']
            if self.symbol == self.this_symbol:
                print("In TOS Message by symbol")
                tosprice = message_dict['Price']
                tosmarkettime = message_dict['MarketTime']
                # print("TOS Price = "+tosprice)
                # print(tosmarkettime+": L1 Bid @ " + self.bidpr + "\tSize: " + self.bidsize +
                #       "\tAsk @ " + self.askpr + "\tSize: " + self.asksize)
            #         print("Bid Price:\t" + self.bidpr + "\tBid Size:\t" + self.bidsize + "\tAsk Price:\t" +
            #               self.askpr + "\tAsk Size:\t" + self.asksize)
            #         print("Trade into Bid:\t" + self.bids.__str__())
            #         print("Trade into Ask:\t" + self.asks.__str__())
            #         print("Trade MidPoint:\t" + self.neutrals.__str__()+'\n')
            # # but any named column will not be callable:
            # message_dict['MarketTime'] " + message_dict['Symbol'])
            #             print("     Bid Price: " + message_dict['BidPrice'] + " Bid Size: " + message_dict['BidSize'])
            #             print("     Ask Price: " + message_dict['AskPrice'] + " Ask Size: " + message_dict['AskSize'])
            # message_dict['Price']

    def connectionRefused(self):
        print("No one listening")

    def elapsedtime(self):
        if time.time() - self.starttime > 60.00:
            self.starttime = time.time()
            self.asks = 0
            self.bids = 0
            self.neutrals = 0


Symbols("C:\\Users\\tctech\\Desktop\\Trading Assignments\\Stock List\\SymbolLists\\L1TOS_NCSA.txt")
time.sleep(5)
reactor.listenUDP(5555, ppro_datagram("MES\\U19.CM"))
reactor.run()
