"""
A script that will take readings from an ADC of an ocilating signal from a power generatior 
from an ADC. This script will then calculate the sampling frequency of the ADC and plot a 
graph of the signal voltage over time.  
"""
import time
import numpy as np
import matplotlib.pyplot as plt
from DAH import MCP3208

ADC0= MCP3208(0)        # Define ADC as SPI chip 0 (CO0/GPIO08)
ADC_input= []           # Empty list for the 
Sample_size=200         # Number of voltage samples the ADC will take 
x=0                     
t_1= time.time()        # Time prior to soltage samples being taken 
while x<= Sample_size:  # Loop untill desired number of samples have been taken                                       
	ADC_input.append(ADC0.analogReadVolt(0)) # read channel 0 of ADC and append to list
	x+=1

t_2= time.time()        # Time after samples have been taken
t_interval= (t_2-t_1)/x # Find the time delta between sampling loop and the time interval between each voltage sample 
t_delta= t_2-t_1
sample_frequency= 1/(t_delta/Sample_size)   # 

t_array= np.arange(0,t_interval*Sample_size + t_interval ,t_interval)   # Create a numpy array  containing the time each voltage rerading was taken relative to the first (starting at t=0)
ADC_input= np.array(ADC_input)  # Convert the voltage reading lint into a numpy array


print('The sampling frequency is '+ str(1/(t_delta/Sample_size)))    # Print sampling frequency of ADC
np.savetxt('V_output.txt',(t_array, ADC_input), delimiter= ',') # Save the time and voltage outpout arrays to a txt file  

"""
This code may produce an error (low probability) where the two numpy arrays differ by one element when sampling voltages with high frequencies
( > 1 KHz ). This is due to the calculated time interval not syncing up with the real time interval (by orders of microseconds).
If this occures, reruning the code will typically result in numpy arrays of equal lengh and for the two arrays to be plotted against eachother
"""