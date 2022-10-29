import time
from DAH import PCF8574
import numpy as np

pcf= PCF8574(address=0x38)
pcf.portWrite(15)
