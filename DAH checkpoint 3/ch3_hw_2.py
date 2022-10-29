"""
This script will read the digital output from an ADC of a square wave voltage source. 
The script will then find the average amximum and minimum f the voltage square wave and 
output them to a txt file.
"""

from unittest.loader import VALID_MODULE_NAME
from DAH import MCP3208
import matplotlib.pyplot as plt
import numpy as np
import time


def find_range(ADC0):
    """
    This function will take a small sample of voltage readings and use them to find and output 
    the voltage range and interval of the square wave.
    """

    Volt_temp= []   # empty array for the voltage readings
    range_sample_size= 20   # Number of readings tro be taken
    
    for i in range(0, range_sample_size):   # Loop to take 20 readings of the voltage source form the Channel 1 of theADC 
        Volt_temp.append(ADC0.analogReadVolt(0))
    
    Volt_interval= (max(Volt_temp) - min(Volt_temp))/2  # Finding the interval (half amplitude) of the square wave
    Volt_range= min(Volt_temp) + Volt_interval  # Finding offset from x-axis (ie: 0V) of the square wave

    return Volt_interval, Volt_range

def find_average__minmax(ADC0, sample_size, Volt_range):
    """
    This function will calculate and output the average maximum and minimum voltage in the square 
    wave of the input source.
    """
    
    Volt_min = []   # Empty array for voltage readings from the troth of the square wave
    Volt_max = []   # Empty array for voltage readings from the peak of the square wave 

    for j in range(0, sample_size): # Loop to take a reading of the voltage source and sort into appropiate array 
        V= ADC0.analogReadVolt(0)

        if V> Volt_range:   # Sort into max array if the voltage reading is above the middle if the square wave
            Volt_max.append(V)
        else:   # Sort into min array if the voltage reading is below the middle if the square wave
            Volt_min.append(V)
    
    Volt_min_average= sum(Volt_min)/len(Volt_min) # Finding the average value of the of the sorted max and min voltage arrays
    Volt_max_average= sum(Volt_max)/len(Volt_max)

    return Volt_min_average, Volt_max_average


def main():
    ADC0= MCP3208(0)
    sample_size=100
    Volt_interval, Volt_range= find_range(ADC0)
    Volt_min_average, Volt_max_average= find_average__minmax(ADC0, sample_size, Volt_range) 
    calibration_points= [Volt_min_average,Volt_max_average]
    np.savetxt("Calibration Data.txt", calibration_points, delimiter=',') # Save average min and max datapoints to atxt file for easy access in future

main()