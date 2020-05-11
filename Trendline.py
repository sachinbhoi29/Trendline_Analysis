import trendln
import matplotlib.pyplot as plt
import os
import yfinance as yf # requires yfinance - pip install yfinance
#
dirname = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(dirname, 'Report\\trendline')
if not os.path.isdir(filepath):
   os.makedirs(filepath)
   
tickers = ['INDUSINDBK.NS','LTI.NS', 'CIPLA.NS' ,'JINDALSAW.NS','BLUESTARCO.NS','WHIRLPOOL.NS','SYMPHONY.NS','HINDCOPPER.NS','FLFL.NS','ABFRL.NS','DMART.NS','SHOPERSTOP.NS','SPIC.NS','524013.BO','IFCI.NS','TFCILTD.NS','BATAINDIA.NS','KANSAINER.NS','EUROCERA.NS','BERGEPAINT.NS','BHEL.NS','THERMAX.NS','ITDC.NS','PHOENIXTN.BO','LEMONTREE.NS','TAJGVK.NS','INDHOTEL.NS','JINDHOT.BO','ADVANIHOTR.NS','GREAVESCOT.NS','RELIANCE.NS','MAHSCOOTER.NS','JSWSTEEL.NS','SAIL.NS','GULFOILLUB.NS','INOXLEISUR.NS' , 'IOC.NS', 'TATAMOTORS.NS']

for t in tickers:
	try:
		start = '2020-03-01'
		end = '2020-05-4'                      #timeframe = '3mo'   #30d #1mo, 3mo, max, 1y
		hist = yf.download(t,start,end)   # tick.history(period=timeframe, rounding=True)   
		mins, maxs = trendln.calc_support_resistance(hist[-1000:].Close)
		minimaIdxs, pmin, mintrend, minwindows = trendln.calc_support_resistance((hist[-1000:].Low, None)) #support only
		mins, maxs = trendln.calc_support_resistance((hist[-1000:].Low, hist[-1000:].High))
		(minimaIdxs, pmin, mintrend, minwindows), (maximaIdxs, pmax, maxtrend, maxwindows) = mins, maxs
		minimaIdxs, maximaIdxs = trendln.get_extrema(hist[-1000:].Close)
		maximaIdxs = trendln.get_extrema((None, hist[-1000:].High)) #maxima only
		minimaIdxs, maximaIdxs = trendln.get_extrema((hist[-1000:].Low, hist[-1000:].High))
		fig = trendln.plot_support_resistance(hist[-1000:].Close) # requires matplotlib - pip install matplotlib
		t1 = t
		t = t + "_" + start + "_" + end + ".png"
		file = os.path.join(filepath, t )
		t1 = t1 + "_" +  start + "_" + end+ "_" + ".png"
		print("\n Volume ratio: latest day/previous day:", round(hist['Volume'][-1]/hist['Volume'][-2], 4), ",", round(hist['Volume'][-2]/hist['Volume'][-3],4),"," , round(hist['Volume'][-3]/hist['Volume'][-4], 4),"," ,round(hist['Volume'][-4]/hist['Volume'][-5],4),"," ,round(hist['Volume'][-5]/hist['Volume'][-6],4))
		file1 = os.path.join(filepath, t1 )
		plt.savefig(file1, format='png')
		print(t,t1)
		fig = trendln.plot_sup_res_date((hist[-1000:].Low, hist[-1000:].High), hist[-1000:].index) 
		plt.savefig(file, format='png')
	except Exception as e:
		print (e)
		pass



