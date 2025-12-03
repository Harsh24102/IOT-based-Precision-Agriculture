import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pin connected to the soil moisture sensor
moisture_sensor_pin = 21

def read_moisture_level():
    # Set up the GPIO pin as input
    GPIO.setup(moisture_sensor_pin, GPIO.IN)

    # Wait for the sensor to stabilize
    time.sleep(0.1)

    # Read the moisture level (0 for dry soil, 1 for moist soil)
    moisture_level = GPIO.input(moisture_sensor_pin)
    return moisture_level

def categorize_moisture_level(moisture_value):
    if moisture_value == 0:
        return "Very low"
    elif 0 < moisture_value <= 100:
        return "Low"
    elif 100 < moisture_value <= 300:
        return "Medium"
    elif 300 < moisture_value <= 500:
        return "High"
    else:
        return "Very high"

try:
    while True:
        # Read moisture level
        moisture_level = read_moisture_level()

        # Categorize moisture level
        moisture_category = categorize_moisture_level(moisture_level)

        # Print moisture level category
        print("Moisture level:", moisture_category)

        # Wait before taking another reading
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO settings on keyboard interrupt
    GPIO.cleanup()

