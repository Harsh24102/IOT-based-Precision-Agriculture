"""Read a soil moisture sensor's digital output (DO pin) on a Raspberry Pi.

The DO pin only reports two states: above or below the threshold set with the
potentiometer on the sensor board. It cannot give a percentage. (The earlier
version mapped this 0/1 value onto 0-500 ranges, so it could only ever print
"Very low" or "Low".) For real percentages, read the analog AO pin through an
ADC such as the MCP3008.
"""
import time

import RPi.GPIO as GPIO

MOISTURE_SENSOR_PIN = 21   # BCM numbering
# Most modules pull DO LOW when the soil is wet (below the threshold).
# If your readings look reversed, set this to GPIO.HIGH.
WET_LEVEL = GPIO.LOW
INTERVAL_SECONDS = 1


def read_moisture_state():
    """Return "Wet" or "Dry" based on the sensor's digital output."""
    return "Wet" if GPIO.input(MOISTURE_SENSOR_PIN) == WET_LEVEL else "Dry"


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)
    time.sleep(0.1)  # let the sensor settle
    try:
        while True:
            state = read_moisture_state()
            print("Soil moisture:", state, "(irrigation needed)" if state == "Dry" else "")
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()  # always release the pins, not only on Ctrl+C


if __name__ == "__main__":
    main()
