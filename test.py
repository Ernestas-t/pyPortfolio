import yfinance as yf
import os
import time

#for key, value in dictionary.items():
#    print(key, ' : ', value)
tickers = input()

while True:
    aapl = yf.Ticker(tickers)
    dictionary = (aapl.info)
    bid = 'bid : ' + str(dictionary['bid'])
    ask = 'ask : ' + str(dictionary['ask'])
    os.system('cls')
    print(tickers)
    print(bid)
    print(ask)
    time.sleep(2)