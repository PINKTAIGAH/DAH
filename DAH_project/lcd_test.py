import lcd
import time
lcd.lcd_init()

lcd.lcd_string('Nisser + Giorgio', lcd.LCD_LINE_1)
lcd.lcd_string('Juntos siempre<3', lcd.LCD_LINE_2)
time.sleep(20)
lcd.lcd_byte(0x01,lcd.LCD_CMD)

lcd.GPIO.cleanup()
