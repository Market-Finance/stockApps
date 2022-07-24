import shared.mover as m

def auto_complete_mover_in():
    """
    DESCRIPTION: The purpose of this function is to download auto complete
                 from blob storage location 
    INPUT: None
    OUTPUT: encoded string 
    """
    # Blob file path and file_name source files
    blob_file_path= 'MarketFinance/common/auto_complete_new'
    blob_file_name= 'auto_complete.json'

    data= m.blob_storage_download(blob_file_path, blob_file_name)
    return data

def analysis_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined analysis
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'analysis.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/analysis'
    data_lake_file_name= 'analysis'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def chart_v2_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined chart_v2
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'chart_v2.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/chart_v2'
    data_lake_file_name= 'chart_v2'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def chart_v3_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined chart_v3
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'chart_v3.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/chart_v3'
    data_lake_file_name= 'chart_v3'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def holders_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined holder
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'holders.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/holders'
    data_lake_file_name= 'holders'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def holdings_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined holdings
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'holdings.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/holdings'
    data_lake_file_name= 'holdings'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def insider_roster_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined insider roster
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'insider_roster.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/insider_roster'
    data_lake_file_name= 'insider_roster'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def insider_transactions_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined insider transaction
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'insider_transaction.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/insider_transaction'
    data_lake_file_name= 'insider_transaction'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def options_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined options
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'options.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/options'
    data_lake_file_name= 'options'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def profile_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined profile
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'profile.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/profile'
    data_lake_file_name= 'profile'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def recommendations_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined recommendations
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'recommendation.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/recommendation'
    data_lake_file_name= 'recommendation'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def time_series_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined time series
                 to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'time_series.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/time_series'
    data_lake_file_name= 'time_series'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"

def upgrade_downgrades_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined upgrade and
                 downgrade to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'upgrade_downgrades.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/upgrade_downgrades'
    data_lake_file_name= 'upgrade_downgrades'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"


def statistics_v2_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined upgrade and
                 downgrade to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'statistics_v2.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/statistics_v2'
    data_lake_file_name= 'statistics_v2'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"


def statistics_v3_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined upgrade and
                 downgrade to this desired blob storage and data lake location 
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/stock'
    blob_file_name= 'statistics_v3.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'stock/statistics_v3'
    data_lake_file_name= 'statistics_v3'

    m.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    m.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success!"



