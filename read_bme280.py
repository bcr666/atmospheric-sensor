#!/usr/bin/env python3

import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x77)

#Loop to print data
while True:
	temperatureC = bme280.temperature
	temperatureF = temperatureC*9/5+32
	print("Temperature: %.2f C" % temperatureC)
	print("Temperature: %.2f F" % temperatureF)
	print("Humidity: %.2f %%" % bme280.humidity)
	print("Pressure: %.2f hpa" % bme280.pressure)
	print("-----------------------------")
	time.sleep(5)

