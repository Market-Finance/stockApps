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
                 and extract stock get options
    INPUT:  query string dictionary
    OUTPUT: stock options dictionary
    """
    auto_complete_list= fm.auto_complete_mover_in()
    options_list= list()

    # Extract options for a given stock
    querystring_list= qs.options_query_string(auto_complete_list)
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-options"
    
    for querystring in querystring_list:
        options_dict= miner(url, querystring)
        options_list.append(options_dict)
    
    # Moving out the file to blob and datalake
    fm.options_mover_out(options_list)
    return "Success!"
