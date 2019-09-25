#bens API key B09JFLLPFQJIIV6O

import requests
import pandas as pd
import matplotlib.pyplot as plt

def dataParser(ticker, returntype, dataImportType="TIME_SERIES_DAILY", interval="Daily", outputsize="compact", apikey="B09JFLLPFQJIIV6O"):

    #check if we support the requested ticker
    traded_tickers=["AAPL", "GOOGL", "INTC", "MFST"]
    if ticker not in traded_tickers:
        print("Not a valid ticker: " + ticker)
        return 0

    #check supported data delivery
    if returntype == "latest":
        print("Giving latest information of "+ticker)
        #interval = "Daily"
        outputsize = "compact"
    elif returntype == "history":
        print("Giving history (interval: "+interval+") of "+ticker)
        #interval = "Daily"
        outputsize = "full"
    else:
        print("Invalid returntype: " + returntype)
        return 0

    ### magic import code
    requestString="https://www.alphavantage.co/query?function="+dataImportType+"&symbol="+ticker+"&outputsize="+outputsize+"&apikey="+apikey
    print("Request made at "+requestString)
    response = requests.get(requestString)
    # Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
    # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    if response.status_code != 200:
        raise ValueError("Could not retrieve data, code:", response.status_code)
    # The service sends JSON data, we parse that into a Python datastructure
    raw_data = response.json()
    # Let's look at the raw data (it's a lot so let's limit it)
    #raw_data.keys()
    #raw_data['Meta Data']
    # The actual time series is huge, let's just look at the first few items
    # Let's use itertools to do this in a lazy way
    import itertools
    list(itertools.islice(raw_data['Time Series ('+interval+')'].items(), 0,5))
    # Let's be smart and retrieve the name of the column with our actual data
    colname = list(raw_data.keys())[-1]
    # We want to extract the corresponding column only
    data = raw_data[colname]
    df = pd.DataFrame(data).T.apply(pd.to_numeric)
    #df.info()
    #df.head()
    # Next we parse the index to create a datetimeindex
    df.index = pd.DatetimeIndex(df.index)
    # Let's fix the column names
    df.rename(columns=lambda s: s[3:], inplace=True)
    #df.info()
    ### end of magic import code

    #return statements
    if returntype == "latest":
        return df['close'].iloc[0]
    elif returntype == "history":
        return df['close'][0:500]
    else:
        print("This should not happen")
        return 0

#test code
#ticker=input("choose symbol (e.g. MSFT, INTC, AAPL, GOOGL)")
ticker="GOOGL"
tickerInfo=dataParser(ticker=ticker, returntype="history")

print(tickerInfo)
if tickerInfo.size > 1:
    plt1 = tickerInfo.plot(kind='line')
    plt.title("History of "+ticker)
    plt.xlabel("Time")
    plt.xlabel("Price")
