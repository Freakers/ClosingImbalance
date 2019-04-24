"# ClosingImbalance" 

This file contains the folllowing PYTHON classes used to demonstrate the PPro8 API

  *class Symbols:
  *class RegisterSymbol:
  class RegisterImbalance:
  class RegisterSymbols:
  class RegisterDictionarySymbols:
  class SnapShot:
  class TOSFileReader:
  class registerSP500:
  class ImbalanceFileReader:
  class ClosingImbalanceFile:
  class Imbalance:
  class TSXClosingImbalance:
  class SubmitMarketOrder:
  class SellMarketOrder:
  class BuyMarketOrder:
  class SellFutures:
  class BuyFutures:
  class LoadSymbols():
  class loadCSVinDictionary():
  class levelone():
  class Symbols:
  class ppro_datagram(DatagramProtocol):

This file contains the folllowing PYTHON unit tests used to demonstrate the above classes

This file contains the folllowing PYTHON classes used to demonstrate the PPro8 API

  ACB_TOS = RegisterSymbol("ACB.TO", "TOS")
  ACB_L1  = RegisterSymbol("ACB.TO", "L1")
  GS_L1   = RegisterSymbol("GS.TO", "L1")
  GS_L2   = RegisterSymbol("GS.TO", "L2")
  GS_L2_UDP = RegisterSymbol("GS.TO", "L2", "5555")
  GS_TOS  = RegisterSymbol("GS.TO", "TOS")
  test2 = SnapShot(["TD.TO", "X.TO", "ACB.TO","CRON.TO"], "IMBALANCE")
  test3 = TOSFileReader()
  test4 = ClosingImbalanceFile()
  testBuy  = BuyMarketOrder("ES\M19.CM", "1")
  test6Sell = SellMarketOrder("ACB.TO", 100)
  test7 = RegisterImbalance()
  test8 = ImbalanceFileReader()
  test5 = Imbalance().loadfile(200000000.00)
  test9 = TSXClosingImbalance.loadfile(10000000.00, ".TO")
  test10 = BuyFutures()
  test11 = registerSP500()
  x = LoadSymbols()
  print(x.get.symbols)
  test13 = registerSP500(x.get.symbols)
  test12.listSymbols()
  test1 = RegisterSymbols(x.get.symbols, "TOS")
  BuyMarketOrder("CRON.TO", "100")
  SellMarketOrder("ACB.TO", "100")
  test = SubmitMarketOrder("WEED.TO", "Buy", "100")
  test = BuyMarketOrder("ACB.TO", "100")
  test = SellMarketOrder("ACB.TO", "100")
  L1=RegisterSymbol("ACB.TO", "L1", "5555")

  reactor.listenUDP(5555, ppro_datagram())
  reactor.run()

It also contains a \data folder containing various Exchange Symbol Lists traded at DTTW

  Amsterdam.csv
  Bovespa.csv
  Brussels.csv
  CBOE-BITCOIN.csv
  CBOE-VIX.csv
  CBOE.csv
  Copenhagen.csv
  CSE.csv
  Dublin.csv
  ETF.csv
  Helsinki.csv
  Johannesburg.csv
  Lisbon.csv
  London.csv
  Madrid.csv
  Milan.csv
  Moscow.csv
  NASDAQ.csv
  NYMEX-E-miniCrudeOil.csv
  NYMEX-Gasoline.csv
  NYMEX-Light SweetCrudeOil.csv
  NYMEX-NaturalGas.csv
  NYMEX-NYHarborULSD.csv
  NYMEX.csv
  NYSE-AMEX.csv
  NYSE.csv
  Oslo.csv
  OTC-Pink.csv
  Paris.csv
  SP_500.csv
  Stockholm.csv
  Switzerland.csv
  Turkey.csv
  Vienna.csv
  Warsaw.csv
  Xetra.csv



