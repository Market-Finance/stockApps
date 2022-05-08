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
    DESCRIPTION: The purpose of this function is to a pass query string 
                 and extract holders for a given stock
    INPUT: query string dictionary
    OUTPUT: holders dictionary  
    """
    auto_complete_list= fm.auto_complete_mover_in()
    holders_list= list()

    # Extract holders for a given stock
    querystring_list= qs.chart_query_string(auto_complete_list)
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holders"
    
    for querystring in querystring_list:
        holders_dict= miner(url, querystring)
        holders_list.append(holders_dict)

    # Moving out the file to blob and datalake
    fm.holders_mover_out(holders_list)
    
    return "Success!"
