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
                 query string and extract stock chart v2 for a given stock
    INPUT: query string dictionary
    OUTPUT: stock chart v2 dictionary
    """
    auto_complete_list= fm.auto_complete_mover_in()
    chart_v2_list= list()

    # Extract chart_v2 for a given stock
    querystring_list= qs.chart_query_string(auto_complete_list)
    
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart"

    for querystring in querystring_list:
        chart_v2_dict= miner(url, querystring)
        chart_v2_list.append(chart_v2_dict)

    # Moving out the file to blob and data lake
    fm.chart_v2_mover_out(chart_v2_list)

    return "Success!"
