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
                 and extract insider roster for a given stock
    INPUT: query string dictionary
    OUTPUT: insider roster dictionary
    """
    auto_complete_list= fm.auto_complete_mover_in()
    insider_roster_list= list()

    # Extract insider roster for a given stock
    querystring_list= qs.insider_roster_query_string(auto_complete_list)
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-insider-roster"
    
    for querystring in querystring_list:
        insider_roster_dict= miner(url, querystring) 
        insider_roster_list.append(insider_roster_dict)

    # Moving out the file to blob and datalake
    fm.insider_roster_mover_out(insider_roster_list)
    return "Success!"