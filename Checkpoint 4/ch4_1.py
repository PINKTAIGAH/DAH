from DAH import PCF8574
import time

pcf= PCF8574(address=0x38)

LED0=0
pcf.digitalWrite(LED0, True)    # Turn off LED by pulling high 

while True:
    pcf.digitalWrite(LED0, False)
    time.sleep(0.05)
    pcf.digitalWrite(LED0, True)
    time.sleep(0.05)




