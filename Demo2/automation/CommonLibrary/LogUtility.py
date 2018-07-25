import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def CreateLoggerFile(filename):
    try:
        fulllogname = "D:\\pythonCode\\Demo2"+"\\"+filename+".log"
        fh = logging.FileHandler(fulllogname)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s [line:%(lineno)d] %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    except Exception as err:
        logger.debug("Error when creating log file, error message: {}".format(str(err)))


def Log(message):
    logger.debug(message)

