"# ClosingImbalance" 

This file contains the folllowing PYTHON classes used to demonstrate the PPro8 API
<li>
  class Symbols:
</li>
<li>  
  class RegisterSymbol:
</li>
<li>  
  class RegisterImbalance:
</li>
<li>  
  class RegisterSymbols:
</li>
<li>  
  class RegisterDictionarySymbols:
</li>
<li>  
  class SnapShot:
</li>
<li>  
  class TOSFileReader:
</li>
<li>  
  class registerSP500:
</li>
<li>  
  class ImbalanceFileReader:
</li>
<li>  
  class ClosingImbalanceFile:
</li>
<li>  
  class Imbalance:
</li>
<li>  
  class TSXClosingImbalance:
</li>
<li>  
  class SubmitMarketOrder:
</li>
<li>  
  class SellMarketOrder:
</li>
<li>  
  class BuyMarketOrder:
</li>
<li>  
  class SellFutures:
</li>
<li>  
  class BuyFutures:
</li>
<li>  
  class LoadSymbols():
</li>
<li>  
  class loadCSVinDictionary():
</li>
<li>  
  class levelone():
</li>
<li>  
  class Symbols:
</li>
<li>  
  class ppro_datagram(DatagramProtocol):
</li>

<p>This file contains the folllowing PYTHON unit tests used to demonstrate the above classes</p>

<p>This file contains the folllowing PYTHON classes used to demonstrate the PPro8 API</p>

<li>  
  ACB_TOS = RegisterSymbol("ACB.TO", "TOS")
</li>
<li>  
  ACB_L1  = RegisterSymbol("ACB.TO", "L1")
</li>
<li>  
  GS_L2   = RegisterSymbol("GS.TO", "L2")
</li>
<li>  
  GS_L2_UDP = RegisterSymbol("GS.TO", "L2", "5555")
</li>
<li>  
  GS_TOS  = RegisterSymbol("GS.TO", "TOS")
</li>
<li>  
  test2 = SnapShot(["TD.TO", "X.TO", "ACB.TO","CRON.TO"], "IMBALANCE")
</li>
<li>  
  test3 = TOSFileReader()
</li>
<li>  
  test4 = ClosingImbalanceFile()
</li>
<li>  
  testBuy  = BuyMarketOrder("ES\M19.CM", "1")
</li>
<li>  
  test6Sell = SellMarketOrder("ACB.TO", 100)
</li>
<li>  
  test7 = RegisterImbalance()
</li>
<li>  
  test8 = ImbalanceFileReader()
</li>
<li>  
  test5 = Imbalance().loadfile(200000000.00)
</li>
<li>  
  test9 = TSXClosingImbalance.loadfile(10000000.00, ".TO")
</li>
<li>  
  test10 = BuyFutures()
</li>
<li>  
  test11 = registerSP500()
</li>
<li>  
  x = LoadSymbols()
  print(x.get.symbols)
</li>
<li>  
  test13 = registerSP500(x.get.symbols)
</li>
<li>  
  test12.listSymbols()
</li>
<li>  
  test1 = RegisterSymbols(x.get.symbols, "TOS")
</li>
<li>  
  BuyMarketOrder("CRON.TO", "100")
</li>
<li>  
  SellMarketOrder("ACB.TO", "100")
</li>
<li>  
  test = SubmitMarketOrder("WEED.TO", "Buy", "100")
</li>
<li>  
  test = BuyMarketOrder("ACB.TO", "100")
</li>
<li>  
  test = SellMarketOrder("ACB.TO", "100")
</li>
<li>  
  L1=RegisterSymbol("ACB.TO", "L1", "5555")
</li>
<li>  
  reactor.listenUDP(5555, ppro_datagram())
  reactor.run()
</li>

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
</p>


