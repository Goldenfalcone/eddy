#!/usr/bin/python

#robogaia.com
# the temperatures are in fahrenheit
# temperature_hysteresis sets how low the temperature
#goes until the heater starts

import smbus
import time
import datetime
from subprocess import call
import sys
import ignitionlcd
import RPi_I2C_driver

bus = smbus.SMBus(1)
lcd = RPi_I2C_driver.lcd()

#I2C addres

address = 0x4d
#this will tell how low will go until the heater starts again below the set point
temperature_hysteresis = 4
isHeating = True
  
def get_fahrenheit_val(): 
	data = bus.read_i2c_block_data(address, 1,2)
	val = (data[0] << 8) + data[1]
	return val/5.00*9.00/5.00+32.00
def get_celsius_val(): 
	data = bus.read_i2c_block_data(address, 1,2)
	val = (data[0] << 8) + data[1]
	return val/5.00
temperature =get_fahrenheit_val() 
   
def set_ignite():
	print "ignition"
	ignitionlcd.ignitiondisplay()
	call(["temp_relay_on", "cold"])
        call(["temp_relay_on", "hot"])
	
def set_hot():
	print "heating"
	lcd.lcd_display_string("Current Temp:" + "" +str(temperature)+"F", 1)
	lcd.lcd_display_string("Cooking Temp:"+"" +str(set_point)+"F", 2)
	call(["temp_relay_on", "hot"])
	time.sleep(18)
	call(["temp_relay_off", "hot"])
	time.sleep(115)
		
	
def set_close():
	print "hold"
	call(["temp_relay_off", "cold"])
	call(["temp_relay_off", "hot"])	
	


def main(argv):

	if len (sys.argv) < 2 :
		print "Usage: temperature_hold  [temperature] "
		sys.exit (1)	
	set_point=sys.argv[1]
	try:
		set_point=float(sys.argv[1])
	except ValueError:
		print "the argument is not a number"
		sys.exit (1)
	print "set point =" , set_point
	print "temperature hysteresis =" , temperature_hysteresis
        #starts auger and igniter
        set_ignite()
        time.sleep(420)
        ignitionlcd.litdisplay()

	#main loop
	while 1 == 1:
	    #get the temperature from sensor
		temperature =get_fahrenheit_val()
		#uncomment this for celsius
		#temperature = get_celsius_val()
		print temperature
		
		#Heating loop
		if temperature  <= (set_point- temperature_hysteresis):
                        set_hot()
			isHeating = True
		elif isHeating == True and temperature  <= set_point:
   		    set_hot()
		else:
			lcd.lcd_display_string("Current Temp:" + "" +str(temperature)+"F", 1)
                        lcd.lcd_display_string("Cooking Temp:"+"" +str(set_point)+"F", 2)
                        lcd.lcd_display_string("holding", 3)
			print "hold"
		time.sleep(1)

if __name__ == "__main__":
	main(sys.argv[1:])
