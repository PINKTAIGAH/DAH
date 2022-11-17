import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

LCD_COLUMNS = 16
LCD_ROWS = 2

LCD_RS = digitalio.DigitalInOut(board.D22)
LCD_EN = digitalio.DigitalInOut(board.D17)
LCD_D4 = digitalio.DigitalInOut(board.D25)
LCD_D5 = digitalio.DigitalInOut(board.D24)
LCD_D6 = digitalio.DigitalInOut(board.D23)
LCD_D7 = digitalio.DigitalInOut(board.D18)

def lcd_init():
	lcd = characterlcd.Character_LCD_Mono(LCD_RS, LCD_EN, LCD_D4, LCD_D5,\
	         LCD_D6, LCD_D7, LCD_COLUMNS, LCD_ROWS)
	lcd.clear()
	return lcd
