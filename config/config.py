class Config:
    # WEB URL
    API_URL = "https://dummyjson.com/products"

    # DATA COLUMNS
    DATA_COLUMNS = ["id", "title", "category", "price", "discountPercentage", "rating", "stock"]

    # FOLDERS
    OUTPUT_FOLDER = 'output'
    LOG_FOLDER = 'logs'

    # FILENAME
    OUTPUT_FILENAME = 'data_summary.xlsx'
    LOG_FILENAME = 'api_sales_report.log'

    # REQUEST TIMEOUT TIME
    REQUEST_TIME = 10