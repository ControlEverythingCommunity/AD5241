# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# AD5241
# This code is designed to work with the AD5241_I2CPOT_10K I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Potentiometers?sku=AD5241_I2CPOT_10K#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# AD5241 address, 0x2C(44)
# Send command byte, 0x00(00)
#		0x80(128)	Input resistance value
bus.write_i2c_block_data(0x2C, 0x00, [0x80])

time.sleep(0.5)

# AD5241 address, 0x2C(44)
# Read data back from 0x00(00), 1 byte
data = bus.read_byte_data(0x2C, 0x00)

# Convert the data
resistance = (data / 256.0 ) * 10.0

# Output data to screen
print "Resistance : %.2f K" %resistance
