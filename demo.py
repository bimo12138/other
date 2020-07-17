import logging
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]   %(filename)s   %(message)s',
                    datefmt=' %Y-%m-%d %H:%M:%S ',
                    filename='test.log',
                    filemode='a')
 
def base_log(message):
    logging.info(message)


def important_log(message):
    logging.warn(message)

def error_log(message):
    logging.error(message)

