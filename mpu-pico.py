import adafruit_mpu6050
import board
import busio

i2c = busio.I2C(board.GP15, board.GP14)
mpu = adafruit_mpu6050.MPU6050(i2c)

//
  //mpu.acceleration
  //mpu.gyro
  //mpu.temperature
//

while True:
  println()
