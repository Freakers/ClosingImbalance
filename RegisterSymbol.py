import urllib.request
import urllib.response
import time


class RegisterSymbol():
    """Registers a single symbol in PPro8 API"""
    def __init__(self, symbol="CRON.TO", feedType="TOS"):
        #print("Rergister Symbol")
        #print('Register Symbol Request  : http://localhost:8080/Register?symbol='+symbol+'&feedtype='+feedType)
        with urllib.request.urlopen('http://localhost:8080/Register?symbol='+symbol+'&feedtype='+feedType) as response1:
            html1: object = response1.read()
            #print("Register Symbol Response : " + html1.__str__())


class RegisterImbalance():
    """Registers a single symbol in PPro8 API"""
    def __init__(self):
        #print("Rergister Symbol")
        #print('Register Symbol Request  : http://localhost:8080/Register?symbol='+symbol+'&feedtype='+feedType)
        with urllib.request.urlopen('http://localhost:8080/Register?region=1&feedtype=IMBALANCE&output=bytype') as response1:
            html1: object = response1.read()
            #print("Register Symbol Response : " + html1.__str__())


class RegisterSymbols:
    """Registers a list of symbols in PPro8 API"""
    def __init__(self, symbols=['CRON.TO', 'XO.TO', 'TD.TO'], feedType="TOS"):
        print("Register Symbols")
        for symbol in symbols:
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
        file = open("C:\\Users\\tctech\\Documents\\Trading Notes\\ClosingImbalance.txt", "r")
        #file = open("C:\\Program Files (x86)\\Ralota\\PPro8 Ekeko\\IMBAL_CIRC_1.log", "r")
        recordcount = 1
        imbalancerecords = {}
        for record in file:
            imbalancerecord = {}
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
                    BuyMarketOrder(imbalancerecords[key]['Symbol'], 100)

                if imbalancerecords[key]['Side'] == 'B' and imbalancerecords[key]['Symbol'].endswith(".TO"):
                    print("Symbol : " + imbalancerecords[key]['Symbol'] +
                          ", Market : " + imbalancerecords[key]['Source'] +
                          ", Side : " + imbalancerecords[key]['Side'] +
                          ", Market Time : " + imbalancerecords[key]['MarketTime'] +
                          ", Volume : " + imbalancerecords[key]['Volume'] +
                          ", AuctionPrice : " + imbalancerecords[key]['AuctionPrice'] +
                          ", TradeValue : " + str(int(
                        float(imbalancerecords[key]['AuctionPrice']) * float(int(imbalancerecords[key]['Volume'])))))
                    SellMarketOrder(imbalancerecords[key]['Symbol'], 100)
        return ""


class SubmitMarketOrder:
    """Submit Order based on the symbol"""
    def __init__(self, symbol="CRON.TO", shares="100"):
        print("Submitting 100 Share order for Symbol")
        print('Submit Order Request  : http://localhost:8080/ExecuteOrder?symbol='+symbol +
              '&ordername=TSX%20Buy%20SweepSOR%20Market%20DAY' +
              '&shares='+strshares)
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=ACB.TO' +
                                    '&ordername=TSX%20Buy%20SweepSOR%20Market%20DAY' +
                                    '&shares=100') as response1:
            html1: object = response1.read()
            print("Submit Order Response : " + html1.__str__())


class SellMarketOrder:
    """Submit Order based on the symbol"""
    def __init__(self, symbol="CRON.TO", shares="100"):
        print("Sell 100 Shares Market:" + symbol)
        print('API - Execute Order Request  : http://localhost:8080/ExecuteOrder?symbol='+symbol+'&limitprice=10.00&ordername=TSX%20Buy%20SweepSOR%20Market%20DAY%20Reserve&shares=1000&displaysize=100')
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=ACB.TO' +
                                    '&ordername=TSX%20Sell->Short%20SweepSOR%20Market%20DAY' +
                                    '&shares=100') as response1:
            html1: object = response1.read()
            print("API - Execute Order Response : " + html1.__str__())


class BuyMarketOrder:
    """Submit Order based on the symbol"""
    def __init__(self, symbol="CRON.TO", shares="100"):
        print("Buy 100 Shares Market: " + symbol)
        with urllib.request.urlopen('http://localhost:8080/ExecuteOrder?symbol=ACB.TO' +
                                    '&ordername=TSX%20Buy%20SweepSOR%20Market%20DAY' +
                                    '&shares=100') as response1:
            html1: object = response1.read()
            print("API - Execute Order Response : " + html1.__str__())

#test1 = RegisterSymbols(["TD.TO", "X.TO", "ACB.TO","CRON.TO"], "TOS")
#test2 = SnapShot(["TD.TO", "X.TO", "ACB.TO","CRON.TO"], "IMBALANCE")
#test3 = TOSFileReader()
#test4 = ClosingImbalanceFile()
#testBuy  = BuyMarketOrder("ACB.TO", 100)
#test6Sell = SellMarketOrder("ACB.TO", 100)
#test7 = RegisterImbalance()
#test8 = ImbalanceFileReader()
#test5 = Imbalance().loadfile(200000000.00)
test9 = TSXClosingImbalance.loadfile(20000000.00)

