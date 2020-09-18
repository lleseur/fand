============
Installation
============

Python dependencies
===================

Server
------

 - pySMART (homepage__, pypi__): access drives SMART data
 - psutil (homepage__, pypi__): access CPU temperatures

__ https://github.com/freenas/py-SMART
__ https://pypi.org/project/pySMART/
__ https://github.com/giampaolo/psutil
__ https://pypi.org/project/psutil/

Raspberry Pi client
-------------------

 - gpiozero (homepage__, pypi__): access GPIO for PWM and tachometer signals
 - gpiozero's native pin factory does not currently supports PWM (sept 2020),
   you need one of the following packages:

    - RPi.GPIO (homepage__, pypi__): does not supports hardware PWM,
      only uses software PWM
    - pigpio (homepage__, pypi__, github__): supports hardware PWM
      but cannot work with Linux's lockdown LSM
    - RPIO (homepage__, pypi__): unmaintained

__ https://github.com/gpiozero/gpiozero
__ https://pypi.org/project/gpiozero/
__ https://sourceforge.net/projects/raspberry-gpio-python/
__ https://pypi.org/project/RPi.GPIO/
__ http://abyz.me.uk/rpi/pigpio/python.html
__ https://pypi.org/project/pigpio/
__ https://github.com/joan2937/pigpio
__ https://github.com/metachris/RPIO
__ https://pypi.org/project/RPIO/

Non-Python dependencies
=======================

Server
------

- smartmontools_: pySMART's backend

.. _smartmontools: https://www.smartmontools.org/

Installation
============

Server
------

Install smartmontools on your system with your prefered package manager.

Install fand with:

.. code-block:: console

   $ pip install fand[server]

Raspberry Pi client
-------------------

Install fand with one of the following commands:

 - Install with RPi.GPIO:

   .. code-block:: console

      $ pip install fand[clientrpi-rpi-gpio]

 - Install with pigpio:

   .. code-block:: console

      $ pip install fand[clientrpi-pigpio]

 - Install with RPIO:

   .. code-block:: console

      $ pip install fand[clientrpi-rpio]

Other modules
-------------

No extra dependencies required, you can install with:

.. code-block:: console

   $ pip install fand

Custom installation
-------------------

You can cumulate extra dependencies:

.. code-block:: console

   $ pip install fand[server,clientrpi-pigpio]

Python version support
======================

Officially supported Python versions
------------------------------------

fand should support any Python 3 version supported by upstream_.

 - Python 3.6
 - Python 3.7
 - Python 3.8

.. _upstream: https://www.python.org/downloads/

Officially supported Python implementations
-------------------------------------------

 - CPython_
 - PyPy_

.. _CPython: https://www.python.org/
.. _PyPy: https://www.pypy.org/

Operating system support
========================

Server
------

 - Linux
 - FreeBSD
 - Windows: untested, missing support for CPU temperature monitoring
   (:func:`psutil.sensors_temperatures` does not supports Windows)

Raspberry Pi client
-------------------

 - Linux
 - Windows: untested
 - FreeBSD: unsupported, missing support for any of the gpiozero's
   backend for PWM

Other modules
-------------

 - Any OS with Python
