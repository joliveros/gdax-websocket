from __future__ import absolute_import
from gdax_websocket.websocket import GdaxWebsocket
from time import sleep
import logging
import websocket

_logger = logging.getLogger('websocket')
_logger.setLevel(logging.DEBUG)
websocket.enableTrace(True)

ws = GdaxWebsocket()
ws.connect()
ws.subscribe_action('orderBookL2')

while True:
    sleep(1)
