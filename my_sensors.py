import 
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