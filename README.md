<H1>ClosingImbalance</H1>

<p>
  This project contains the folllowing PYTHON classes used to demonstrate the PPro8 API and to code the TSX closing imbalance.
  The project was developed using Python 3.7.2 and Intellij PYCharm Community Edition 2019.1.1 running on a windows 10 platform
</p>
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

<p>
  This file contains the folllowing PYTHON unit tests used to demonstrate the above classes
</p>

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

<p>
  The project also conatins a \data folder containing Exchange Symbol Lists for various markets traded at DTTW. Please check to see which symbols are available on specific markets
</p>
  <li>Amsterdam.csv 
  <li>Bovespa.csv
  <li>Brussels.csv
  <li>CBOE-BITCOIN.csv
  <li>CBOE-VIX.csv
  <li>CBOE.csv
  <li>Copenhagen.csv
  <li>CSE.csv
  <li>Dublin.csv
  <li>ETF.csv
  <li>Helsinki.csv
  <li>Johannesburg.csv
  <li>Lisbon.csv
  <li>London.csv
  <li>Madrid.csv
  <li>Milan.csv
  <li>Moscow.csv
  <li>NASDAQ.csv
  <li>NYMEX-E-miniCrudeOil.csv
  <li>NYMEX-Gasoline.csv
  <li>NYMEX-Light SweetCrudeOil.csv
  <li>NYMEX-NaturalGas.csv
  <li>NYMEX-NYHarborULSD.csv
  <li>NYMEX.csv
  <li>NYSE-AMEX.csv
  <li>NYSE.csv
  <li>Oslo.csv
  <li>OTC-Pink.csv
  <li>Paris.csv
  <li>SP_500.csv
  <li>Stockholm.csv
  <li>Switzerland.csv
  <li>Turkey.csv
  <li>Vienna.csv
  <li>Warsaw.csv
  <li>Xetra.csv
