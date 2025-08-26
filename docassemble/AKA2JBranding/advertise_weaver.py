# pre-load
import os
from docassemble.base.util import log

try:
    from docassemble.ALWeaver.custom_values import advertise_capabilities
    if not os.environ.get('ISUNITTEST'):
        advertise_capabilities(__name__, minimum_version="1.5")

except ImportError:
    log("Not advertising capabilities because ALWeaver is not installed.")