import logging
import os
from config.config import Config

def setup_logger():
    # CREATE THE LOG FOLDER
    os.makedirs(Config.LOG_FOLDER, exist_ok=True)

    # CREATE THE FILENAME PATH
    log_path = os.path.join(Config.LOG_FOLDER, Config.LOG_FILENAME)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
        )

    return logging.getLogger(__name__)