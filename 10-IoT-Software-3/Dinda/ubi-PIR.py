import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
TOUCH_SENSOR_PIN = 23  # GPIO pin number for touch sensor
GPIO.setup(TOUCH_SENSOR_PIN, GPIO.IN)

# Ubidots configuration
UBIDOTS_TOKEN = "BBFF-kTSkgX5Sa1iYOP1V0WwuMdCdP5UnYo"
DEVICE_LABEL = "sensors"
VARIABLE_LABEL = "PIR"

def send_data_to_ubidots(touch_status):
    url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}/{VARIABLE_LABEL}/values"
    headers = {"Content-Type": "application/json", "X-Auth-Token": UBIDOTS_TOKEN}
    payload = {"value": touch_status}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Data sent to Ubidots successfully!")
    else:
        print("Failed to send data to Ubidots")

try:
    while True:
        sound_detected = GPIO.input(TOUCH_SENSOR_PIN)
        print("Gerakan terdeteksi:", sound_detected)

        # Send touch status to Ubidots
        send_data_to_ubidots(sound_detected)

        time.sleep(0.9)
        print("================")

except KeyboardInterrupt:
    GPIO.cleanup()
