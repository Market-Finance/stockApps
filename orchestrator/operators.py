# Operator is not in use
from function_mover import *
from query_string import *
  
def analysis_operator(context, auto_complete_list): 
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 analysis for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """ 
    querystring_list= analysis_query_string(auto_complete_list)
    analysis_activity= [
        context.call_activity('analysis', querystring) for
            querystring in querystring_list if querystring]

    analysis_list= yield context.task_all(analysis_activity)
    analysis_mover_out(analysis_list)

def chart_v2_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 chart_v2 for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    querystring_list= chart_query_string(auto_complete_list)
    chart_v2_activity= [
        context.call_activity('chart_v2', querystring) for
            querystring in querystring_list if querystring]

    chart_v2_list= yield context.task_all(chart_v2_activity)
    chart_v2_mover_out(chart_v2_list)

def chart_v3_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 chart_v3 for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    querystring_list= chart_query_string(auto_complete_list)
    chart_v3_activity= [
        context.call_activity('chart_v3', querystring) for
            querystring in querystring_list if querystring]
    
    chart_v3_list= yield context.task_all(chart_v3_activity)
    chart_v3_mover_out(chart_v3_list)

def holders_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 holders for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    querystring_list= holders_query_string(auto_complete_list)
    holders_activity= [
        context.call_activity('holders', querystring) for
            querystring in querystring_list if querystring]
    
    holders_list= yield context.task_all(holders_activity)
    holders_mover_out(holders_list)

def holdings_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 holdings for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    querystring_list= holdings_query_string(auto_complete_list)
    holdings_activity= [
        context.call_activity('holdings', querystring) for
            querystring in querystring_list if querystring]
    
    holdings_list= yield context.task_all(holdings_activity)
    holdings_mover_out(holdings_list)

def insider_roster_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 insider roster for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    querystring_list= insider_roster_query_string(auto_complete_list)
    insider_roster_activity= [
        context.call_activity('insider_roster', querystring) for
            querystring in querystring_list if querystring]
    
    insider_roster_list= yield context.task_all(insider_roster_activity)
    insider_roster_mover_out(insider_roster_list)

def options_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 options for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    # extract stock options, and read it to blob and datalake
    querystring_list= options_query_string(auto_complete_list)
    options_activity= [
        context.call_activity('options', querystring) for
            querystring in querystring_list if querystring]
    
    options_list= yield context.task_all(options_activity)
    options_mover_out(options_list)

def profile_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 profile for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    querystring_list= profile_query_string(auto_complete_list)
    profile_activity= [
        context.call_activity('profile', querystring) for
            querystring in querystring_list if querystring]
    
    profile_list= yield context.task_all(profile_activity)
    profile_mover_out(profile_list)

def recommendations_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 recommendations for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    querystring_list= recommendations_query_string(auto_complete_list)
    recommendations_activity= [
        context.call_activity('recommendations', querystring) for
            querystring in querystring_list if querystring]   
    
    recommendations_list= yield context.task_all(recommendations_activity)
    recommendations_mover_out(recommendations_list)

def time_series_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 time_series for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    querystring_list= time_series_query_string(auto_complete_list)
    time_series_activity= [
        context.call_activity('time_series', querystring) for
            querystring in querystring_list if querystring]
    
    time_series_list= yield context.task_all(time_series_activity)
    time_series_mover_out(time_series_list)

def upgrade_downgrades_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract
                 upgrade/ downgrades for a given stock, and read it it blob
                 data lake storage
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    # extract stock upgrade/ dowgrades, and read it to blob and datalake
    querystring_list= upgrade_downgrades_query_string(auto_complete_list)
    upgrade_downgrades_activity= [
        context.call_activity('upgrade_downgrades', querystring) for
            querystring in querystring_list if querystring]

    upgrade_downgrades_list= yield context.task_all(upgrade_downgrades_activity)
    upgrade_downgrades_mover_out(upgrade_downgrades_list)






    # Extract analysis for a given stock
    querystring_list= qs.analysis_query_string(auto_complete_list)
    analysis_activity= [
        context.call_activity('analysis', querystring) for
            querystring in querystring_list
    ]
    analysis_list= yield context.task_all(analysis_activity)

    # Extract chart_v2 for a given stock
    querystring_list= qs.chart_query_string(auto_complete_list)
    chart_v2_activity= [
        context.call_activity('chart_v2', querystring) for
            querystring in querystring_list
    ]
    chart_v2_list= yield context.task_all(chart_v2_activity)

    # Extract chart_v3 for a given stock
    querystring_list= qs.chart_query_string(auto_complete_list)
    chart_v3_activity= [
        context.call_activity('chart_v3', querystring) for
            querystring in querystring_list
    ]
    chart_v3_list= yield context.task_all(chart_v3_activity)

    # Extract holders for a given stock
    querystring_list= qs.holders_query_string(auto_complete_list)
    holders_activity= [
        context.call_activity('holders', querystring) for
            querystring in querystring_list
    ]
    holders_list= yield context.task_all(holders_activity)

    # Extract holdings for a given stock
    querystring_list= qs.holdings_query_string(auto_complete_list)
    holdings_activity= [
        context.call_activity('holdings', querystring) for
            querystring in querystring_list
    ]
    holdings_list= yield context.task_all(holdings_activity)

    # Extract insider roster for a given stock
    querystring_list= qs.insider_roster_query_string(auto_complete_list)
    insider_roster_activity= [
        context.call_activity('insider_roster', querystring) for
            querystring in querystring_list
    ]
    insider_roster_list= yield context.task_all(insider_roster_activity)

    # Extract options for a given stock
    querystring_list= qs.options_query_string(auto_complete_list)
    options_activity= [
        context.call_activity('options', querystring) for
            querystring in querystring_list
    ]
    options_list= yield context.task_all(options_activity)

    # Extract profile for a given stock
    querystring_list= qs.profile_query_string(auto_complete_list)
    profile_activity= [
        context.call_activity('profile', querystring) for
            querystring in querystring_list
    ]
    profile_list= yield context.task_all(profile_activity)

    # Extract recommendations for a given stock
    querystring_list= qs.recommendations_query_string(auto_complete_list)
    recommendations_activity= [
        context.call_activity('recommendations', querystring) for 
            querystring in querystring_list
    ]
    recommendations_list= yield context.task_all(recommendations_activity)

    # Extract time series for a given stock
    querystring_list= qs.time_series_query_string(auto_complete_list)
    time_series_activity= [
        context.call_activity('time_series', querystring) for
            querystring in querystring_list
    ]
    time_series_list= yield context.task_all(time_series_activity)

    # Extract stock upgrade/ downgrades for a give stock
    querystring_list= qs.upgrade_downgrades_query_string(auto_complete_list)
    upgrade_downgrades_activity= [
        context.call_activity('upgrade_downgrades', querystring) for
        querystring in querystring_list 
    ]
    upgrade_downgrades_list= yield context.task_all(upgrade_downgrades_activity)


    # Moving out all the files to blob and data lake storage
    fm.analysis_mover_out(analysis_list)
    del analysis_list
    fm.chart_v2_mover_out(chart_v2_list)
    del chart_v2_list
    fm.chart_v3_mover_out(chart_v3_list)
    del chart_v3_list
    fm.holders_mover_out(holders_list)
    del holders_list
    fm.holdings_mover_out(holdings_list)
    del holdings_list
    fm.insider_roster_mover_out(insider_roster_list)
    del insider_roster_list
    fm.options_mover_out(options_list)
    del options_list
    fm.profile_mover_out(profile_list)
    del profile_list
    fm.recommendations_mover_out(recommendations_list)
    del recommendations_list
    fm.time_series_mover_out(time_series_list)
    del time_series_list
    fm.upgrade_downgrades_mover_out(upgrade_downgrades_list)
    del upgrade_downgrades_list

    return 'Success'
