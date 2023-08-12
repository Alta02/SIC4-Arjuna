import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

SOUND_SENSOR_PIN = 17  # GPIO pin number
MQTT_BROKER = "broker.hivemq.com"  #Ganti dengan alamat broker HiveMQ
MQTT_TOPIC = "test1/arjuna/data-sound"

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(MQTT_BROKER, 1883, 60)

try:
    while True:
        sound_detected = GPIO.input(SOUND_SENSOR_PIN)
        message = str(sound_detected)
        
        print("Sound Detected:", sound_detected)
        client.publish(MQTT_TOPIC, message)
        time.sleep(1)
        print("==================")

except KeyboardInterrupt:
    GPIO.cleanup()
