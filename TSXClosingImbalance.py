import urllib.request
import urllib.response
import time
import os
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol

class Symbols:
    symbols = {}

    def _init__(self):
        print("Hello")

    def setsymbols(self, record, sym):
        self.symbols[record] = sym

    def getsymbols(self):
        return print(self.symbols.__str__())


class RegisterSymbol:
    """Registers a single symbol in PPro8 API"""
    def __init__(self, symbol="CRON.TO", feedType="TOS", output="btype"):
        print("Rergister Symbol")
        print('Register Symbol Request  : http://localhost:8080/Register?symbol='+symbol+'&feedtype='+feedType)
        with urllib.request.urlopen('http://localhost:8080/Register?symbol='+symbol+'&feedtype='+feedType) \
                as response1:
            html1: object = response1.read()
            print("Register Symbol Response : " + html1.__str__())
        print('http://localhost:8080/SetOutput?symbol='+symbol +
              '&feedtype='+feedType+'&output='+output+'&status=on')
        with urllib.request.urlopen('http://localhost:8080/SetOutput?symbol='+symbol +
                                    '&feedtype='+feedType+'&output='+output+'&status=on') as response2:
            html2: object = response2.read()
            print("Register Output: "+html2.__str__())

class RegisterImbalance:
    """Registers a single symbol in PPro8 API"""
    def __init__(self):
        print("Rergister Imbalance")
        print('API - Register Imbalance Request  : ' +
              'http://localhost:8080/Register?region=1&feedtype=IMBALANCE&output=bytype')
        with urllib.request.urlopen('http://localhost:8080/Register?region=1&feedtype=IMBALANCE&output=bytype') as response1:
            html1: object = response1.read()
            print("API - Register Imbalance Response : " + html1.__str__())


class RegisterSymbols:
    """Registers a list of symbols in PPro8 API"""
    def __init__(self, symbols, feedType="TOS"):
        print("Register Symbols")
        print(symbols)
        for k, symbol in symbols.items():
            print("")
            print('Register Symbol Request  : http://localhost:8080/Register?symbol='+symbol.__str__()+'&feedtype='+feedType)
            with urllib.request.urlopen('http://localhost:8080/Register?symbol='+symbol.__str__() + '&feedtype='+feedType.__str__()) as response1:
                html1: object = response1.read()
                print("Register Symbol Response : " + html1.__str__())
            with urllib.request.urlopen('http://localhost:8080/SetOutput?symbol='+symbol +
                                        '&feedtype='+feedType+'&output=bytype&status=on') as response2:
                html2: object = response2.read()
                #print("Register Output: "+symbol)


class RegisterDictionarySymbols:
    """Registers a list of symbols in PPro8 API"""
    def __init__(self, symbols={1: {'ticker': 'CRON.TO'}}, feedType="TOS"):
        print("Register Symbols")
        for ticker, symbol in symbols.items():
            #print('Register Symbol Request  : http://localhost:8080/Register?symbol='+symbol+'&feedtype='+feedType)
            with urllib.request.urlopen('http://localhost:8080/Register?symbol='+symbol+'&feedtype='+feedType) as response1:
                html1: object = response1.read()
                #print("Register Symbol Response : " + html1.__str__())
            with urllib.request.urlopen('http://localhost:8080/SetOutput?symbol='+symbol+
                                        '&feedtype='+feedType+'&output=bytype&status=on') as response2:
                html2: object = response2.read()
                #print("Register Output: "+symbol)


class SnapShot:
    """Create Snapshot of Time of Sale in PPro8 API"""
    def __init__(self, symbols=['CRON.TO', 'XO.TO', 'TD.TO'], feedType="TOS"):
        for symbol in symbols:
            print('Snapshot Request  : http://localhost:8080/GetSnapshot?symbol='+symbol+'&feedtype='+feedType)
            with urllib.request.urlopen('http://localhost:8080/GetSnapshot?symbol='+symbol+'&feedtype='+feedType) as response:
                html1: object = response.read()
                print("Snapshot Response: "+html1.__str__())


class TOSFileReader:
    """Create Time of Sale Feed Reader PPro8 API, Reads log file created by the Register Class"""
    def __init__(self):
        file = open("C:\\Program Files (x86)\\Ralota\\PPro8 Ekeko\\TOS_1.log", "r")
        while 1:
            where = file.tell()
            line = file.readline()
            if not line:
                time.sleep(1)
                file.seek(where)
            else:
                print(line)


class registerSP500:
    def __init__(self, symbols={1: {'ticker': 'CRON.TO'}}):
        counter = 1
        symbol = {}
        for counter, symbol in symbols.items():
            print(counter)
            print(symbol)
            RegisterSymbol(symbol.__str__(), "TOS")
            RegisterSymbol(symbol.__str__(), "L1")


class ImbalanceFileReader:
    """Create Time of Sale Feed Reader PPro8 API, Reads log file created by the Register Class"""
    def __init__(self):
        file = open("C:\\Program Files (x86)\\Ralota\\PPro8 Ekeko\\IMBAL_CIRC_1.log", "r")
        while 1:
            where = file.tell()
            line = file.readline()
            if not line:
                time.sleep(1)
                file.seek(where)
            else:
                print(line)


class ClosingImbalanceFile:
    """Read and process the Imbalance File for Parsing into the Imbalance Data Class"""
    def __init__(self):
        print("Reading Closing Imbalance File")
        file = open("C:\\Users\\tctech\\Documents\\Trading Notes\\ClosingImbalance.txt", "r")
        for line in file:
            print(line)
        file.close()

class Imbalance:
    """Data Class Used to store the closing imbalance information in the Imbalance Class using a Dictionary"""


    def __init__(self):
        print("Initialize Imbalance Object")


    @staticmethod
    def loadfile(tradeValue):
        """Load the Imbalance File for Parsing into the imbalancerecord(s) data dictionaries"""
        print("Start Load Imbalance File: "+time.asctime())
        #file = open("C:\\Users\\tctech\\Documents\\Trading Notes\\ClosingImbalance.txt", "r")
        file = open("C:\\Program Files (x86)\\Ralota\\PPro8 Ekeko\\IMBAL_CIRC_1.log", "r")
        recordcount = 1
        imbalancerecords = {}
        for record in file:
            imbalancerecord = {}
            for field in record.split(','):
                fieldName  = field.split('=').__getitem__(0)
                fieldValue = field.split('=').__getitem__(1)
                imbalancerecord[fieldName] = fieldValue
            imbalancerecords[recordcount] = imbalancerecord
            #print(imbalancerecord)
            recordcount = recordcount + 1
        print("Imbalance Load Completed:  "+time.asctime())
        for key, value in imbalancerecords.items():
            if float(imbalancerecords[key]['AuctionPrice']) * float(int(imbalancerecords[key]['Volume'])) > tradeValue:

                print("Symbol : " + imbalancerecords[key]['Symbol'] +
                      ", Market : " + imbalancerecords[key]['Source'] +
                      ", Side : " + imbalancerecords[key]['Side'] +
                      ", Market Time : " + imbalancerecords[key]['MarketTime'] +
                      ", Volume : " + imbalancerecords[key]['Volume'] +
                      ", AuctionPrice : " + imbalancerecords[key]['AuctionPrice'] +
                      ", TradeValue : " + str(int(float(imbalancerecords[key]['AuctionPrice']) * float(int(imbalancerecords[key]['Volume'])))))
        return ""

class TSXClosingImbalance:
    """Data Class Used to store the TSX closing imbalance information in the Imbalance Records Dictionary"""


    def __init__(self):
        print("Initialize Imbalance Object")


    @staticmethod
    def loadfile(tradeValue):
        """Load the Imbalance File for Parsing into the imbalancerecord(s) data dictionaries"""
        print("Start Load Imbalance File: "+time.asctime())
        #file = open("C:\\Users\\tctech\\Documents\\Trading Notes\\ClosingImbalance.txt", "r")
        file = open("C:\\Program Files (x86)\\Ralota\\PPro8 Ekeko\\IMBAL_CIRC_1.log", "r")
        recordcount = 1
        imbalancerecords = {}
        for record in file:
            imbalancerecord = {}
            #print(record.__str__())
            if str(".TO") in record:
                for field in record.split(','):
                    fieldName  = field.split('=').__getitem__(0)
                    fieldValue = field.split('=').__getitem__(1)
                    imbalancerecord[fieldName] = fieldValue
                    imbalancerecords[recordcount] = imbalancerecord
                    #print(imbalancerecord)
                recordcount = recordcount + 1
        print("Imbalance Load Completed:  "+time.asctime())
        for key, value in imbalancerecords.items():
            if float(imbalancerecords[key]['AuctionPrice']) * float(int(imbalancerecords[key]['Volume'])) >= tradeValue:
                if imbalancerecords[key]['Side'] == 'S' and imbalancerecords[key]['Symbol'].endswith(".TO"):
                    print("Symbol : " + imbalancerecords[key]['Symbol'] +
                          ", Market : " + imbalancerecords[key]['Source'] +
                          ", Side : " + imbalancerecords[key]['Side'] +
                          ", Market Time : " + imbalancerecords[key]['MarketTime'] +
                          ", Volume : " + imbalancerecords[key]['Volume'] +
                          ", AuctionPrice : " + imbalancerecords[key]['AuctionPrice'] +
                          ", TradeValue : " + str(int(
                        float(imbalancerecords[key]['AuctionPrice']) * float(int(imbalancerecords[key]['Volume'])))))
                    BuyMarketOrder(imbalancerecords[key]['Symbol'], "100")

                if imbalancerecords[key]['Side'] == 'B' and imbalancerecords[key]['Symbol'].endswith(".TO"):
                    print("Symbol : " + imbalancerecords[key]['Symbol'] +
                          ", Market : " + imbalancerecords[key]['Source'] +
                          ", Side : " + imbalancerecords[key]['Side'] +
                          ", Market Time : " + imbalancerecords[key]['MarketTime'] +
                          ", Volume : " + imbalancerecords[key]['Volume'] +
                          ", AuctionPrice : " + imbalancerecords[key]['AuctionPrice'] +
                          ", TradeValue : " + str(int(
                        float(imbalancerecords[key]['AuctionPrice']) * float(int(imbalancerecords[key]['Volume'])))))
                    SellMarketOrder(imbalancerecords[key]['Symbol'], "100")
        return ""


class SubmitMarketOrder:
    """Submit Order based on the symbol"""
    def __init__(self, symbol="CRON.TO", side="Buy", shares="100"):
        print("Submitting 100 Share order for Symbol")
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=' + symbol +
                                    '&ordername=TSX%20' + side + '%20SweepSOR%20Market%20DAY' +
                                    '&shares=' + shares) as response1:
            html1: object = response1.read()
            print("Submit Order Response : " + html1.__str__())


class SellMarketOrder:
    """Submit Order based on the symbol"""
    def __init__(self, symbol="CRON.TO", shares="100"):
        print("Sell " + shares + " Shares Market:" + symbol)
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=' + symbol +
                                    '&ordername=TSX%20Sell->Short%20SweepSOR%20Market%20DAY' +
                                    '&shares=' + shares) as response1:
            html1: object = response1.read()
            print("API - Execute Order Response : " + html1.__str__())


class BuyMarketOrder:
    """Submit Order based on the symbol"""
    def __init__(self, symbol="CRON.TO", shares="100"):
        print("Buy " + shares + " Shares Market: " + symbol)
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=' + symbol +
                                    '&ordername=TSX%20Buy%20SweepSOR%20Market%20DAY' +
                                    '&shares=' + shares) as response1:
            html1: object = response1.read()
            print("API - Execute Order Response : " + html1.__str__())


class SellFutures:
    """Submit Futures Contract to sell based on the symbol and contract size, default is ES|M19.CM 1 Contract"""
    def __init__(self, symbol="ES\M19.CM", shares="1"):
        print("Sell " + shares + " Contract Market:" + symbol)
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=' + symbol +
                                    '&ordername=CME%20Sell%20CME%20Market%20DAY' +
                                    '&share=' + shares) as response1:
            html1: object = response1.read()
            print("API - Execute Order Response : " + html1.__str__())


class BuyFutures:
    """Submit Futures Contract to buy based on the symbol and contract size, default is ES|M19.CM 1 Contract"""
    def __init__(self, symbol="ES\M19.CM", shares="1"):
        print("Sell " + shares + " Contract Market:" + symbol)
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=' + symbol +
                                    '&ordername=CME%20Buy%20CME%20Market%20DAY' +
                                    '&share=' + shares) as response1:
            html1: object = response1.read()
            print("API - Execute Order Response : " + html1.__str__())


class LoadSymbols():
    """Load the Symbol File into the symbols data dictionaries"""
    get = Symbols()

    def __init__(self, file=os.getcwd().__str__() + '\\data\\SP_500.csv'):
        print("Start Load File: " + time.asctime())
        print("Current Working Directory: " + file)
        # file = open("C:\\Users\\tctech\\Documents\\Trading Notes\\ClosingImbalance.txt", "r")
        file = open(file, "r")
        recordcount = 1
        sym = {}
        symbols = Symbols()
        for symbol in file:
            symbolrecord = {}
            symbolrecord[recordcount] = symbol.rstrip()
            sym[recordcount] = symbolrecord
            symbols.setsymbols(recordcount, symbol.rstrip())
            recordcount += 1
        print(symbols.getsymbols())
        get = symbols.symbols


class loadCSVinDictionary():
    """Load CSV record into data dictionaries"""
    def __init__(self, record="field1=a, field2=b", **obj):
        for field in record.split(","):
            obj[field.split("=").__getitem__(0)] = field.split("=").__getitem__(1)


class levelone():
    """L1 Object"""
    level_1 = {}

    def __init__(self):
        print("L1 Object Initialized")

    def setL1(self, record, level1):
        self.level_1[record] = level1

    def getL1(self):
        return print(self.level_1.__str__())


class Symbols:
    symbols = {}

    def _init__(self):
        print("Hello")

    def setsymbols(self, record, sym):
        self.symbols[record] = sym

    def getsymbols(self):
        return print(self.symbols.__str__())

class ppro_datagram(DatagramProtocol):
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
        # now you can call specific data by name in the line you're processing instead of counting colums
        # See the print statement below for examples

        print('{} {} {}'.format(message_dict['Symbol'], message_dict['Message'], msg))

        # but any named column will not be callable:
        # message_dict['MarketTime']
        # message_dict['Price']

    def connectionRefused(self):
        print("No one listening")


#ACB_TOS = RegisterSymbol("ACB.TO", "TOS")
#ACB_L1  = RegisterSymbol("ACB.TO", "L1")
#GS_L1   = RegisterSymbol("GS.TO", "L1")
#GS_L2   = RegisterSymbol("GS.TO", "L2")
#GS_L2_UDP = RegisterSymbol("GS.TO", "L2", "5555")
#GS_TOS  = RegisterSymbol("GS.TO", "TOS")
#test2 = SnapShot(["TD.TO", "X.TO", "ACB.TO","CRON.TO"], "IMBALANCE")
#test3 = TOSFileReader()
#test4 = ClosingImbalanceFile()
#testBuy  = BuyMarketOrder("ES\M19.CM", "1")
#test6Sell = SellMarketOrder("ACB.TO", 100)
#test7 = RegisterImbalance()
#test8 = ImbalanceFileReader()
#test5 = Imbalance().loadfile(200000000.00)
test9 = TSXClosingImbalance.loadfile(10000000.00)
#test10 = BuyFutures()
#test11 = registerSP500()
#x = LoadSymbols()
#print(x.get.symbols)
#test13 = registerSP500(x.get.symbols)
#test12.listSymbols()
#test1 = RegisterSymbols(x.get.symbols, "TOS")
#BuyMarketOrder("CRON.TO", "100")
#SellMarketOrder("ACB.TO", "100")
#test = SubmitMarketOrder("ACB.TO", "Buy", "100")
#test = BuyMarketOrder("ACB.TO", "100")
#test = SellMarketOrder("ACB.TO", "100")
#L1=RegisterSymbol("ACB.TO", "L1", "5555")
#reactor.listenUDP(5555, ppro_datagram())
#reactor.run()