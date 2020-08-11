# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 Philip Howard, written for Pimoroni Ltd
#
# SPDX-License-Identifier: MIT
"""
`pimoroni_mics6814`
================================================================================

Driver for the MICS6814 Gas sensor


* Author(s): Philip Howard

Implementation Notes
--------------------

**Hardware:**

* Pimoroni Enviro+ FeatherWing:
  https://shop.pimoroni.com/products/enviro-plus-featherwing

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""

import digitalio
import analogio


__version__ = "0.0.1"
__repo__ = "https://github.com/pimoroni/Pimoroni_CircuitPython_MICS6814.git"


class MICS6814Reading:
    """Stores a single MICS6814 gas reading."""

    __slots__ = "oxidising", "reducing", "nh3"

    def __init__(self, ox, red, nh3):
        self.oxidising = ox
        self.reducing = red
        self.nh3 = nh3

    def __repr__(self):
        fmt = """Oxidising: {ox:05.03f} Ohms
Reducing: {red:05.03f} Ohms
NH3: {nh3:05.03f} Ohms"""
        return fmt.format(ox=self.oxidising, red=self.reducing, nh3=self.nh3)

    __str__ = __repr__


class Pimoroni_MICS6814:
    """Driver for the MICS6814 gas sensor."""

    def __init__(self, ox_pin, red_pin, nh3_pin, enable_pin=None):
        self._enable_pin = None
        if enable_pin is not None:
            self._enable_pin = digitalio.DigitalInOut(enable_pin)
            self._enable_pin.direction = digitalio.Direction.OUTPUT
            self._enable_pin.value = True
        self._ox_adc = analogio.AnalogIn(ox_pin)
        self._red_adc = analogio.AnalogIn(red_pin)
        self._nh3_adc = analogio.AnalogIn(nh3_pin)

    def read_all(self):
        """Return gas resistance for oxidising, reducing and NH3"""
        try:
            oxidizing = 56000 / ((65535 / self._ox_adc.value) - 1)
        except ZeroDivisionError:
            oxidizing = 0

        try:
            reducing = 56000 / ((65535 / self._red_adc.value) - 1)
        except ZeroDivisionError:
            reducing = 0

        try:
            nh3 = 56000 / ((65535 / self._nh3_adc.value) - 1)
        except ZeroDivisionError:
            nh3 = 0

        return MICS6814Reading(oxidizing, reducing, nh3)

    @property
    def oxidising(self):
        """Gas resistance for oxidising gases.
        Eg chlorine, nitrous oxide
        """
        return self.read_all().oxidising

    @property
    def reducing(self):
        """Gas resistance for reducing gases.
        Eg hydrogen, carbon monoxide
        """
        return self.read_all().reducing

    @property
    def nh3(self):
        """Gas resistance for nh3/ammonia"""
        return self.read_all().nh3

    def read_oxidising(self):
        """Return gas resistance for oxidising gases.
        Eg chlorine, nitrous oxide
        """
        return self.read_all().oxidising

    def read_reducing(self):
        """Return gas resistance for reducing gases.
        Eg hydrogen, carbon monoxide
        """
        return self.read_all().reducing

    def read_nh3(self):
        """Return gas resistance for nh3/ammonia"""
        return self.read_all().nh3
