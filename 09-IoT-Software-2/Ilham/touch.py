import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the touch sensor pin
touch_pin = 17

# Set up the pin as input
GPIO.setup(touch_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(touch_pin) == GPIO.HIGH:
            print("Disentuh sama Ilham")
        else:
            print("Ngga disentuh sama Ilham")
        time.sleep(0.9)
        print("================")

except KeyboardInterrupt:
    GPIO.cleanup()
