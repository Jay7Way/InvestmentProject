from Functions.DataParser import dataParser
import pandas as pd

MktInput = pd.DataFrame()

MktInput = MktInput.append(dataParser("AAPL", "history"))
dataParser("GOOGL", "history")
dataParser("INTC", "history")
dataParser("MFST", "history")
