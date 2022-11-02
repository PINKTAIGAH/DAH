import numpy as np
import pygame, time
import matplotlib.pyplot as plt

output_rate= 44100
max_amplitude= np.iinfo(np.int16).max
def sine_wave(pitch, volume,duration):
	global output_rate, max_amplitude
	
	total_samples= int(output_rate*duration)
	output_buffer= np.zeros((total_samples, 2), dtype= np.int16)
	
	amplitude= int(max_amplitude*volume)
	
	wave_step= float(pitch/output_rate)*2*np.pi
	
	for i in range(total_samples):
		output_buffer[i][0]= amplitude*np.sin(i*wave_step)
		output_buffer[i][1]= amplitude*np.sin(i*wave_step)
		 
	return output_buffer
	
pygame.mixer.init(frequency= output_rate, channels=2, size= -16)
sin523= sine_wave(523,1,0.5)
plt.plot(sin523[0:100])
plt.show()

note_C5= pygame.mixer.Sound(buffer= sin523)
note_C5.play()
time.sleep(2)
