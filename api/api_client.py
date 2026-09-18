import requests
from config.config import Config
from utils.logger import setup_logger

# CREATE THE LOGGER OBJECT
logger = setup_logger()

# GET PRODUCTS DATA FROM API
def get_products_data():
    try:
        response = requests.get(Config.API_URL, timeout=Config.REQUEST_TIME)

        response.raise_for_status()

        data = response.json()

        logger.info("Successfully retrived product data from API.")

        return data['products']
    
    except requests.exceptions.ConnectionError as e:
        logger.error(e)
        return None
    except requests.exceptions.Timeout as e:
        logger.error(e)
        return None
    except requests.exceptions.JSONDecodeError as e:
        logger.error(e)
        return None
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return None

# CALLING THE FUNCTION
if __name__ == "__main__":
    get_products_data()