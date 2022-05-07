# Import Libraries
import os
import pandas as pd
import numpy as np 
import requests
import json
import time 
import random 
import sys

from shared.fun_request import miner

# Override default settings
sys.setrecursionlimit(10000)

def main(querystring):
    """
    DESCRIPTION: The purpose of this function is to pass a query string
                 and extract holdings for a given stock 
    INPUT: query string dictionary
    OUTPUT: holdings dictionary
    """
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holdings"
    holdings_dict= miner(url, querystring)
    return holdings_dict
