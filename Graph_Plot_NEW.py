import firebase_admin
from firebase_admin import credentials, db
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time

# Initialize Firebase with your credentials
cred = credentials.Certificate("dht11-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://dht11-data-e5d29-default-rtdb.firebaseio.com/'
}, name='my-app')

# Get a reference to the Firebase Realtime Database with the correct path
ref = db.reference('/sensor_data')

# Create the plot
plt.ion()  # Turn on interactive mode
fig, (ax1, ax2) = plt.subplots(2, 1)

# Initialize empty lists to store timestamp, temperature, and humidity data
timestamps = []
temperatures = []
humidities = []

# Define update function for the plot
def update_plot():
    global timestamps, temperatures, humidities
    # Fetch data from Firebase
    data = ref.get()
    if data:
        try:
            # Clear previous data
            timestamps.clear()
            temperatures.clear()
            humidities.clear()
            for key, value in data.items():
                timestamps.append(datetime.strptime(value['timestamp'], '%Y-%m-%d %H:%M:%S'))
                temperatures.append(value['temperature'])
                humidities.append(value['humidity'])
            # Update temperature plot
            ax1.clear()
            ax1.plot(timestamps, temperatures, 'r-', label='Temperature')
            ax1.set_title('Real-time Temperature Data')
            ax1.set_xlabel('Timestamp')
            ax1.set_ylabel('Temperature (°C)')
            ax1.legend()
            ax1.grid(True)
            # Update humidity plot
            ax2.clear()
            ax2.plot(timestamps, humidities, 'b-', label='Humidity')
            ax2.set_title('Real-time Humidity Data')
            ax2.set_xlabel('Timestamp')
            ax2.set_ylabel('Humidity (%)')
            ax2.legend()
            ax2.grid(True)
            
            # Set x-axis limit based on the maximum timestamp
            max_timestamp = max(timestamps)
            ax1.set_xlim(max_timestamp - timedelta(hours=1), max_timestamp)
            ax2.set_xlim(max_timestamp - timedelta(hours=1), max_timestamp)
            
            # Draw the plot
            plt.draw()
            plt.pause(0.1)
        except Exception as e:
            print("Error:", e)

# Continuous loop to update the plot
while True:
    update_plot()
    time.sleep(1)  # Fetch data every 1 second