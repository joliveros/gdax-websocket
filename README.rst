gdax-websocket
================
.. image:: https://api.travis-ci.org/joliveros/gdax-websocket.svg?branch=master
    :target: https://travis-ci.org/joliveros/gdax-websocket
.. image:: https://requires.io/github/joliveros/gdax-websocket/requirements.svg?branch=master
    :target: https://requires.io/github/joliveros/gdax-websocket/requirements?branch=master
.. image:: https://coveralls.io/repos/joliveros/gdax-websocket/badge.svg?branch=master
    :target: https://coveralls.io/r/joliveros/gdax-websocket?branch=master

Install
-------

.. code-block:: sh

    $ pip install gdax-websocket

Usage
-----

1. First you should set your `GDAX_API_KEY` and `GDAX_API_SECRET`. It can
   be done as follows:

.. code-block:: sh

    $ cp .env.example .env
    #  edit .env to reflect your API key and secret
    $ source .env

2. Then in your project you can consume `Instrument` as follows:

.. code-block:: python

    from gdax_websocket import Instrument
    import asyncio
    import websocket

    websocket.enableTrace(True)

    XBTH17 = Instrument(symbol='XBTH17',
                        # subscribes to all channels by default, here we
                        # limit to just these two
                        channels=['margin', 'orderBook10'],
                        # you must set your environment variables to authenticate
                        # see .env.example
                        shouldAuth=True)

    # Get the latest orderbook
    orderBook10 = XBTH17.get_table('orderBook10')

    # subscribe to all action events for this instrument
    XBTH17.on('action', lambda x: print("# action message: %s" % x))

    loop = asyncio.get_event_loop()
  loop.run_forever()

Examples
--------

Run example scripts:

.. code-block:: sh

    $ RUN_ENV=development python -m examples.example-1

Tests
-----

Testing is set up using `pytest <http://pytest.org>` and coverage is handled
with the pytest-cov plugin.

Run your tests with `py.test` in the root directory.

Coverage is ran by default and is set in the `pytest.ini` file.
To see an html output of coverage open `htmlcov/index.html` after running the tests.
