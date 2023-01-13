class Sensor():
    def __init__(self,name,location,record_date):
        self.name=name
        self.location=location
        self.record_date=record_date
        self.data={}

    def add_data(self, data, time):
        self.data["data"]=data
        self.data["time"]=time
        print("Data points added successfully")

    def clear_data(self):
        self.data={}
        print("Data removed successfully")

import numpy as np

sensor1 = Sensor(name="sensor1", location="haldia", record_date="2023-01-09")
data = np.random.randint(-10, 10, 10)
time = np.arange(10)
print(data)
print(time)

sensor1.add_data(data=data ,
          time=time)
print("generic sensor data:" ,sensor1.data)

import numpy as np
acc_data = np.random.randint(-10, 10, 10)
acc_time = np.arange(10)

class accelerometer(Sensor):
    def show_sensor_type(self):
        print(f"This is {self.name}")

acc= accelerometer(
    name="accelerometer",
    location="haldia",
    record_date="2023-01-19"
)

acc.add_data(
    data=acc_data,
    time=acc_time 
)
print('Accelerometer data: ',acc.data)

class gyro(accelerometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and the location is {self.location}")

gyro_data = np.random.randint(-15,15,10)
gyro_time = np.arange(10)

gyro = gyro(
    name="gyroscope",
    location="kolkata",
    record_date="2023-01-10"
)

gyro.add_data(time=gyro_time , data=gyro_data)

acc.show_sensor_type()
gyro.show_sensor_type()

#new code

class GPS(Sensor):
    def __init__(self, name, location,record_date,brand):
        super().__init__(
            name, location,record_date
        )
        self.brand = brand

gps = GPS(
    name="gps",
    location="chennai",
    record_date="2021-01-10",
    brand="samsung"
)
print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)
