import numpy as np
import pygame, time
import matplotlib.pyplot as plt
from signal_generator import *


OUTPUT_RATE= 44100
MAX_AMPLITUDE= np.iinfo(np.int16).max
pygame.mixer.init(frequency= OUTPUT_RATE, channels=2, size= -16)

sin523= triangle_wave(523,0.5,1)
plt.plot(sin523[0:100])
plt.show()

note_C5= pygame.mixer.Sound(buffer= sin523)
note_C5.play()
time.sleep(2)
