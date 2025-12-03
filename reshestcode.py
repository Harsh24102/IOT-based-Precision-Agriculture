import Adafruit_DHT
import firebase_admin
from firebase_admin import credentials, firestore
import time
from datetime import datetime

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/home/pi/Desktop/credentials.json")  # Replace with your service account credentials
firebase_admin.initialize_app(cred)
db = firestore.client()

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Print data to console
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        # Send data to Firestore
        doc_ref = db.collection(u'sensor_data').document()
        doc_ref.set({
            u'sensor': u'DHT11',
            u'timestamp': current_time,
            u'temperature': temperature,
            u'humidity': humidity
        })
    else:
        print("Sensor failure. Check wiring.")
    # Pause execution for 3 seconds
    time.sleep(3)

