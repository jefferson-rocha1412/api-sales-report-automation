import os
from config.config import Config
from utils.logger import setup_logger

logger = setup_logger()

def create_report(data):
    # CREATE THE OUTPUT FOLDER
    os.makedirs(Config.OUTPUT_FOLDER, exist_ok=True)

    file_path = os.path.join(Config.OUTPUT_FOLDER, Config.OUTPUT_FILENAME)
    
    data.to_excel(file_path, index=False)

    logger.info(f'File successfuly saved {file_path}.')