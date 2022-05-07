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

def main(querystring):
    """
    DESCRIPTION: The purpose of this function is to a pass query string 
                 and extract holders for a given stock
    INPUT: query string dictionary
    OUTPUT: holders dictionary  
    """
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holders"
    holders_dict= miner(url, querystring)
    return holders_dict
