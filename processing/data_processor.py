import pandas as pd
from config.config import Config
from utils.logger import setup_logger

logger = setup_logger()

def process_data(products):
    product_df = pd.DataFrame(products)

    new_products_df = product_df[Config.DATA_COLUMNS]

    logger.info('Successfully processed product data')

    return new_products_df

if __name__ == "__main__":
    process_data()
    