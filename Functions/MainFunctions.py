import csv
import json
import pandas as pd
from Functions.DataParser import dataParser
from Classes.Account import Account
import pandas as pd

def getAccount(accName, accList):
    for i in range (0,len(accList)):
        if accList[i].name == accName:
            return i

    return None
