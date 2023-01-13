from my_sensors import  Accelerometer, gyro, GPS
import numpy as np

#get all the dummy data
time = np.arange(10)
acc_data = np.random.randint(-10,10,10)
gyro_data = np.random.randint(-15,15,10)
gps_data = np.random.randint(-12,12,10)
