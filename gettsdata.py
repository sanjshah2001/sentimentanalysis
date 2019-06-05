#!/usr/bin/python

# This script will receive pricing and sentiment feed from data provider
# Usage: gettsdata.py -i <TickerSymbol> -r <RANGE> -m <MONTH> -d <DAY> -y <YEAR>
# Example: gettsdata.py -i TWTR -r 365 -m 1 -d 1 -y 2016 or just run the script
# Ensure data provider has valid data for Symbol provided.  For testing, leverage default values provided by running script without any arguments

import quandl
import datetime
import sys
import getopt

def main(argv):

# Pre-define day range and stock symbol in case user don't provide them
 rang_e = 20
 yea_r = 2017
 mont_h = 6
 da_y = 1
 
# Simulation of sentiment data for 2018 as provider do not have data for 2017 as free sample
 syea_r = 2018

 TickerSymbol = 'TWTR'

 try:
   opts, args = getopt.getopt(argv,"i:r:y:m:d:",["HELP=","iSym=","RANGE=","MONTH=","DATE=","DAY="])
 except getopt.GetoptError:
   print ('gettsdata.py -i <TickerSymbol> -r <RANGE> -m <MONTH> -d <DAY> -y <YEAR>')
   sys.exit(2)
 for opt, arg in opts:
   if opt == ('-h', "--HELP"):
         print ('gettsdata.py -i <TickerSymbol>')
         sys.exit()
   elif opt in ("-i", "--iSym"):
         TickerSymbol = arg
   elif opt in ("-r", "--RANGE"):
          rang_e = int(arg)
   elif opt in ("-y", "--YEAR"):
          yea_r = int(arg)
   elif opt in ("-m", "--MONTH"):
          mont_h = int(arg)
   elif opt in ("-d", "--DAY"):
         da_y = int(arg)

# INPUT YOUR API KEY HERE
 quandl.ApiConfig.api_key = "<YOUR KEY>"

# Temporary store of input data
 sd = open("senti_data", "w+")
 pd = open("price_data", "w+")

 dat_e = datetime.datetime(yea_r, mont_h, da_y)
 sdat_e = datetime.datetime(syea_r, mont_h, da_y)

 for DAYS in range(rang_e):
    dat_e += datetime.timedelta(days=1)
    sdat_e += datetime.timedelta(days=1)

# Fetch data using quandle API
    senti_data = quandl.get_table('IFT/NSA', date=sdat_e, ticker=TickerSymbol)
    mkt_data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'close'] }, ticker = [TickerSymbol], date = dat_e, paginate=False)
    senti_str = str(senti_data)
    senti_split =  senti_str.split()
    Date = senti_split[13]
    Sentim = senti_split[14]
    NewsVol = senti_split[16]
    NewsBuz = senti_split[17]
    mkt_str = str(mkt_data)
    mkt_split =  mkt_str.split()
    if mkt_split[7] != "[]" and Sentim != "0.0":
        Price = mkt_split[7]
        PDate = mkt_split[6]
        Senti_DATA = "[{\"Date\":\""+Date+"\",\"Sentiment\":\""+Sentim+"\",\"News-Volume\":\""+NewsVol+"\",\"News-Buzz\":\""+NewsBuz+"\"}]"
        Price_DATA = "[{\"PDate\":\""+PDate+"\",\"Price\":\""+Price+"\"}]"
        sd.write(Senti_DATA)
        pd.write(Price_DATA)
        sd.write("\n")
        pd.write("\n")
 sd.close()
 pd.close()


if __name__ == "__main__":
   main(sys.argv[1:])
