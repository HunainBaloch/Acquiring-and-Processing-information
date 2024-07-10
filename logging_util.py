import logging

logging.basicConfig(filename='project_log.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def log_message(message):
    logging.info(message)
