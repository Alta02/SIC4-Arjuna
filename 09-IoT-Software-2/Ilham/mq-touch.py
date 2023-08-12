import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

TOUCH_SENSOR_PIN = 17  # GPIO pin number for touch sensor
MQTT_BROKER = "broker.hivemq.com"  # Change to your HiveMQ broker address
MQTT_TOPIC = "test1/arjuna/data-touch"

GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_SENSOR_PIN, GPIO.IN)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(MQTT_BROKER, 1883, 60)

try:
    while True:
        touch_detected = GPIO.input(TOUCH_SENSOR_PIN)  # Sensor output is active high
        message = "Touched" if touch_detected else "Not touched"
        mqtt_payload = "1" if touch_detected else "0"

        print(message)
        client.publish(MQTT_TOPIC, mqtt_payload)
        time.sleep(1)
        print("==================")

except KeyboardInterrupt:
    GPIO.cleanup()
