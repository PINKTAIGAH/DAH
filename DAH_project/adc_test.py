from DAH import MCP3208,PCF8574,MCP23S17
import time
from lcd import *

CHANNELS= 3
ADC_CHIP= 1
MAX_FREQ= 2000
MAX_TIME= 5
ADC= MCP3208(chip= ADC_CHIP)
PCF= PCF8574(address= 0x38)
MCP= MCP23S17(chip= 0, address= 0x20)
BUTTON_CHANGE= 0
BUTTON_WAVE= 1
WAVEFORM= ['SINE', 'SAWTOOTH', 'TRIANGLE', 'SQUARE', 'NOISE']
BUTTON_NUMBER= 11

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

def find_pot_value(adc_reading):
	adc_reading[0]= int(adc_reading[0]*MAX_FREQ)
	adc_reading[1]= round(adc_reading[1],2)
	adc_reading[2]= round(adc_reading[2]*MAX_TIME,2)
	return adc_reading

def check_exit_state():
	result= None
	if PCF.digitalRead(BUTTON_CHANGE)==0:
		result= False
	else:
		result= True
	return result

def check_waveform_state(i):
    if PCF.digitalRead(BUTTON_WAVE)==0:
        i+=1
        time.sleep(0.5)
        if i==5:
            i=0
    return i		

def poll_potentiometer():
	adc_reading_float= [round(ADC.analogReadFloat(channel= i),3) for i in range(CHANNELS)]
	adc_reading_value= find_pot_value(adc_reading_float)
	return adc_reading_value

def buttons_pressed(port_state):
    index= []
    for i, _ in enumerate(port_state):
        
        if port_state[i]== 0:
            index.append(i)
    return(index)
3
def poll_buttons():
	port_state= bin(MCP.portRead())[2:].zfill(BUTTON_NUMBER)
	port_state= [int(x) for x in str(port_state)]
	port_state= port_state[::-1]
	down_state= buttons_pressed(port_state)
	print(down_state)
	return down_state
	
def button_customize(button_param):
	time.sleep(1)
	selected_button_index= None
	waveform_index= 0
	running= None
	while True:
		time.sleep(1)
		polled_param= poll_potentiometer()
		waveform_index= check_waveform_state(waveform_index)
		selected_button_index= poll_buttons() 
		print(selected_button_index)
		click= check_exit_state()
		print(list((waveform_index, *polled_param)))
		if click== False:
			button_param[selected_button_index[0]]= (waveform_index, *polled_param)
			break
		time.sleep(0.05)

	return button_param
				
def main():
	button_param= [None for x in range(BUTTON_NUMBER)]
	while True:
		if PCF.digitalRead(BUTTON_CHANGE)== 0:
			button_param= button_customize(button_param)
		print('button param:')
		print(button_param)
		time.sleep(0.2)
		
if __name__== '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
	finally:
		print('program Terminated')
