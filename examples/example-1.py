#! /home/jose/.pyenv/shims/python

from __future__ import absolute_import
from gdax_websocket.websocket import GdaxWebsocket
import logging
import websocket
import asyncio

_logger = logging.getLogger('websocket')
_logger.setLevel(logging.DEBUG)
websocket.enableTrace(True)

ws = GdaxWebsocket()
ws.connect()
ws.subscribe_action('instrument_')

loop = asyncio.get_event_loop()
loop.run_forever()
