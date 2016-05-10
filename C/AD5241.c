// Distributed with a free-will license.
// Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
// AD5241
// This code is designed to work with the AD5241_I2CPOT_10K I2C Mini Module available from ControlEverything.com.
// https://www.controleverything.com/content/Potentiometers?sku=AD5241_I2CPOT_10K#tabs-0-product_tabset-2

#include <stdio.h>
#include <stdlib.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <fcntl.h>

void main() 
{
	// Create I2C bus
	int file;
	char *bus = "/dev/i2c-1";
	if((file = open(bus, O_RDWR)) < 0) 
	{
		printf("Failed to open the bus. \n");
		exit(1);
	}
	// Get I2C device, AD5241 I2C address is 0x2C(44)
	ioctl(file, I2C_SLAVE, 0x2C);

	// Send Start Command(0x00)
	// Input resistance value(0x80)
	char config[2] = {0};
	config[0] = 0x00;
	config[1] = 0x80;
	write(file, config, 2);
	sleep(1);

	// Read 1 bytes of data from the register(0x00)
	// data
	char data[1] = {0};
	if(read(file, data, 1) != 1)
	{
		printf("Erorr : Input/output Erorr \n");
	}
	else
	{
		// Convert the data
		float resistance = (data[0] / 256.0) * 10.0;

		// Output data to screen
		printf("Resistance : %.2f K \n", resistance);
	}
}