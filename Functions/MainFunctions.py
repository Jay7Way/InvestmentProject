def getAccount(accName, accList):
    for i in range (0,len(accList)):
        if accList[i].name == accName:
            return i

    return None
