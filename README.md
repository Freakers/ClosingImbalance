<H1>Closing Imbalance</H1>
<p>
The TMX Closing Imbalance code TSXClosingImbalance.py contains the various classes which are listed after the section on how the program works.

This is a general purpose utility which allows the user to register Imbalances by trading region.
  

<H2>How to run TMX Closing Balance Closing Imbalance</H2>
<p>
  The porgram waits until a specific date and time and registers the imbalance for the NCSA region (North America) and then waits until 15 seconds after the TSX MOC Imbalance is disseminated (3:40:15 PM) and scans the file for imbalances overs a specified user threshold
  
  The datetime function works as follows datetime(YYYY, MM, DD, HH, MM, SS, 0)
  Pause until June 24, 2019 15:25:00
  
    pause.until(datetime(2019, 6, 24, 15, 25, 0, 0))
    
  Register the Imbalance Feed in the API has been setup to register all imbalances for the NCSA trade region (North America)
  
    step1 = RegisterImbalance()
    
  Pause until June 24, 2019 15:40:15
  
    pause.until(datetime(2019, 6, 24, 15, 40, 15, 0))
    
  Read the imbalance file C:\Program Files (x86)\Ralota\PPro8 Guapy\IMBAL_CIRC_1 created by the PPro API and the scan the file and report all trades over 5 milliom
  
    step2 = TSXClosingImbalance.loadfile(5000000.00, ".TO")
</p>
</p>
<p>
  
  Project containing the following PYTHON classes used to demonstrate the PPro8 API and to code and test the TSX closing imbalance.
  The project was developed using Python 3.7.2 and Intellij PYCharm Community Edition 2019.1.1 running on a windows 10 platform.
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
<H1>Symbols by Markets</H1>  
The project also contains a folder called "\data" and this folder contains a list of symbols for each exchange 
These symbol lists for various markets that can be used by the API or used as training symbol list fopr practice in TMS. 
Please check to see which symbols are available on specific markets by going to https://www.daytradetheworld.com/wiki/

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

<H2>How to Run L1TOS consolidated feed reader</H2>
<p>
The L1TOS Consolidated feed reader is essential a python tool that allows a trade to conslidate the Last Time Of Sale (TOS Feed) with the L1 Quotes of the 
symbol being traded. It allows the trader to see how the trades are related to the Best Bid and Ask to allow the trader to view trades relative to the 
order flow within the book.

The following is a realtime output produced one a minute by minute sampling of trades into the L1 book:

09:28:46.172: L1 Bid @ 2909.00	Size: 156	Ask @ 2909.25	Size: 70
09:28:46.172: Traded @ 2909.00 Size: 1
Trade into Bid:	     189	%56
Trade into Ask:	     146	%43
Trade MidPoint:	       0	%0

The first two line items are the last L1 quotes captured giving the trader the last spread in the book and the second line
is the TOS related to the latest L1 quote.

The next three lines are how the trades relate to the buyers and sellers

Trade into Bid:	     189	%56
Trade into Ask:	     146	%43
Trade MidPoint:	       0	%0

Trade into bid reflects how trades are currently trading into the bid price (meaning the sellers are trading into the bidders)
Trade into ask reflects how trades are currently trading into the ask price (meaning the buyers are trading into the sellers)
Trade into midpoint reflects how trades are currently trading into the mid point price (meaning the buyers or sellers are trading into the midpoint)

This three numbers create a trading indicator showing a upward or downward price movement based on trading sentiment.

This indicator is collected on a minute by minute basis and is the reset every minute to ensure that the trader is using a realtime indicator.

</p>