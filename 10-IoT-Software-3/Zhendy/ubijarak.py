import RPi.GPIO as GPIO
import time
import requests
import json

GPIO.setmode(GPIO.BCM)

GPIO_Trigger = 24
GPIO_echo = 23

# Set up GPIO pins as output and input
GPIO.setup(GPIO_Trigger, GPIO.OUT)
GPIO.setup(GPIO_echo, GPIO.IN)


# Ubidots configuration
UBIDOTS_TOKEN = "BBFF-kTSkgX5Sa1iYOP1V0WwuMdCdP5UnYo"
DEVICE_LABEL = "sensors"
VARIABLE_LABEL = "ultra"

# Function to measure distance
def distance():
    GPIO.output(GPIO_Trigger, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_Trigger, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_echo) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_echo) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance

# Send distance data to Ubidots
def send_data_to_ubidots(distance_value):
    url = "https://industrial.api.ubidots.com/api/v1.6/devices/{device_label}/{variable_label}/values"
    headers = {"Content-Type": "application/json", "X-Auth-Token": UBIDOTS_TOKEN}
    payload = {"value": distance_value}

    url = url.format(device_label=DEVICE_LABEL, variable_label=VARIABLE_LABEL)
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Data sent to Ubidots successfully!")
    else:
        print("Failed to send data to Ubidots")

# Main loop
try:
    while True:
        dist = distance()
        print("Measured Distance = %.2f cm" % dist)
        
        # Send distance data to Ubidots
        send_data_to_ubidots(dist)
        print("=========================================")

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
