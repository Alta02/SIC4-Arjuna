import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

PIR_SENSOR_PIN = 17  # GPIO pin number for PIR sensor
MQTT_BROKER = "broker.hivemq.com"  # Ganti dengan alamat broker HiveMQ
MQTT_TOPIC = "test1/arjuna/data-pir"

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_SENSOR_PIN, GPIO.IN)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(MQTT_BROKER, 1883, 60)

try:
    while True:
        pir_triggered = GPIO.input(PIR_SENSOR_PIN)
        message = f"Motion detected: {pir_triggered}"
        mqtt_payload = "01" if pir_triggered else "00"
        
        print(message)
        client.publish(MQTT_TOPIC, mqtt_payload)
        time.sleep(1)
        print("==================")

except KeyboardInterrupt:
    GPIO.cleanup()
