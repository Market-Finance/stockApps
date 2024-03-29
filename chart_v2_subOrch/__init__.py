import logging
import os
from datetime import datetime
import azure.functions as func
import azure.durable_functions as df


import shared.function_mover as fm
import shared.query_string as qs

def orchestrator_function(context: df.DurableOrchestrationContext):

    yield context.call_activity('chart_v2', "None")
    
    return "Success!"

main= df.Orchestrator.create(orchestrator_function)

