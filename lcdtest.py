import smbus
import time
import datetime
from subprocess import call
import sys
import RPi_I2C_driver
import temperaturehold
import array

lcd = RPi_I2C_driver.lcd()

temperature = temperaturehold.get_fahrenheit_val()
settext = ("Temp:" + str(temperature)+"F")

lcd.lcd_display_string(settext, 1)


