# -*- coding: utf-8 -*-
"""Module for controlling GPIOs of Orange Pi microcomputers.

- The library **orangepi_PC_gpio_pyH3** should be installed from:
  https://github.com/duxingkei33/orangepi_PC_gpio_pyH3.
- If the library is not installed, the library simulator is used with the same
  interface.
- For controlling in-built LEDs their control at the operating system level
  should be set to `None`.
- 

"""
__version__ = "0.9.0"
__status__ = "Beta"
__author__ = "Libor Gabaj"
__copyright__ = "Copyright 2018-2019, " + __author__
__credits__ = ["https://github.com/duxingkei33"]
__license__ = "MIT"
__maintainer__ = __author__
__email__ = "libor.gabaj@gmail.com"


import logging
from typing import NoReturn
from . import gpio, port, connector


def pinmap(func):
    """Decorator for mapping and checking a GPIO pin."""
    def _decorator(self, pin: str):
        if pin in dir(port):
            port_num = getattr(port, pin)
        elif pin in dir(connector):
            port_num = getattr(connector, pin)
        else:
            port_num = None
            errmsg = f'Unknown {pin=}'
            self._logger.error(errmsg)
        if port_num:
            return func(self, port_num)
    return _decorator


###############################################################################
# Classes
###############################################################################
class OrangePiOne(object):
    """Creating a GPIO manager for microcomputer ``Orange Pi One``.

    Notes
    -----
    - GPIO pins including system LEDs are identified for the sake of this class
      by name of its attributes defined in the library.
    - Each pin can be named in the form as a ``port`` or as a ``connector``.
      Each form has its own list of available pin names, which can be obtained
      with commands::

          dir(port)
          dir(connector)

    - List of available ports for GPIO pins:
      ``PA0``, ``PA1``, ``PA10``, ``PA11``, ``PA12``, ``PA13``, ``PA14``,
      ``PA18``, ``PA19``, ``PA2``, ``PA20``, ``PA21``, ``PA3``, ``PA6``,
      ``PA7``, ``PA8``, ``PA9``, ``PC0``, ``PC1``, ``PC2``, ``PC3``, ``PC4``,
      ``PC7``, ``PD14``, ``PG6``, ``PG7``, ``PG8``, ``PG9``

    - List of available ports for system LEDS:
      ``POWER_LED``, ``STATUS_LED``

    - List of available connectors for GPIO pins:
      ``gpio1p10``, ``gpio1p11``, ``gpio1p12``, ``gpio1p13``, ``gpio1p15``,
      ``gpio1p16``, ``gpio1p18``, ``gpio1p19``, ``gpio1p21``, ``gpio1p22``,
      ``gpio1p23``, ``gpio1p24``, ``gpio1p26``, ``gpio1p27``, ``gpio1p28``,
      ``gpio1p29``, ``gpio1p3``, ``gpio1p31``, ``gpio1p32``, ``gpio1p33``,
      ``gpio1p35``, ``gpio1p36``, ``gpio1p37``, ``gpio1p38``, ``gpio1p40``,
      ``gpio1p5``, ``gpio1p7``, ``gpio1p8``

    - List of available connectors for system LEDS:
      ``LEDp1``, ``LEDp2``

    """

    def __init__(self):
        """Create the class instance - constructor."""
        # Hardware initialization
        gpio.init()
        # Logging
        self._logger = logging.getLogger(' '.join([__name__, __version__]))
        self._logger.debug(
            f'Instance of "{self.__class__.__name__}" created: {self}')

    def __str__(self):
        """Represent instance object as a string."""
        return self.__class__.__name__

    def __repr__(self) -> str:
        """Represent instance object officially."""
        msg = f'{self.__class__.__name__}()'
        return msg

    @pinmap
    def pin_on(self, pin: str) -> NoReturn:
        """Set pin as OUTPUT and to HIGH."""
        gpio.setcfg(pin, gpio.OUTPUT)
        gpio.output(pin, gpio.HIGH)

    @pinmap
    def pin_off(self, pin: str) -> NoReturn:
        """Set pin as OUTPUT and to LOW."""
        gpio.setcfg(pin, gpio.OUTPUT)
        gpio.output(pin, gpio.LOW)

    def pin_toggle(self, pin: str) -> NoReturn:
        """Set pin as OUTPUT and invert its state."""
        if self.is_pin_on(pin):
            self.pin_off(pin)
        else:
            self.pin_on(pin)

    @pinmap
    def pin_pullup(self, pin: str) -> NoReturn:
        """Set PULLUP of pin."""
        gpio.pullup(pin, gpio.PULLUP)

    @pinmap
    def pin_pulldown(self, pin: str) -> NoReturn:
        """Set PULLDOWN of pin."""
        gpio.pullup(pin, gpio.PULLDOWN)

    @pinmap
    def pin_pullclear(self, pin: str) -> NoReturn:
        """Reset PULLUP or PULLDOWN of pin."""
        gpio.pullup(pin, gpio.PULLNONE)

    @pinmap
    def pin_read(self, pin: str) -> int:
        """Set pin as INPUT and read its state."""
        gpio.setcfg(pin, gpio.INPUT)
        return gpio.input(pin)

    @pinmap
    def pin_state(self, pin: str) -> int:
        """Return pin state without changing its mode."""
        return gpio.input(pin)

    @pinmap
    def is_pin_on(self, pin: str) -> bool:
        """Return flag about pin state HIGH."""
        return gpio.input(pin) == gpio.HIGH

    def is_pin_off(self, pin: str) -> bool:
        """Return flag about pin state LOW."""
        return not self.is_pin_on(pin)

    def is_pin_output(self, pin: str) -> bool:
        """Return flag about pin mode OUTPUT."""
        return self.pin_state(pin) == gpio.OUTPUT

    def is_pin_input(self, pin: str) -> bool:
        """Return flag about pin mode INPUT."""
        return self.pin_state(pin) == gpio.INPUT
