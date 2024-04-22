from US_Visa.exception import USvisaException
from US_Visa.logger import logging
import sys

try:
    a=1/"10"
except Exception as e:
    logging.info(e)
    raise USvisaException(e,sys) from e