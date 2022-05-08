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
    DESCRIPTION: The purpose of this method is to pass a query string
                 and extract insider transaction information for a given stock
    INPUT: dictionary querystring
    OUTPUT: dictionary stock insider transaction
    """
    auto_complete_list= fm.auto_complete_mover_in()
    insider_transactions_list= list()

    # Extract insider transaction for a given stock
    querystring_list= qs.insider_transactions_query_string(auto_complete_list)
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-insider-transactions"
    
    for querystring in querystring_list:
        insider_transactions_dict= miner(url, querystring)
        insider_transactions_list.append(insider_transactions_dict)
    
    # Moving out the files to blob and datalake
    fm.insider_transactions_mover_out(insider_transactions_list)
    return "Success!"
