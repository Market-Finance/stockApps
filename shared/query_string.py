from datetime import datetime
from datetime import timedelta

def analysis_query_string(data:list):
    """
    DESCRIPTION: The purpose of this method is to extract the
    query string for the stock get analysis API
    INPUT: List of JSON [Auto_complete]
    OUTPUT: List of query stings- List of dictionaries
    """
    queryString_list = list()
    for i in range(len(data)):
        queryString = {"symbol": data[i]['q'], "region": data[i]['region']}
        queryString_list.append(queryString)

    return queryString_list

def chart_query_string(data:list):
    """
    DESCRIPTION: The purpose of this function is to extract the 
    query string for get chart V2 and V3 
    INPUT: List of JSON [Auto_complete]
    OUTPUT: List of query strings- List of dictionaries
    """
    queryString_list = list()
    for i in range(len(data)):
        queryString = {"interval":"1m", "symbol": data[i]['q'], "range":"1d", "region":data[i]['region']}
        queryString_list.append(queryString)

    return queryString_list

def holders_query_string(data:list):
    """
    DESCRIPTION: The purpose of this method is to extract 
    the query string for the stock holders analysis API 
    INPUT: List of JSON [Auto_complete]
    OUTPUT: List of query strings- list of dictionaries
    """
    queryString_list = list()
    for i in range(len(data)):
        queryString = {"symbol": data[i]['q'], "region": data[i]["region"]}
        queryString_list.append(queryString)

    return queryString_list

def holdings_query_string(data:list):
    """
    DESCRIPTION: The purpose of this function is to extract the query
    string for the stock holdings API
    INPUT: List of JSON [Auto_complete]
    OUTPUT: List of query strings- List of dictionaries
    """
    queryString_list = list()
    for i in range(len(data)):
        queryString = {"symbol": data[i]['q'], "region": data[i]["region"]}
        queryString_list.append(queryString)

    return queryString_list

def insider_roster_query_string(data:list):
    """
    DESCRIPTION: The purpose of this method is to extract the query 
    string for the insider roster API 
    INPUT: List of JSON [Auto_complete]
    OUTPUT: List of query string- List of dictionaries
    """
    queryString_list = list()
    for i in range(len(data)):
        queryString = {"symbol": data[i]['q'], "region": data[i]["region"]}
        queryString_list.append(queryString)

    return queryString_list

def insider_transactions_query_string(data:list):
    """
    DESCRIPTION: The purpose of this method is to extract the
    query string for the stock insider_transaction API
    INPUT: List of JSON [Auto_complete]
    OUTPUT: List of query strings- List of dictionaries
    """
    queryString_list = list()
    for i in range(len(data)):
        queryString = {"symbol": data[i]['q']}
        queryString_list.append(queryString)

    return queryString_list    

def options_query_string(data:list):
    """
    DESCRIPTION: The pupose of this method is to extract the query string
    for the stock get options API 
    INPUT: List of JSON [Auto_complete]
    OUTPUT: List of query strings- List of dictionaries
    """
    # Covert current_date_time into EPOX date time (seconds)
    date = datetime.now() - timedelta(days=-1)
    y= date.year
    m= date.month
    d= date.day
    h= 23
    min= 59

    dateRange = datetime(y, m, d, h, min).timestamp()
    
    queryString_list = list()
    for i in range(len(data)):
        queryString = {"symbol": data[i]['q'], "date": str(int(dateRange)), "region":data[i]['region']}
        queryString_list.append(queryString)

    return queryString_list

def profile_query_string(data:list):
    """
    DESCRIPTION: The purpose of this methos is to extract the query string
    for the stock profile
    INPUT: List of JSON [Auto_complete]
    OUTPUT: List of query strings- List of dictionaries
    """
    queryString_list = list()
    for i in range(len(data)):
        queryString = {"symbol": data[i]['q'], "region": data[i]["region"]}
        queryString_list.append(queryString)

    return queryString_list

def recommendations_query_string(data:list):
    """
    DESCRIPTION: The purpose of this method is to extract the
    query string for the stock get recommendation API
    INPUT: List of JSON [Auto-Complete]
    OUTPUT: List of query strings- List of dictionaries
    """
    queryString_list = list()
    for i in range(len(data)):
        queryString = {"symbol": data[i]['q']}
        queryString_list.append(queryString)

    return queryString_list

def time_series_query_string(data:list):
    """
    DESCRIPTION: The purpose of this method is to extract 
    the query string for the stock get time series API
    INPUT: List of JSON [Auto_complete]
    OUTPUT: List of query strings- List of dictionaries
    """
    # Convert current_date_time into EPOX Date time (seconds)
    dateRange_list = list()
    for i in range(1,3):
        date = datetime.now() - timedelta(days=i)
        y = date.year
        m = date.month
        d = date.day
        h = 23
        min = 59
        dateRange = datetime(y, m, d, h, min).timestamp()
        dateRange_list.append(dateRange)

    queryString_list = list()
    for i in range(len(data)):
        queryString = {"symbol": data[i]['q'], "period2": str(int(dateRange_list[1])), "period1": str(int(dateRange_list[0])), "region":data[i]["region"]}
        queryString_list.append(queryString)

    return queryString_list

def upgrade_downgrades_query_string(data:list):
    """
    DESCRIPTION: The purpose of this method is to extract the
    query string for the stock get upgrade and downgrades API
    INPUT: List of JSON [Auto_complete]
    OUTPUT: List of query strings- List of dictionaries
    """
    queryString_list = list()
    for i in range(len(data)):
        queryString = {"symbol": data[i]['q'], "region": data[i]['region']}
        queryString_list.append(queryString) 
    
    return queryString_list
