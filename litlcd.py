import lcddriver
from time import *

lcd = lcddriver.lcd()

lcd.lcd_display_string("Thank You for your patience.", 1)
lcd.lcd_display_string("We are now ready to cook", 2)
lcd.lcd_display_string("Have a nice day", 3)
lcd.lcd_display_string("!!!!!!!!!!!!!!!!!", 4)
