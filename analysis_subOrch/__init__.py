import logging
import os
from datetime import datetime
import azure.functions as func
import azure.durable_functions as df


import shared.function_mover as fm
import shared.query_string as qs

def orchestrator_function(context: df.DurableOrchestrationContext):
    auto_complete_list= fm.auto_complete_mover_in()

    # Extract chart_v2 for a given stock 
    querystring_list= qs.analysis_query_string(auto_complete_list)

    analysis_activity= [
        context.call_activity('analysis', querystring) for
            querystring in querystring_list]
    
    analysis_list= yield context.task_all(analysis_activity)

    #Moving out the file to blob
    fm.analysis_mover_out(analysis_list)
    
    return "Success!"

main= df.Orchestrator.create(orchestrator_function)

