import random as rd
import pandas as pd
import os
from datetime import datetime

def randomSensor1():
    return rd.randint(20, 50)

def randomSensor2():
    return rd.uniform(70, 80)

def randomSensor3():
    return rd.choice(['True', 'False'])

def randomSensor4():
    return rd.randint(1, 10) * 10

sensor1 = randomSensor1()
sensor2 = randomSensor2()
sensor3 = randomSensor3()
sensor4 = randomSensor4()

excel_file = "sensor_data.xlsx"
data = {
    "DateTime": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Sensor 1": [sensor1],
    "Sensor 2": [sensor2],
    "Sensor 3": [sensor3],
    "Sensor 4": [sensor4]
}
df_new = pd.DataFrame(data)

if os.path.exists(excel_file):
    df_existing = pd.read_excel(excel_file)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
else:
    df_combined = df_new

df_combined.to_excel(excel_file, index=False)
