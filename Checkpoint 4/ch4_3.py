import time
from DAH import PCF8574
import numpy as np

pcf= PCF8574(address=0x38)
switch0= 5
x= np.array([1,2,4,16,32])
choice= int(input('Add base number: '))
button=False
i=0
while True:
	
	while pcf.digitalRead(switch0) == True:
		i+= 1
		time.sleep(0.2)
	if i>x.shape[0]-1:
		i=0
	print(x[i])    
	pcf.portWrite(choice*x[i])
	time.sleep(0.1)
	pcf.portWrite(15)
	time.sleep(0.1)

    
      

