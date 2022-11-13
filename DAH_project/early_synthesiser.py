import numpy as np
import pygame, time, lcd
from DAH import PCF8574
from DAH import MCP23S17
from signal_generator import *

mcp= MCP23S17(chip= 0, address= 0x20)
MCP_BUTTONS= np.array([262, 277, 294, 311, 330, 349, 370, 392])
BUTTON1=1
BUTTON0=0
DURATION= 0.3
VOLUME= 0.5
OUTPUT_RATE= 44100
MAX_AMPLITUDE= np.iinfo(np.int16).max
WAVEFORM= ['SINE', 'SAWTOOTH', 'TRIANGLE', 'SQUARE']



pygame.mixer.init(frequency= OUTPUT_RATE, channels=2, size= -16)
lcd.lcd_init()


def clear_screen():
	lcd.lcd_byte(0x01, lcd.LCD_CMD)

def create_wave(frequency, waveform_index):
	if waveform_index == 0:
		wave= sine_wave(frequency,VOLUME, DURATION)
		
	elif waveform_index == 1:
		wave= sawtooth_wave(frequency,VOLUME, DURATION)
		
	elif waveform_index == 2:
		wave= triangle_wave(frequency,VOLUME, DURATION)
		
	elif waveform_index == 3:
		wave= square_wave(frequency,VOLUME, DURATION)
	
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
        individual_note.plau()
        
def main():
	waveform_index=0
	clear_screen()
	waveform= np.arange(0,4)
	
	while True:
		
		lcd.lcd_string(f'Synthesiser test', lcd.LCD_LINE_1)
		lcd.lcd_string(f'{WAVEFORM[waveform_index]}', lcd.LCD_LINE_2)
		port_state= bin(mcp.portRead())
		port_state= [int(x) for x in str(port_state[2:])]
		port_state= port_state[::-1]
		down_state= buttons_pressed(port_state[:-2])
		print(down_state)
		
		
		'''
		if mcp.digitalRead(BUTTON0)== False:
			note= create_wave(frequency, waveform_index[i])
			note.play()
			time.sleep(0.3)

		if pcf.digitalRead(BUTTON1)== False:
            waveform_index+=1
            time.sleep(0.5)
			
			if waveform_index==4:
				waveform_index=0			
        '''
if __name__ == '__main__':
	
	try:
		main()
	except KeyboardInterrupt:
		pass
	finally:
		clear_screen()
		lcd.GPIO.cleanup()

