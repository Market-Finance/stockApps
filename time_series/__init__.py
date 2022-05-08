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
    and extract stock time_series for a given stock
    INPUT: query string dictionary
    OUTPUT: time series dictionary
    """
    auto_complete_list= fm.auto_complete_mover_in()
    time_series_list= list()

    # Extract time series for a given stock
    querystring_list= qs.time_series_query_string(auto_complete_list)
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-timeseries"
    
    for querystring in querystring_list:
        time_series_dict= miner(url, querystring)
        time_series_list.append(time_series_dict)

    # Moving out the file to blob and datalake
    fm.time_series_mover_out(time_series_list)
    return "Success!"
