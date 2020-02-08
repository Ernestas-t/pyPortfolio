#pyPorfolio v0.3
#started 2020-02-07
import json
import yfinance as yf
import os
import time
#import pandas as pd

version = 0.3

#print current version of the program
def versionPrint():
    print('pyPortfolio v' + str(version))
    print('\n')

versionPrint()
myPortfolio = {}

myPortfolio = json.load(open('C:/Users/Ernestas/Documents/pyPortfolio/config.json'))

#listing available functions
def helpCommand():
    print("""Available functions:
    help
    add
    print
    save
    clear
    total
    total now""")

#clear all values in myPortfolio
def clearPortfolio():
    myPortfolio.clear()

def currentPortfolioSum():
    #os.system('cls') -- for further use clearing the screen
    #versionPrint() -- after clearing always print the current version
    totalCurrentPrice = 0.0
    #print('Downloading data...')
    #iterate through all the tickers in myPortfolio
    for tickers in myPortfolio:
      data = yf.Ticker(tickers)
      dictionary = (data.info)
      price = dictionary['bid']
      #iterate through ticker amount values and add up to price
      for ticker in myPortfolio[tickers]:
         for _, value in ticker.items():
             currentPrice = (float(value[1]) * price)
             totalCurrentPrice += currentPrice
    return float(totalCurrentPrice)

#add a new trade to the portfolio
def addTrade():
    while True:
        trade = []
        tickerCheck = input('Enter ticker: ')
        if tickerCheck == 'q':
            break
        while True:
            dateCheck = input('Enter trade date: ')
            if dateCheck == 'q':
                break
            date = dateCheck
            priceCheck = input('Enter price: ')
            if priceCheck == 'q':
                break
            amountCheck = input('Enter amount: ')
            if amountCheck == 'q':
                break
            tradeDictionary = {int(date): [float(priceCheck), float(amountCheck)]}
            trade.append(tradeDictionary)
            myPortfolio[tickerCheck] = trade

def percentage(value1, value2):
    return (((value1 - value2) / value2) * 100.0)


#current portfolio sum
def portfolioSum():
    totalPortfolio = 0.0
    for tickers in myPortfolio:
        for trades in myPortfolio[tickers]:
            for _, value in trades.items():
                totalPortfolio += float(value[0])
    return (totalPortfolio)

#check inputed user command
def checkInput(command):
    if command == 'help':
        helpCommand()
    elif command == 'add':
        addTrade()
    elif command == 'print':
        printPorfolio()
    elif command == 'save':
        savePorfolio()
    elif command == 'clear':
        clearPortfolio()
    elif command == 'total':
        print(portfolioSum())
    elif command == 'total now':
        print('Downloading data...')
        Download = currentPortfolioSum()
        print(round(Download, 2), '$')
        print(round(percentage(Download, portfolioSum()), 2), '%')
    else :
        print('Unknown command', '\n')

#list current portfolio
def printPorfolio():
    for tickers in myPortfolio:
        print (tickers)
        for trades in myPortfolio[tickers]:
            for key, value in trades.items():
                print(key, ' : ', value[0], '$', 'shares:', value[1])
    print()

#save portfolio to json file
def savePorfolio():
    save = json.dumps(myPortfolio)
    with open('C:/Users/Ernestas/Documents/pyPortfolio/config.json', 'w') as file:
        file.write(save)
        file.close

#user input interface
while True:
    user_input = input('Enter command: ')
    if user_input == 'exit':
        break
    checkInput(user_input)