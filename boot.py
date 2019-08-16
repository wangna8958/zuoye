
# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

import gc

import os

#import webrepl

#webrepl.start()

gc.collect()
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ZTE-221', '0123456789@jiaxing')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
do_connect()



