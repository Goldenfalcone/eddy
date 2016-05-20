#!/usr/bin/python
#Ignition program for Eddy

import smbus
import time
import datetime
import lcddriver
from subprocess import call
import sys
import os
import ignitionlcd
import litlcd

bus = smbus.SMBus(1)

#I2C address

address = 0x4d

def set_ignite():
    ignitionlcd.ignitiondisplay
    call(["temp_relay_on", "cold"])
    call(["temp_relay_on", "hot"])

def set_lit():
    ignitionlcd.litdisplay
    call(["temp_relay_off", "cold"])
    call(["temp_relay_off", "hot"])
    
count = 0
while count <= 0:
    if count <= 0:
        set_ignite()
        count +=1
        print count

    elif count >= 300:
         set_lit()
    time.sleep(1)
    

    
    
