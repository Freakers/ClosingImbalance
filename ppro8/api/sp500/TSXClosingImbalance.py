import urllib.request
import urllib.response
import time
import os
import threading
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
import pause
import shutil
from datetime import datetime

class Symbols:
    symbols = {}

    def _init__(self):
        print("Hello")

    def setsymbols(self, record, sym):
        self.symbols[record] = sym

    def getsymbols(self):
        return print(self.symbols.__str__())


class mocsymbols:

    def __init__(self, mocsym):
        self.symbols = {}
        self.loadmocsymbols(mocsym)
        print(self.symbols.__len__())
        # self.listsymbols()
        # self.deregistersymbol()
        self.registersymbols()

    def setsymbols(self, record, sym):
        self.symbols[record] = sym

    def getsymbols(self):
        return self.symbols

    def registersymbols(self):
        print("Starting THREADS to register TOS for MOC Symbol List")
        for record, symbol in self.symbols.items():
            #print(symbol)
            t = threading.Thread(target=self.registersymbol, args=(symbol, "TOS", "bytype",))
            t.start()

    def deregistersymbols(self):
        print("Starting THREADS to deregister TOS for MOC Symbol List")
        for record, symbol in self.symbols.items():
            #print(symbol)
            t = threading.Thread(target=self.deregistersymbol, args=(symbol, "TOS", "1",))
            t.start()

    def registersymbol(self, symbol, feedType, output):
        #print('Register Symbol Request  : http://localhost:8080/Register?symbol=' + symbol + '&feedtype=' + feedType)
        with urllib.request.urlopen('http://localhost:8080/Register?symbol=' + symbol + '&feedtype=' + feedType) \
                as response1:
            html1: object = response1.read()
            #print("Register Symbol Response : " + html1.__str__())
        #print('http://localhost:8080/SetOutput?symbol=' + symbol + '&feedtype=' + feedType + '&output=' + output + '&status=on')
        with urllib.request.urlopen('http://localhost:8080/SetOutput?symbol=' + symbol +
                                    '&feedtype=' + feedType + '&output=' + output + '&status=on') as response2:
            html2: object = response2.read()
            #print("Register Output: " + html2.__str__())

    def deregistersymbol(self, symbol, feedType, region, output):
        print('Deregister Symbol Request  : http://localhost:8080/Deregister?symbol=' + symbol + '&region=' +
              region + '&feedtype=' + feedType)
        with urllib.request.urlopen('http://localhost:8080/SetOutput?symbol=' + symbol +
                                    '&feedtype=' + feedType + '&output=' + output + '&status=off') as response0:
            html0: object = response0.read()
            #print("Deregister Symbol Response : " + html0.__str__())
        with urllib.request.urlopen('http://localhost:8080/Deregister?symbol=' + symbol + '&region=' + region +
                                    '&feedtype=' + feedType) as response1:
            html1: object = response1.read()
            #print("Deregister Symbol Response : " + html1.__str__())

    def loadmocsymbols(self, mocsymbols):
        for key, symbol in mocsymbols.items():
            self.symbols[key] = symbol.rstrip()


class RegisterSymbol:
    """Registers a single symbol in PPro8 API"""
    def __init__(self, symbol="CRON.TO", feedType="TOS", output="btype"):
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
    def __init__(self, feedType="TOS", **symbols):
        for k, symbol in symbols:
            print('Snapshot Request  : http://localhost:8080/GetSnapshot?symbol='+symbol+'&feedtype='+feedType)


            with threading.Thread(target=urllib.request.urlopen, args=('http://localhost:8080/GetSnapshot?symbol='+symbol+'&feedtype='+feedType, )) as response:
            #with urllib.request.urlopen('http://localhost:8080/GetSnapshot?symbol='+symbol+'&feedtype='+feedType) as response:
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
            RegisterSymbol(symbol, "TOS")
            RegisterSymbol(symbol, "L1")


class ImbalanceFileReader:
    """Create Time of Sale Feed Reader PPro8 API, Reads log file created by the Register Class"""

    def __init__(self):
        n = datetime.now()
        l1_tos_stats = {}
        l1_tos_symbol = {}
        l1_symbols = {}
        rec_count = 1
        n = datetime.now()
        file = open("C:\\logs\\" + n.date().__str__() + "\\IMBAL_CIRC_1.log", "r")
        for record in file:
            if ".TO" in record:
                #print(record)
                fields = record.split(",")
                l1_symbols[rec_count] = fields[6].split("=").pop(1) + ";" + \
                                        fields[3].split("=").pop(1) + ";" + fields[8].split("=").pop(1) + ";" + \
                                        fields[10].split("=").pop(1) + ";" + \
                                        str(float(fields[8].split("=").pop(1))*float(fields[10].split("=").pop(1)))
                rec_count = rec_count + 1
                #print(rec_count)
        tos = TOSFileReader()
        file = open("C:\\logs\\" + n.date().__str__() + "\\MOCImbalance.csv", "w")
        masterfile = open("C:\\logs\\master\\MOCImbalance.csv", "a")
        file.write("Date;Symbol;Side;Shares;Price;Trade Value;Close Price; Net Share Profit\n")
        for key, l1_symbols in l1_symbols.items():
            fields = l1_symbols.split(";")
            side = fields[1]
            moc_price = float(fields[3])
            ltp = tos.get_last_trade(l1_symbols.split(";").pop(0)).__str__()
            if "None" not in ltp:
                if side == "B":
                    last_trade_price = float(tos.get_last_trade(l1_symbols.split(";").pop(0)).__str__())
                    performance = str(last_trade_price - moc_price)
                    file.write(n.date().__str__() + ";" + l1_symbols.__str__() + ";" +
                               tos.get_last_trade(l1_symbols.split(";").pop(0)).__str__() + ";" + performance + "\n")
                    masterfile.write(n.date().__str__() + ";" + l1_symbols.__str__() + ";" +
                               tos.get_last_trade(l1_symbols.split(";").pop(0)).__str__() + ";" + performance + "\n")
                else:
                    if side == "S":
                        last_trade_price = float(tos.get_last_trade(l1_symbols.split(";").pop(0)).__str__())
                        performance = str(moc_price - last_trade_price)
                        file.write(n.date().__str__() + ";" + l1_symbols.__str__() + ";" +
                                   tos.get_last_trade(l1_symbols.split(";").pop(0)).__str__() + ";" + performance + "\n")
                        masterfile.write(n.date().__str__() + ";" + l1_symbols.__str__() + ";" +
                                         tos.get_last_trade(l1_symbols.split(";").pop(0)).__str__() + ";" + performance + "\n")
                    else:
                        file.write(n.date().__str__() + ";" + l1_symbols.__str__() + ";" +
                                   tos.get_last_trade(l1_symbols.split(";").pop(0)).__str__() + ";" + "00.00" + "\n")
                        masterfile.write(n.date().__str__() + ";" + l1_symbols.__str__() + ";" +
                                         tos.get_last_trade(l1_symbols.split(";").pop(0)).__str__() + ";" + performance + "\n")

class TOSFileReader:
    """Create Time of Sale File Reader, Reads log file created by the Register Class"""

    def __init__(self):
        self.tos_records = {}
        self.last_trade_record = {}
        self.tos_records_closing = {}
        rec_count = 1
        n = datetime.now()
        file = open("C:\\logs\\" + n.date().__str__() + "\\TOS_1.log", "r")
        for record in file:
            if ".TO" in record:
                #print(record)
                self.tos_records[rec_count] = record
                rec_count = rec_count + 1
                #self.get_last_trade(symbol)

    def get_last_trade(self, symbol="CNE.TO"):
        symbol = "Symbol="+symbol
        message_dict = {}
        for key, tos_record in self.tos_records.items():
            if symbol in tos_record:
                n = datetime.now()
                #print(n.year.__str__() + n.month.__str__() + n.day.__str__())
                for item in tos_record.split(','):
                    couple = item.split('=')
                    message_dict[couple[0]] = couple[1]
                    trdtime  = message_dict.get('MarketTime')
                    mtime = str(trdtime).split(":")
                if datetime(n.year, n.month, n.day, int(mtime[0]), int(mtime[1]),
                            int(mtime[2].split('.').pop(0)), 0).time() \
                        >= datetime(n.year, n.month, n.day, 16, 00, 00, 0).time():
                    #print("Last Trade Matched: "+tos_record)
                    self.last_trade_record[key] = tos_record
                    toslastprice = tos_record.split(",").pop(5).split("=").pop(1)
                    return toslastprice
                    break

    def match_last_trades_to_moc_records(self, symbol):
        for k, v in self.last_trade_record.items():
            if symbol in v:
                return self.last_trade_record[k]

class ClosingImbalanceFile:
    """Read and process the Imbalance File for Parsing into the Imbalance Data Class"""
    def __init__(self):
        print("Reading Closing Imbalance File")
        file = open("C:\\Users\\tctech\\Documents\\Trading Notes\\ClosingImbalance.txt", "r")
        for line in file:
            print(line)
        file.close()


class TSXClosingImbalance:
    """Data Class Used to store the TSX closing imbalance information in the Imbalance Records Dictionary"""
    mrec = {}

    def __init__(self):
        print("Initialize Imbalance Object")


    def loadfile(tradeValue, market):
        moc_records = {}
        moc_dict = {}
        symbols = {}
        """Load the Imbalance File for Parsing into the imbalancerecord(s) data dictionaries"""
        print("Start Load Imbalance File: "+time.asctime())
        file = open("C:\\Program Files (x86)\\Ralota\\PPro8 Haya\\IMBAL_CIRC_1.log", "r")
        recordcount = 1
        imbalancerecords = {}
        for record in file:
            imbalancerecord = {}
            #print(record.__str__())
            if str(market) in record:
                for field in record.split(','):
                    fieldName  = field.split('=').__getitem__(0)
                    fieldValue = field.split('=').__getitem__(1)
                    imbalancerecord[fieldName] = fieldValue
                    imbalancerecords[recordcount] = imbalancerecord
                    # Store all symbols into symbols dictionary
                    if fieldName == 'Symbol':
                        symbols[recordcount] = fieldValue
                        #print(imbalancerecord)
                recordcount = recordcount + 1
        print("Imbalance Load Completed:  "+time.asctime())
        recordcount = 1
        for key, value in imbalancerecords.items():
            #print("Auction Price: " + imbalancerecords[key]['AuctionPrice'])
            #print("Volume        : "+ imbalancerecords[key]['Volume'])
            if float(imbalancerecords[key]['AuctionPrice']) * float(int(imbalancerecords[key]['Volume'])) >= tradeValue:
                if imbalancerecords[key]['Side'] == 'S' and imbalancerecords[key]['Symbol'].endswith(market):
                    print("Market Time: " + imbalancerecords[key]['MarketTime'] +
                          "\tSymbol: " + imbalancerecords[key]['Symbol'].ljust(10) +
                          "\tMarket: " + imbalancerecords[key]['Source'] +
                          "\tSide: " + imbalancerecords[key]['Side'].ljust(4) +
                          "\tVolume: " + imbalancerecords[key]['Volume'].ljust(9) +
                          "\tAuctionPrice: " + imbalancerecords[key]['AuctionPrice'] +
                          "\tTradeValue: " + format(float(imbalancerecords[key]['AuctionPrice']) * float(int(imbalancerecords[key]['Volume'])), ',.2f'))
                    moc_dict['MarketTime'] = imbalancerecords[key]['MarketTime']
                    moc_dict['Symbol'] = imbalancerecords[key]['Symbol']
                    moc_dict['Side'] = imbalancerecords[key]['Side']
                    moc_dict['Volume'] = imbalancerecords[key]['Volume']
                    moc_dict['AuctionPrice'] = imbalancerecords[key]['AuctionPrice']
                    moc_dict['ClosingPrice'] = "00.00"
                    moc_records[recordcount] = moc_dict
                    recordcount = recordcount + 1
                    #BuyMarketOrder(imbalancerecords[key]['Symbol'], "100")

                if imbalancerecords[key]['Side'] == 'B' and imbalancerecords[key]['Symbol'].endswith(market):
                    print("Market Time: " + imbalancerecords[key]['MarketTime'] +
                          "\tSymbol: " + imbalancerecords[key]['Symbol'].ljust(10) +
                          "\tMarket: " + imbalancerecords[key]['Source'] +
                          "\tSide: " + imbalancerecords[key]['Side'].ljust(4) +
                          "\tVolume: " + imbalancerecords[key]['Volume'].ljust(9) +
                          "\tAuctionPrice: " + imbalancerecords[key]['AuctionPrice'] +
                          "\tTradeValue: " + format(float(imbalancerecords[key]['AuctionPrice']) * float(int(imbalancerecords[key]['Volume'])), ',.2f'))
                    moc_dict['MarketTime'] = imbalancerecords[key]['MarketTime']
                    moc_dict['Symbol'] = imbalancerecords[key]['Symbol']
                    moc_dict['Side'] = imbalancerecords[key]['Side']
                    moc_dict['Volume'] = imbalancerecords[key]['Volume']
                    moc_dict['AuctionPrice'] = imbalancerecords[key]['AuctionPrice']
                    moc_dict['ClosingPrice'] = "00.00"
                    moc_records[recordcount] = moc_dict
                    recordcount = recordcount + 1
                    #SellMarketOrder(imbalancerecords[key]['Symbol'], "100")
        # Load Moc Symbols and Register Time of Sale for each imbalance record
        m = mocsymbols(symbols)
        n = datetime.now()
        while datetime(n.year, n.month, n.day,n.hour, n.minute, n.second).time() \
                <= datetime(n.year, n.month, n.day, 16, 12, 00).time():
            SnapShot(m.getsymbols())
            time.sleep(15)
            n = datetime.now()
        print("Collecting TOS Snapshot at " + datetime(n.year, n.month, n.day,n.hour, n.minute, n.second).time().__str__())
        if not os.path.exists("C:\\logs\\" + n.date().__str__()):
            os.makedirs("C:\\logs\\" + n.date().__str__())
        shutil.copy("C:\\Program Files (x86)\\Ralota\\PPro8 Haya\\IMBAL_CIRC_1.log", "C:\\logs\\" + n.date().__str__())
        shutil.copy("C:\\Program Files (x86)\\Ralota\\PPro8 Haya\\TOS_1.log", "C:\\logs\\" + n.date().__str__())


class SubmitMarketOrder:
    """Submit Order based on the symbol"""
    def __init__(self, symbol="CRON.TO", side="Buy", shares="100"):
        print("Submitting 100 Share order for Symbol")
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=' + symbol +
                                    '&ordername=TSX%20' + side + '%20SweepSOR%20Market%20ANON%20DAY' +
                                    '&shares=' + shares) as response1:
            html1: object = response1.read()
            print("Submit Order Response : " + html1.__str__())


class SellMarketOrder:
    """Submit Order based on the symbol"""
    def __init__(self, symbol="CRON.TO", shares="100"):
        print("Sell " + shares + " Shares Market:" + symbol)
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=' + symbol +
                                    '&ordername=TSX%20Sell->Short%20SweepSOR%20Market%20ANON%20DAY' +
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


class LoadSymbols:
    """Load the Symbol File into the symbols data dictionaries"""

    def __init__(self, file=os.getcwd().__str__() + '\\symbols.csv'):
        print("Start Load File: " + time.asctime())
        print("Current Working Directory: " + file)
        # file = open("C:\\Users\\tctech\\Documents\\Trading Notes\\ClosingImbalance.txt", "r")
        file = open(file, "r")
        recordcount = 1
        sym = {}
        self.symbols = Symbols()
        for symbol in file:
            symbolrecord = {}
            symbolrecord[recordcount] = symbol.rstrip()
            sym[recordcount] = symbolrecord
            self.symbols.setsymbols(recordcount, symbol.rstrip())
            recordcount += 1

    def getSP500StockList(self):
        return self.symbols

    def getsymbols(self):
        return self.symbols


class loadCSVinDictionary():
    """Load CSV record into data dictionaries"""
    def __init__(self, record="field1=a, field2=b", **obj):
        for field in record.split(","):
            obj[field.split("=").__getitem__(0)] = field.split("=").__getitem__(1)


class LevelOne:
    """L1 Object"""
    level_1 = {}

    def __init__(self):
        print("L1 Object Initialized")

    def setL1(self, record, level1):
        self.level_1[record] = level1

    def getL1(self):
        return print(self.level_1.__str__())


class ppro_datagram(DatagramProtocol):

    def __init__(self):
        self.bidpr = 0
        self.askpr = 0
        self.asks = 0
        self.bids = 0

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

        # print('{} {} {}'.format(message_dict['Symbol'], message_dict['Message'], msg))
        if message_dict['Message'] == "L1":
            bidpr = float(message_dict['BidPrice'])
            askpr = float(message_dict['AskPrice'])
            bids = 0
            asks = 0
            print("L1 Time  :\\t" + message_dict['MarketTime'] + "\\tSymbol: " + message_dict['Symbol'])
            print("Bid Price:\\t" + message_dict['BidPrice'] + "\\tBid Size: " + message_dict['BidSize'])
            print("Ask Price:\\t" + message_dict['AskPrice'] + "\\tAsk Size: " + message_dict['AskSize'])
            x = 1
        if message_dict['Message'] == "TOS":
            print("TOS Time: " + message_dict['MarketTime'] + " Price: " + message_dict['Price'] +
                  " Size: " + message_dict['Size'])
            if float(message_dict['Price']) >= askpr:
                asks = asks + 1
            if float(message_dict['Price']) <= bidpr:
                bids = bids + 1
        print("Bids = " + bids.__str__() + " Asks = " + asks.__str__())
        # but any named column will not be callable:
        # message_dict['MarketTime'] " + message_dict['Symbol'])
        #             print("     Bid Price: " + message_dict['BidPrice'] + " Bid Size: " + message_dict['BidSize'])
        #             print("     Ask Price: " + message_dict['AskPrice'] + " Ask Size: " + message_dict['AskSize'])
        # message_dict['Price']

    def connectionRefused(self):
        print("No one listening")

# Unit Test - Register symbol ACB.TO for Time of Sale to the default TOS file
#   bytype = defaults to file in PPro8
#   9999 = defaults to a UDP port
#ACB_TOS = RegisterSymbol("_STW.E1", "TOS", "bytype")

# Unit Test - Register symbol ACB.TO for Level 1 quotes and write the L1 data to the default L1 file
#   bytype = defaults to file in PPro8
#   9999 = defaults to a UDP port
# #ACB_L1  = RegisterSymbol("ACB.TO", "L1", "bytype")

# Unit Test - Register symbol GS.TO for Level 2 quotes and write the L2 data to the default L2 file
#   bytype = defaults to file in PPro8
#   9999 = defaults to a UDP port
#GS_L2   = RegisterSymbol("GS.TO", "L2", "bytype")

# Unit Test - Register symbol GS.TO for Level 2 quotes and write the L2 data to the default L2 file
# bytype = defaults to file in PPro8
# 9999 = defaults to a UDP port
#GS_L2_UDP = RegisterSymbol("GS.TO", "L2", "5555")

# Unit Test - Register symbol GS.TO for Level 2 quotes and write the L2 data to the default L2 file
#GS_TOS  = RegisterSymbol("GS.TO", "TOS")

# Unit Test - Perform snapshot of imbalance
#test2 = SnapShot()

# Unit Test - Test Reading the TOS feed
#test3 = TOSFileReader()

# Unit Test - Utility that reads TSX closing imbalance
#test4 = ClosingImbalanceFile()

# Unit Test - Submit Buy Market Order by symbol and shares
#testBuy  = BuyMarketOrder("ES\M19.CM", "1")

# Unit Test - Submit Sell Market Order by symbol and shares
#test6Sell = SellMarketOrder("ACB.TO", 100)

# Unit Test - Imbalance File Reader
#test8 = ImbalanceFileReader()
#test81 = TOSFileReader()

# Unit Test -  Load Imbalance file and report all trade imbalance numbers over trade threshold
#test5 = Imbalance().loadfile(50000000.00)

# Unit Test - Submit Buy futures order by symbol and shares
#test10 = BuyFutures()

#test11 = registerSP500()

# x = LoadSymbols()
# y = x.getsymbols()
#test2 = SnapShot("_STW60.E1")

#print("Print : "+x.getSP500StockList())

#test13 = registerSP500(x.get.symbols)

#test12.listSymbols()

#test1 = RegisterSymbols(x.get.symbols, "TOS")

#BuyMarketOrder("CRON.TO", "100")

#SellMarketOrder("ACB.TO", "100")

#test = SubmitMarketOrder("WEED.TO", "Buy", "100")

#test = BuyMarketOrder("ACB.TO", "100")

#test = SellMarketOrder("ACB.TO", "100")

#L1=RegisterSymbol("CRON.TO", "L1", "5555")

#TOS = RegisterSymbol("_STW60.E1", "TOS", "5555")

#reactor.listenUDP(5555, ppro_datagram())

#reactor.run()


#
# TSXClosingImbalance
# Process Flow
# Step 1. Wait until 13:35:00 PM and then register MOC Imbalance for North American Region Region=1
#     pause.until(datetime(n.year, n.month, n.day, 13, 35, 0, 0))
#     step1 = RegisterImbalance()
# Step 2. Wait until 13:40:00 PM (TSX MOC Imbalance Reporting) and generate list of stocks that equal or exceeed a trade value of 10 million or more
#     pause.until(datetime(n.year, n.month, n.day, 13, 40, 0, 0))
#     step2 = TSXClosingImbalance.loadfile(10000000.00, ".TO")
# NOTE: Step 3 is inside of the class TSXClosingImbalance
#       Step 3. Then register all MOC eligible symbols for TOS (time of sale) data and capture the until 4:12 PM
# Step 4. Once the market has closed take all moc records and find the corresponding Last Trade Price in the TOS files
# Create data folder and store MOC report and all data
n = datetime.now()
print(n.year.__str__()+n.month.__str__()+n.day.__str__())
pause.until(datetime(n.year, n.month, n.day, 15, 35, 0, 0))
step1 = RegisterImbalance()
pause.until(datetime(n.year, n.month, n.day, 15, 40, 0, 0))
step2 = TSXClosingImbalance.loadfile(10000000.00, ".TO")
step3 = ImbalanceFileReader()

