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
    DESCRIPTION: The purpose of this function is to pass query string
    and extract stock recommendation for a given stock
    INPUT: query string dictionary
    OUTPUT: recommendations dictionary
    """
    auto_complete_list= fm.auto_complete_mover_in()
    recommendations_list= list()

    # Extract recommendations roster for a given stock
    querystring_list= qs.recommendations_query_string(auto_complete_list)
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-recommendations"
    
    for querystring in querystring_list:
        recommendations_dict= miner(url, querystring)
        recommendations_list.append(recommendations_dict)
    
    # Moving out the file to blob and datalake
    fm.recommendations_mover_out(recommendations_list)
    return "Success!"
