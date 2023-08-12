import RPi.GPIO as GPIO
import time

SOUND_SENSOR_PIN = 17  # GPIO pin number

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)

try:
    while True:
        sound_detected = GPIO.input(SOUND_SENSOR_PIN)
        if sound_detected:
            print("Suruh diam!")
        else:
            print("sunyi banget.")
        time.sleep(1)
        print("==================")

except KeyboardInterrupt:
    GPIO.cleanup()
