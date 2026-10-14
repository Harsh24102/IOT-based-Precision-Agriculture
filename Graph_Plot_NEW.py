"""Live plot of the temperature and humidity readings logged by reshestcode.py.

Reads the same place the logger writes to: the Firestore collection `sensor_data`.
(The earlier version read the Firebase *Realtime Database*, which the logger never
writes to, so the chart stayed empty.)

Set FIREBASE_CREDENTIALS to the path of your service-account JSON key, or put the
key next to this script as `credentials.json`. Never commit the key file.
"""
import os
import time
from datetime import datetime, timedelta

import firebase_admin
import matplotlib.pyplot as plt
from firebase_admin import credentials, firestore

CREDENTIALS = os.environ.get("FIREBASE_CREDENTIALS", "credentials.json")
WINDOW = timedelta(hours=1)      # how much history to show
REFRESH_SECONDS = 5
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"  # format written by reshestcode.py

firebase_admin.initialize_app(credentials.Certificate(CREDENTIALS))
db = firestore.client()

plt.ion()
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)


def fetch_last_hour():
    """Readings from the last hour, oldest first."""
    since = (datetime.now() - WINDOW).strftime(TIME_FORMAT)
    # Timestamps are stored as sortable text, so a string comparison filters by time.
    docs = (db.collection("sensor_data")
              .where("timestamp", ">=", since)
              .order_by("timestamp")
              .stream())
    rows = []
    for doc in docs:
        d = doc.to_dict()
        try:
            rows.append((datetime.strptime(d["timestamp"], TIME_FORMAT), d["temperature"], d["humidity"]))
        except (KeyError, ValueError, TypeError):
            continue  # skip malformed readings instead of stopping the whole chart
    return rows


def update_plot():
    rows = fetch_last_hour()
    if not rows:
        print("No readings in the last hour yet.")
        return
    timestamps, temperatures, humidities = zip(*rows)

    ax1.clear()
    ax1.plot(timestamps, temperatures, "r-", label="Temperature")
    ax1.set_title("Real-time Temperature Data")
    ax1.set_ylabel("Temperature (°C)")
    ax1.legend()
    ax1.grid(True)

    ax2.clear()
    ax2.plot(timestamps, humidities, "b-", label="Humidity")
    ax2.set_title("Real-time Humidity Data")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Humidity (%)")
    ax2.legend()
    ax2.grid(True)

    fig.autofmt_xdate()
    plt.draw()
    plt.pause(0.1)


if __name__ == "__main__":
    try:
        while plt.fignum_exists(fig.number):
            update_plot()
            plt.pause(REFRESH_SECONDS)
    except KeyboardInterrupt:
        pass
