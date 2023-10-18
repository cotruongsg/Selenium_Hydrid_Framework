import logging

class LogGen:
    @staticmethod
    def loggen():
        # to get the name of the test case file name at runtime

        logger = logging.getLogger(__name__)

        # FileHandler class to set the location of log file

        fileHandler = logging.FileHandler('.\\Logs\\automationLog.log')

        # Formatter class to set the format of log file

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s",datefmt='%m/%d/%Y %I:%M:%S %p')

        # object of FileHandler gets formatting info from setFormatter #method

        fileHandler.setFormatter(formatter)

        # logger object gets formatting, path of log file info with addHandler #method

        logger.addHandler(fileHandler) 

        # setting logging level to INFO

        logger.setLevel(logging.INFO)
        return logger