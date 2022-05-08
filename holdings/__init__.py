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

import shared.function_mover as fm
import shared.query_string as qs

def main(name:str):
    """
    DESCRIPTION: The purpose of this function is to pass a query string
                 and extract holdings for a given stock 
    INPUT: query string dictionary
    OUTPUT: holdings dictionary
    """
    auto_complete_list= fm.auto_complete_mover_in()
    holdings_list= list()

    # Extract holders for a given stock
    querystring_list= qs.holdings_query_string(auto_complete_list)
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holdings"
    
    for querystring in querystring_list:
        holdings_dict= miner(url, querystring)
        holdings_list.append(holdings_dict)
    
    # Moving out the file to blob and datalake
    fm.holdings_mover_out(holdings_list)
    
    return "Success!"
