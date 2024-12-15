from common.dataBaseCredentials import NAME_DATABASE
from dataBase.shareDB import getListShare

import os

def searchListShares():
    listShares = getListShare(NAME_DATABASE)
    symbols = [item[0] for item in listShares]
    return symbols


