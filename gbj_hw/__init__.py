# -*- coding: utf-8 -*-
"""Initial module importing all library modules of the package."""
try:
    from pyA20.gpio import gpio
    from pyA20.gpio import port
    from pyA20.gpio import connector
except ModuleNotFoundError:
    from simulators.pyA20.gpio import gpio
    from simulators.pyA20.gpio import port
    from simulators.pyA20.gpio import connector
from . import orangepi

