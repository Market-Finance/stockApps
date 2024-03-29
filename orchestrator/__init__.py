from enum import auto
import logging
import json
import os
from datetime import datetime
import profile
import azure.functions as func 
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):

    activity_function_list= ["analysis_subOrch", "chart_v2_subOrch", "chart_v3_subOrch",
                             "holders_subOrch", "holdings_subOrch", "insider_roster_subOrch",
                             "insider_transactions_subOrch", "options_subOrch", "profile_subOrch",
                             "recommendations_SubOrch", "time_series_subOrch", "upgrade_downgrades_subOrch",
                             "statistics_v2", "statistics_v3"]

    # Run multiple device provisioning flows in parallel 
    provisioning_tasks= []
    for func_name in activity_function_list:
        provision_task= context.call_sub_orchestrator(func_name)
        provisioning_tasks.append(provision_task)

    yield context.task_all(provisioning_tasks)

    return "Success"

main= df.Orchestrator.create(orchestrator_function)



