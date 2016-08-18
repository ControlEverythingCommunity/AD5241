# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# AD5241
# This code is designed to work with the AD5241_I2CPOT_10K I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Potentiometers?sku=AD5241_I2CPOT_10K#tabs-0-product_tabset-2

from OmegaExpansion import onionI2C
import time

# Get I2C bus
i2c = onionI2C.OnionI2C()

# AD5241 address, 0x2C(44)
# Send command byte, 0x00(00)
#		0x80(128)	Input resistance value
data = [0x80]
i2c.writeBytes(0x2C, 0x00, data)

time.sleep(0.5)

# AD5241 address, 0x2C(44)
# Read data back from 0x00(00), 1 byte
data = i2c.readBytes(0x2C, 0x00, 1)

# Convert the data
resistance = (data[0] / 256.0 ) * 10.0

# Output data to screen
print "Resistance : %.2f K" %resistance
