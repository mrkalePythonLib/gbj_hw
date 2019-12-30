**********************
Purpose of the package
**********************
The package ``gbj_hw``contains a set of Python modules for supporting hardware
within python console applications and scripts running usually on
**Pi microcomputers**, e.g., ``Raspberry Pi``, ``Orange Pi``, ``Nano Pi``, etc.

Modules in package
==================
**orangepi**
  Control GPIOs and system LEDs of Orange Pi microcomputers.

  - For ``Orange Pi One`` the library ``pyA20`` is utilized, which was taken
    from GitHub repository
    `orangepi_PC_gpio_pyH3 <https://github.com/duxingkei33/orangepi_PC_gpio_pyH3.git>`_.

**simulators/pyA20**
  Simulate functionality for the real library pyA20 in order to develop
  and tune python code on platforms, e.g., MS Windows, for which there is no
  such a library.
  
