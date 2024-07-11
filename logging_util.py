import logging

# Configure logging to write messages to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("project_log.log"),
        logging.StreamHandler()
    ]
)

def log_message(level, message):
    if level == 'INFO':
        logging.info(message)
    elif level == 'WARNING':
        logging.warning(message)
    elif level == 'ERROR':
        logging.error(message)
    else:
        logging.debug(message)
