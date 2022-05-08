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
    DESCRIPTION: The purpose of this function is to pass a
                 query string and extract stock analysis for a given stock
    INPUT: query string dictionary
    OUTPUT: stock analysis dictionary
    """
    auto_complete_list= fm.auto_complete_mover_in()
    analysis_list= list()

    # Extract analysis for a given stock 
    querystring_list= qs.analysis_query_string(auto_complete_list)
    
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-analysis"
    for querystring in querystring_list:
        analysis_dict= miner(url, querystring)
        analysis_list.append(analysis_dict)

    #Moving out the file to blob and data lake
    fm.analysis_mover_out(analysis_list) 
    
    return "Success!"
