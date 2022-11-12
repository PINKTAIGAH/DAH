import numpy as np
import pygame, time, lcd
from DAH import PCF8574
from DAH import MCP23S17
from signal_generator import *

pcf= PCF8574(address= 0x38)
mcp= MCP23S17(chip= 0, address= 0x20)
BUTTON0= 0
BUTTON1= 1
DURATION= 0.3
VOLUME= 0.2
OUTPUT_RATE= 44100
MAX_AMPLITUDE= np.iinfo(np.int16).max
WAVEFORM= ['SINE', 'SAWTOOTH', 'TRIANGLE', 'SQUARE']

frequency= 500


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

def main():
	i=0
	clear_screen()
	waveform_index= np.arange(0,4)
	
	while True:
		
		lcd.lcd_string(f'Freq. : {frequency} Hz', lcd.LCD_LINE_1)
		lcd.lcd_string(f'{WAVEFORM[waveform_index[i]]}', lcd.LCD_LINE_2)
		
		if mcp.digitalRead(BUTTON0)== False:
			note= create_wave(frequency, waveform_index[i])
			note.play()
			time.sleep(0.3)
		
		elif mcp.digitalRead(BUTTON1)== False:
			i+=1
			time.sleep(0.5)
			
			if i==4:
				i=0			

if __name__ == '__main__':
	
	try:
		main()
	except KeyboardInterrupt:
		pass
	finally:
		clear_screen()
		lcd.GPIO.cleanup()

