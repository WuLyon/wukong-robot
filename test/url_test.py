from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

now = datetime.now()
date1 = now.timetuple()
date2 = mktime(date1)
date = format_date_time(mktime(now.timetuple()))
logger.info(now)
logger.info(date1)
logger.info(date2)
logger.info(date)