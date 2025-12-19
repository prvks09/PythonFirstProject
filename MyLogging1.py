import MyLogger
logger_instance = MyLogger.MyLogger(__name__)
logger = logger_instance.get_logger()
logger.info("MyLogger module has been imported")
