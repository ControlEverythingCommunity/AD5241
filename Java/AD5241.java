// Distributed with a free-will license.
// Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
// AD5241
// This code is designed to work with the AD5241_I2CPOT_10K I2C Mini Module available from ControlEverything.com.
// https://www.controleverything.com/content/Potentiometers?sku=AD5241_I2CPOT_10K#tabs-0-product_tabset-2

import com.pi4j.io.i2c.I2CBus;
import com.pi4j.io.i2c.I2CDevice;
import com.pi4j.io.i2c.I2CFactory;
import java.io.IOException;

public class AD5241
{
	public static void main(String args[]) throws Exception
	{
		// Create I2C bus
		I2CBus Bus = I2CFactory.getInstance(I2CBus.BUS_1);
		// Get I2C device, AD5241 I2C address is 0x2C(44)
		I2CDevice device = Bus.getDevice(0x2C);

		// Send command byte
		// Input resistance value, 0x80(128)
		device.write(0x00, (byte)0x80);
		Thread.sleep(500);

		// Convert the data
		byte data = (byte)device.read();
		double resistance = ((data & 0xFF) / 256.0) * 10.0;

		// Output data to screen
		System.out.printf("Resistance %.2f K", resistance);
	}
}