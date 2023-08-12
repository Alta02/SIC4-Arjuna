import RPi.GPIO as GPIO
import time

pir_pin = 17  # Ganti dengan nomor pin GPIO yang sesuai

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(pir_pin):
            print("Dinda Terdeteksi bergerak")
        else:
            print("Sensor Tidak mendeteksi dinda")
        time.sleep(1)
        print("=============================")

except KeyboardInterrupt:
    GPIO.cleanup()
