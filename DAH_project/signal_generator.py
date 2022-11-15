import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.signal as signal

OUTPUT_RATE= 44100
MAX_AMPLITUDE= np.iinfo(np.int16).max
ATTACK_DECAY_LENGTH= int(5000/2)

def create_hann_window():
    window= np.hanning(2*ATTACK_DECAY_LENGTH)
    return window[:ATTACK_DECAY_LENGTH-1], window[ATTACK_DECAY_LENGTH:]
        

def sine_wave(pitch, volume, duration):
    
    global OUTPUT_RATE, MAX_AMPLITUDE

    total_samples= int(OUTPUT_RATE*duration)
    t= np.linspace(0, duration, OUTPUT_RATE, endpoint=True)
    amplitude= int(MAX_AMPLITUDE*volume)
    
    window_left, window_right= create_hann_window()
    output_buffer= np.zeros( (total_samples, 2), dtype= np.int16)
    signal_array= amplitude*signal.chirp(t, f0=pitch, t1= total_samples, f1= 3*pitch)
    signal_array[:ATTACK_DECAY_LENGTH-1]= signal_array[:ATTACK_DECAY_LENGTH-1]* window_left
    signal_array[total_samples-ATTACK_DECAY_LENGTH:total_samples]= signal_array[total_samples-ATTACK_DECAY_LENGTH:total_samples] * window_right

    for i in range(total_samples):
        output_buffer[i][0]= output_buffer[i][1]= signal_array[i]
        

    return output_buffer

def sawtooth_wave(pitch, volume, duration):
    
    global OUTPUT_RATE, MAX_AMPLITUDE

    total_samples= int(OUTPUT_RATE*duration)
    t= np.linspace(0, duration, OUTPUT_RATE, endpoint=True)
    amplitude= int(MAX_AMPLITUDE*volume)
    
    window_left, window_right= create_hann_window()
    output_buffer= np.zeros( (total_samples, 2), dtype= np.int16)
    signal_array= amplitude*signal.sawtooth(2*np.pi*pitch*t)
    signal_array[:ATTACK_DECAY_LENGTH-1]= signal_array[:ATTACK_DECAY_LENGTH-1]* window_left
    signal_array[total_samples-ATTACK_DECAY_LENGTH:total_samples]= signal_array[total_samples-ATTACK_DECAY_LENGTH:total_samples] * window_right
    
    for i in range(total_samples):
        output_buffer[i][0]= output_buffer[i][1]= signal_array[i]
        
    return output_buffer

def square_wave(pitch, volume, duration):
    
    global OUTPUT_RATE, MAX_AMPLITUDE

    total_samples= int(OUTPUT_RATE*duration)
    t= np.linspace(0, duration, OUTPUT_RATE, endpoint=True)
    amplitude= int(MAX_AMPLITUDE*volume)
    
    window_left, window_right= create_hann_window()
    output_buffer= np.zeros( (total_samples, 2), dtype= np.int16)
    signal_array= amplitude*signal.square(2*np.pi*pitch*t)
    signal_array[:ATTACK_DECAY_LENGTH-1]= signal_array[:ATTACK_DECAY_LENGTH-1]* window_left
    signal_array[total_samples-ATTACK_DECAY_LENGTH:total_samples]= signal_array[total_samples-ATTACK_DECAY_LENGTH:total_samples] * window_right
    
    for i in range(total_samples):
        output_buffer[i][0]= output_buffer[i][1]= signal_array[i]
        

    return output_buffer

def triangle_wave(pitch, volume, duration):
    
    global OUTPUT_RATE, MAX_AMPLITUDE

    total_samples= int(OUTPUT_RATE*duration)
    t= np.linspace(0, duration, OUTPUT_RATE, endpoint=True)
    amplitude= int(MAX_AMPLITUDE*volume)
    
    window_left, window_right= create_hann_window()
    output_buffer= np.zeros( (total_samples, 2), dtype= np.int16)
    signal_array= amplitude*signal.sawtooth(2*np.pi*pitch*t, 0.5)
    signal_array[:ATTACK_DECAY_LENGTH-1]= signal_array[:ATTACK_DECAY_LENGTH-1]* window_left
    signal_array[total_samples-ATTACK_DECAY_LENGTH:total_samples]= signal_array[total_samples-ATTACK_DECAY_LENGTH:total_samples] * window_right
    
    for i in range(total_samples):
        output_buffer[i][0]= output_buffer[i][1]= signal_array[i]
        

    return output_buffer

def noise_wave(pitch, volume, duration):
    
    total_samples= int(OUTPUT_RATE*duration)
    t= np.linspace(0, duration, OUTPUT_RATE, endpoint=True)
    amplitude= int(MAX_AMPLITUDE*volume)

    window_left, window_right= create_hann_window()
    output_buffer= np.zeros( (total_samples, 2), dtype= np.int16)
    signal_array= amplitude*np.random.normal(0,0.5, total_samples)
    signal_array[:ATTACK_DECAY_LENGTH-1]= signal_array[:ATTACK_DECAY_LENGTH-1]* window_left
    signal_array[total_samples-ATTACK_DECAY_LENGTH:total_samples]= signal_array[total_samples-ATTACK_DECAY_LENGTH:total_samples] * window_right

    for i in range(total_samples):
        output_buffer[i][0]= output_buffer[i][1]= signal_array[i]

    return output_buffer
    
def main():
    trig_wave= noise_wave(500, 0.5, 0.5)
    plt.plot(trig_wave.T[0][:])
    plt.show()

    
if __name__ == '__main__':
    main()
    
