import time
import serial
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

# Create an MPU9250 instance
mpu = MPU9250(
    address_ak=AK8963_ADDRESS,
    address_mpu_master=MPU9050_ADDRESS_68,  # In case the MPU9250 is connected to another I2C device
    address_mpu_slave=None,
    bus=1,
    gfs=GFS_1000,
    afs=AFS_8G,
    mfs=AK8963_BIT_16,
    mode=AK8963_MODE_C100HZ)

# Configure the MPU9250
mpu.configure()

# Initialize serial communication
ser = serial.Serial('/dev/ttyAMA1', 115200)  # Adjust the serial port and baud rate as needed

while True:
    # Read the accelerometer, gyroscope, and magnetometer values
    accel_data = mpu.readAccelerometerMaster()
    gyro_data = mpu.readGyroscopeMaster()
    mag_data = mpu.readMagnetometerMaster()

    # Prepare the data to be sent via serial
    data = (
        f"{accel_data[0]:.2f}"+ "," +f"{accel_data[1]:.2f}"+ "," +f"{accel_data[2]:.2f}\n"
        
    )

    # Send the data via serial
    ser.write(data.encode())

    # Print the sensor values to the console as well
    print(data)

    # Wait for 1 second before the next reading
    time.sleep(1)
