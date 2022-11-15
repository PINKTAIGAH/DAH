import numpy as np
import pygame, time, lcd
from DAH import MCP23S17
from DAH import PCF8574
from signal_generator import *
import time

def clear_screen():
	lcd.lcd_byte(0x01, lcd.LCD_CMD)

def create_wave(frequency, waveform_index):
	if waveform_index == 0:
		wave= sine_wave(frequency, VOLUME, DURATION)
		
	elif waveform_index == 1:
		wave= sawtooth_wave(frequency, VOLUME, DURATION)
		
	elif waveform_index == 2:
		wave= triangle_wave(frequency, VOLUME, DURATION)
		
	elif waveform_index == 3:
		wave= square_wave(frequency, VOLUME, DURATION)
	
	elif waveform_index == 4:
		wave= noise_wave(frequency, VOLUME, DURATION)
	
	note= pygame.mixer.Sound(buffer= wave)
	return note

def buttons_pressed(port_state):
    index= []
    for i, _ in enumerate(port_state):
        
        if port_state[i]== 0:
            index.append(i)
    return(index)

def play_notes(notes):
    for i, individual_note in enumerate (notes):
        individual_note.play()

def check_octave_state(i):
    if pcf.digitalRead(BUTTON_OCTAVE)==0:
        i+=1
        time.sleep(0.5)
        if i==9:
            i=0
    return i

def check_waveform_state(i):
    if pcf.digitalRead(BUTTON_WAVE)==0:
        i+=1
        time.sleep(0.5)
        if i==5:
            i=0
    return i 
                
def main():
    waveform_index, octave_index= 0,0
    while True:
        port_state= bin(mcp.portRead())
        port_state= [int(x) for x in str(port_state[2:])]
        port_state= port_state[::-1]
        down_state= buttons_pressed(port_state[:-2])
        notes= [create_wave(BUTTON_FREQ[octave_index][x],waveform_index) for x in down_state]
        play_notes(notes)
        octave_index= check_octave_state(octave_index)
        waveform_index= check_waveform_state(waveform_index)
        print(f'Waveform : {WAVEFORM[waveform_index]}, Octave: {octave_index}')
        time.sleep(0.05)
    
pcf= PCF8574(address= 0x38)
mcp= MCP23S17(chip= 0, address= 0x20)
O0=[16,17,18,19,21,22,23,25,26,28,29,31]
O1=[33,35,37,39,41,44,46,49,52,55,58,62]
O2=[65,69,73,78,82,87,93,98,104,110,117,123]
O3=[131,139,147,156,165,175,185,196,208,220,233,247]
O4=[262,267,294,311,330,349,370,392,415,440,466,494]
O5=[523,564,587,662,659,698,740,784,831,880,932,988]
O6=[1047,1109,1175,1245,1319,1397,1480,1568,1661,1760,1865,1976]
O7=[2093,2217,2349,2489,2637,2794,2960,3136,3322,3520,3729,3951]
O8=[4186,4435,4699,4978,5274,5588,5920,6272,6645,7040,7459,7902]
BUTTON_FREQ= np.array([O0,O1,O2,O3,O4,O5,O6,O7,O8])
BUTTON_OCTAVE=1
BUTTON_WAVE=0
DURATION= 0.5
VOLUME= 0.5
OUTPUT_RATE= 44100
MAX_AMPLITUDE= np.iinfo(np.int16).max
WAVEFORM= ['SINE', 'SAWTOOTH', 'TRIANGLE', 'SQUARE', 'Noise']

pygame.mixer.init(frequency= OUTPUT_RATE, channels=2, size= -16)



if __name__ == '__main__':
    try :
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd.GPIO.cleanup()
        print('Program Terminated')
        
            



