import logging

from newrelic.agent import NewRelicContextFormatter


log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s'
logging.basicConfig(format=log_format)

newrelic_formatter = NewRelicContextFormatter()
newrelic_handler = logging.StreamHandler()
newrelic_handler.setFormatter(newrelic_formatter)


logger = logging.getLogger('root')
logger.addHandler(newrelic_handler)
