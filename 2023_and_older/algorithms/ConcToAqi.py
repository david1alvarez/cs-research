import math
import requests
import time

# sensor list at https://www.purpleair.com/data.json

def retrieveSensorData(sensorId1, sensorId2, sensorId3, sensorId4):
    response = requests.get(f"https://www.purpleair.com/data.json?show={sensorId1}|{sensorId2}|{sensorId3}|{sensorId4}")
    try:
        sensor = response.json()
    except:
        print("Error: JSON parsing failed.")
        return
    if response.status_code == 200:
        pm25Concentration = 0
        for sensor in list(sensor["data"]):
            # print(f"{sensor[24]}: {aqiPm25(sensor[1])}") # show data for individual sensors
            pm25Concentration += sensor[1] / 4 # https://www.purpleair.com/data.json?show=22989
        print(f"The AQI is: {aqiPm25(pm25Concentration)}")
    elif response.status_code == 429:
        print("Error: too many requests (response code 429).")
    else:
        print(f"Error: response code {response.status_code}")

def calculateAqi(aqiHigh, aqiLow, concHigh, concLow, concentration):
    conc = float(concentration)
    a = ((conc - concLow) / (concHigh - concLow)) * (aqiHigh - aqiLow) + aqiLow
    linear = round(a)
    return linear

def aqiPm25(concentration):
    conc = float(concentration)
    c = (math.floor(10 * conc)) / 10
    if c >= 0 and c < 12.1:
        aqi = calculateAqi(50,0,12,0,c)
    elif c >= 12.1 and c < 35.5:
        aqi = calculateAqi(100,51,35.4,12.1,c)
    elif c >= 35.5 and c < 55.5:
        aqi = calculateAqi(150,101,55.4,35.5,c)
    elif c >= 55.5 and c < 150.5:
        aqi = calculateAqi(200,151,150.4,55.5,c)
    elif c >= 150.5 and c < 250.5:
        aqi = calculateAqi(300,201,250.4,150.5,c)
    elif c >= 250.5 and c < 350.5:
        aqi = calculateAqi(400,301,350.4,250.5,c)
    elif c >= 350.5 and c < 500.5:
        aqi = calculateAqi(500,401,500.4,350.5,c)
    else:
        aqi = -1
    return aqi

while True:
    retrieveSensorData(22989, 37143, 38577, 17951) # nearby sensors
    time.sleep(30)