from common.dataBaseCredentials import NAME_DATABASE
from dataBase.shareDB import getListCrypto, getListShare

import os

def searchListShares():
    listShares = getListShare(NAME_DATABASE)
    print("listShares ", listShares)
    symbols = [item[0] for item in listShares]
    return symbols

def searchListCrypto():
    listCrypto = getListCrypto(NAME_DATABASE)
    symbols = [item[0] for item in listCrypto]
    return symbols




