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

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-mics6814/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-mics6814

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-mics6814

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-mics6814

Usage Example
=============

.. code-block:: python

    import time
    from pimoroni_mics6814 import Pimoroni_MICS6814

    while True:
        time.sleep(1.0)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/pimoroni/Pimoroni_CircuitPython_MICS6814/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.