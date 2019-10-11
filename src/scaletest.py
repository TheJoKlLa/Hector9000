#!/usr/bin/env python3
# coding: utf8
##
#	HectorHardware.py		API class for Hector9000 hardware
#
# imports
from __future__ import division

devEnvironment = True

import time
import sys
from HectorConfig import config

# Uncomment to enable debug output.
import logging

if not devEnvironment:
    import RPi.GPIO as GPIO
    from hx711 import HX711

logging.basicConfig(level=logging.DEBUG)


class HectorHardware:

    def __init__(self, cfg):

        self.config = cfg
        if not devEnvironment:
            GPIO.setmode(GPIO.BOARD)

            hx1 = cfg["hx711"]["DAT"]
            hx2 = cfg["hx711"]["CLK"]
            hxref = cfg["hx711"]["ref"]
            self.hx = HX711(dout=hx1, pd_sck=hx2)
            self.hx.set_reading_format("LSB", "MSB")
            self.hx.set_reference_unit(hxref)
            self.hx.reset()
            self.hx.tare()
        print("done")

    def scale_readout(self):
        if not devEnvironment:
            weight = self.hx.get_weight(5)
            print("weight = %.1f" % weight)
        else:
            weight = 0
        return weight

    def scale_tare(self):
        if not devEnvironment:
            self.hx.tare()

if __name__ == "__main__":
    if not devEnvironment:
        hector = HectorHardware(config)
        
        hector.scale_tare()
        while True:
            print(hector.scale_readout())
            sleep(500)

