"""Simple daemon to control fan speed"""

__author__ = 'Louis Leseur'
__email__ = 'louis.leseur@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2020 Louis Leseur'
__url__ = 'https://github.com/lleseur/fand'
__version__ = '0.1.0'

import logging

logging.basicConfig(
    format='%(levelname)s:%(name)s: %(message)s',
    level=logging.NOTSET,
)

# Workaround pySMART bug with Python 3.8 logging API
# Keep until pySMART's next release
try:
    import pySMART

    class _WrapperPysmartLogger(pySMART.utils.TraceLogger):
        def findCaller(self, stack_info=False, stacklevel=1):
            return super().findCaller(stack_info)

    if logging.getLoggerClass() == pySMART.utils.TraceLogger:
        logging.setLoggerClass(_WrapperPysmartLogger)
except ImportError:
    pass
