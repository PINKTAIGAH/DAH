import numpy as np
import pygame, time
import matplotlib.pyplot as plt
import scipy.signal as signal

def sine_wave(pitch, volume, duration):
    
    global OUTPUT_RATE, MAX_AMPLITUDE

    total_samples= int(OUTPUT_RATE*duration)
    t= np.linspace(0, duration, OUTPUT_RATE, endpoint=True)
    amplitude= int(MAX_AMPLITUDE*volume)
    
    output_buffer= np.zeros( (total_samples, 2), dtype= np.int16)
    signal_array= amplitude*signal.chirp(t, f0=pitch, t1= total_samples, f1= 3*pitch)
    
    for i in range(total_samples):
        output_buffer[i][0]= output_buffer[i][1]= signal_array[i]
        

    return output_buffer

def sawtooth_wave(pitch, volume, duration):
    
    global OUTPUT_RATE, MAX_AMPLITUDE

    total_samples= int(OUTPUT_RATE*duration)
    t= np.linspace(0, duration, OUTPUT_RATE, endpoint=True)
    amplitude= int(MAX_AMPLITUDE*volume)
    
    output_buffer= np.zeros( (total_samples, 2), dtype= np.int16)
    signal_array= amplitude*signal.sawtooth(2*np.pi*pitch*t)
    
    for i in range(total_samples):
        output_buffer[i][0]= output_buffer[i][1]= signal_array[i]
        

    return output_buffer

def square_wave(pitch, volume, duration):
    
    global OUTPUT_RATE, MAX_AMPLITUDE

    total_samples= int(OUTPUT_RATE*duration)
    t= np.linspace(0, duration, OUTPUT_RATE, endpoint=True)
    amplitude= int(MAX_AMPLITUDE*volume)
    
    output_buffer= np.zeros( (total_samples, 2), dtype= np.int16)
    signal_array= amplitude*signal.square(2*np.pi*pitch*t)
    
    for i in range(total_samples):
        output_buffer[i][0]= output_buffer[i][1]= signal_array[i]
        

    return output_buffer

def triangle_wave(pitch, volume, duration):
    
    global OUTPUT_RATE, MAX_AMPLITUDE

    total_samples= int(OUTPUT_RATE*duration)
    t= np.linspace(0, duration, OUTPUT_RATE, endpoint=True)
    amplitude= int(MAX_AMPLITUDE*volume)
    
    output_buffer= np.zeros( (total_samples, 2), dtype= np.int16)
    signal_array= amplitude*signal.sawtooth(2*np.pi*pitch*t, 0.5)
    
    for i in range(total_samples):
        output_buffer[i][0]= output_buffer[i][1]= signal_array[i]
        

    return output_buffer

OUTPUT_RATE= 44100
MAX_AMPLITUDE= np.iinfo(np.int16).max
pygame.mixer.init(frequency= OUTPUT_RATE, channels=2, size= -16)

sin523= triangle_wave(523,0.5,1)
plt.plot(sin523[0:100])
plt.show()

note_C5= pygame.mixer.Sound(buffer= sin523)
note_C5.play()
time.sleep(2)
