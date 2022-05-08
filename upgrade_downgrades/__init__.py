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
    and extract stock upgrades and downgrades for a given stock
    INPUT: query string dictionary
    OUTPUT: dictionary stock upgrades and downgrades
    """
    auto_complete_list= fm.auto_complete_mover_in()
    upgrade_downgrades_list= list()

    # Extract upgrade downgrades for a given stock
    querystring_list= qs.upgrade_downgrades_query_string(auto_complete_list)
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-upgrades-downgrades"

    for querystring in querystring_list:
        upgrade_downgrades_dict= miner(url, querystring)
        upgrade_downgrades_list.append(upgrade_downgrades_dict)

    # Moving out the file to blob and datalake
    fm.upgrade_downgrades_mover_out(upgrade_downgrades_list)
    return "Success!"
