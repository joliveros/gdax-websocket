import logging
import os
import alog

##########################################################################################
# Connection/Auth
##########################################################################################

# API URL.
BASE_URL = "wss://ws-feed.gdax.com"

# The BitMEX API requires permanent API keys. Go to https://testnet.bitmex.com/api/apiKeys
# to fill these out.
GDAX_API_KEY = os.environ.get('GDAX_API_KEY')
GDAX_API_SECRET = os.environ.get('GDAX_API_SECRET')

# Available levels: logging.(DEBUG|INFO|WARN|ERROR)
# LOG_LEVEL = os.environ.get('LOG_LEVEL')

LOG_LEVEL = logging.INFO

alog.set_level(LOG_LEVEL)
