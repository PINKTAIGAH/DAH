'''
Script that will output a range of preselected voltages through a DAC to power an LED located physically next to an LDR.
Resistance changes of LDR will the read by a LDC and output by this script.
'''
from DAH import MCP3208      # Import DAC and ADC libraries
from DAH import MCP4922
import numpy as np           
import time

def volt_loop(volt_array, ADC0_channel):
    
    '''
    Loops through an array of voltage values and outputs that voltage from a DAC to power an LED.
    For each output voltage, analog signal produced by LDR is read and appended to empty array.
    '''

    ADC_float_array= []                                                      # Empty arrays for both float and voltage ADC readings 
    ADC_volt_array= []
    tick= 0                                                                  # Counter used to keep track of array 

    while tick <= volt_array.size:                                           # Loop through all of volt_array
        DAC1.analogWriteVolt(0, volt_array[tick-1])                          # Output voltage from given array element to DAC  
        ADC_float_array.append(ADC0.analogReadFloat(ADC0_channel))   # Read analog signal from ADC and append them to relevant list
        ADC_volt_array.append(ADC0.analogReadVolt(ADC0_channel))
        time.sleep(1)                                                        # Make script wait 1 second in order for circuit to kep up with signal from raspberry pi   
        tick+= 1

    return ADC_float_array, ADC_volt_array                                   # Return lists containing readings form ADC  

ADC0= MCP3208(chip=0)                                                        # Define ADC as SPI chip 0 (CO0/GPIO08)   
DAC1= MCP4922(chip=1)                                                        # Define DAC as SPI chip 1 (CE1/GPIO07)   
ADC0_channel= 0                                                              # Define ADC channel that LDR is connected to
volt_array= np.linspace(0,3,10)                                              # Create array containing all the voltages that will be output   
float_OP, volt_OP= volt_loop(volt_array, ADC0_channel)                       # Run volt_loop function to return list of ACD readings
print(str(float_OP) + "\n" + str(volt_OP))







