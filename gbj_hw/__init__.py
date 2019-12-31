# -*- coding: utf-8 -*-
"""Initial module importing all library modules of the package."""
try:
    from pyA20.gpio import gpio, port, connector
except ModuleNotFoundError:
    from simulators.pyA20.gpio import gpio
    from simulators.pyA20.gpio.port import port
    from simulators.pyA20.gpio.connector import connector
from . import orangepi

