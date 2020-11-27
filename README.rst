Introduction
============

.. image:: https://readthedocs.org/projects/pimoroni-circuitpython-mics6814/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/mics6814/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/pimoroni/Pimoroni_CircuitPython_MICS6814/workflows/Build%20CI/badge.svg
    :target: https://github.com/pimoroni/Pimoroni_CircuitPython_MICS6814/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Driver for the MICS6814 Gas sensor


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Usage Example
=============

.. code-block:: python

    import time
    import analogio
    import digitalio
    import board
    from pimoroni_mics6814 import Pimoroni_MICS6814

    PIN_NH3 = analogio.AnalogIn(board.A0)
    PIN_RED = analogio.AnalogIn(board.A1)
    PIN_OX = analogio.AnalogIn(board.A2)
    PIN_ENABLE = digitalio.DigitalInOut(board.A4)

    MICS6814 = Pimoroni_MICS6814(PIN_OX, PIN_RED, PIN_NH3, PIN_ENABLE)

    while True:
        print(MICS6814.read_all())
        time.sleep(1.0)


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/pimoroni/Pimoroni_CircuitPython_MICS6814/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
