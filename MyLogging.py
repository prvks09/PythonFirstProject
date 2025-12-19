import math
import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# logging.info("MyLogging module has been imported")
# logging.debug(f"math module functions:")
# logging.warning("This is a warning message from MyLogging module")
# logging.error("This is an error message from MyLogging module")
# logging.critical("This is a critical message from MyLogging module")
logger = logging.getLogger(__name__)

formatter = logger.Formatter(
    level=logging.DEBUG, format='   %(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logger.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.info("Logger initialized in MyLogging module")

i = 2
