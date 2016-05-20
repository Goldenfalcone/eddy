import RPi_I2C_driver
from time import *

lcd = RPi_I2C_driver.lcd()

def ignitiondisplay():
    lcd.lcd_display_string("Hello Bones Brothers", 1)
    lcd.lcd_display_string("Ignition Started", 2)
    lcd.lcd_display_string("Please Wait", 3)
    lcd.lcd_display_string("Set for 7 minutes", 4)

def litdisplay():
    lcd.lcd_display_string("Thank You.", 1)
    lcd.lcd_display_string("We are now ready", 2)
    lcd.lcd_display_string("Have a nice day", 3)
    lcd.lcd_display_string("!!!!!!!!!!!!!!!!!", 4)
