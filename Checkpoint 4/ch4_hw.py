"""
A script that will request for the numerical reperestation of a binary number that
be output as a signal though an I2C bus in order to light 4 LEDs. When a button is pressed, 
the output patten used to light the LEDs will be multipieed by a different power of 2. 
"""

import time
from DAH import PCF8574
import numpy as np

def init_parameters():
	"""
	Initial parametes for loop
	"""
	i=0						# Init index value 
	button= False			# Init value of signal from button
	x= np.array([1,2,4,16])	# Array with the powers of 2 that the original signal will be multiplied by 
	
	return i,button,x

def run_loop(pcf, choice,switch0):
	
	"""
	Function will send the desired binary singal theought the pcf and the send a 
	binary signal to turn off all LEds in a loop.
	When a button is pressed, the numerical value of the desired binary output signal will be multiplied by
	by a power of 2. This is done by keping all the multipliers in an array, and changing the index of the 
	multiplier array when the button ids pressed.
	"""
	
	i,button,x= init_parameters()
	
	while True:
		
		while pcf.digitalRead(switch0) == True:		# Loop that will only run when there is a positive signal coming from the button's circuit
			i+= 1									# Increase the multiplier array's index by one
			time.sleep(0.2)
		if i>x.shape[0]-1:							
			i=0										# Reset the multiplier back to 1   
		pcf.portWrite(choice*x[i])					# Write the signal (takin ginto account multiplier) to the I2C
		time.sleep(0.1)
		pcf.portWrite(15)							# Write a signal to the I2C to turn opff all LEDs
		time.sleep(0.1)
	return

def main():
	pcf= PCF8574(address=0x38)						# Initialize the PCF8574 class
	switch0= 5										# Pin number the button circuit is connected to.		
	choice= int(input('Add base number: '))			# Numerical value of the base binary output signal
	run_loop(pcf, choice, switch0)					# Run the loop funtion to start the LED blinking pattern.   
	
	return 
main()      

