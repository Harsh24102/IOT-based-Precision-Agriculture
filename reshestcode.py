"""Read temperature and humidity from a DHT11 sensor and log them to Firestore.

Runs on the Raspberry Pi. Set FIREBASE_CREDENTIALS to the path of your
service-account JSON key (default: /home/pi/Desktop/credentials.json).
Never commit the key file.
"""
import os
import time
from datetime import datetime

import Adafruit_DHT
import firebase_admin
from firebase_admin import credentials, firestore

CREDENTIALS = os.environ.get("FIREBASE_CREDENTIALS", "/home/pi/Desktop/credentials.json")
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4            # BCM pin the sensor's data line is wired to
INTERVAL_SECONDS = 3

firebase_admin.initialize_app(credentials.Certificate(CREDENTIALS))
db = firestore.client()

try:
    while True:
        # read_retry tries up to 15 times; the DHT11 often fails a single read.
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
            db.collection("sensor_data").add({
                "sensor": "DHT11",
                "timestamp": current_time,
                "temperature": temperature,
                "humidity": humidity,
            })
        else:
            print("Sensor failure. Check wiring.")
        time.sleep(INTERVAL_SECONDS)
except KeyboardInterrupt:
    print("Stopped.")
