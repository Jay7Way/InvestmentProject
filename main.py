from Functions.DataParser import dataParser
import pandas as pd

#MktInput = pd.DataFrame()

MktInput = dataParser("AAPL", "history", apikey='HIIHSE0ZFJGE38PI')
#dataParser("GOOGL", "history")
#dataParser("INTC", "history")
#dataParser("MFST", "history")
