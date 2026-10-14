# 🌱 IoT Precision Agriculture — ANFIS & Fuzzy-Logic Irrigation

![Raspberry Pi](https://img.shields.io/badge/Edge-Raspberry%20Pi-A22846?logo=raspberrypi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Firebase](https://img.shields.io/badge/Cloud-Firestore-FFCA28?logo=firebase&logoColor=black)
![ANFIS](https://img.shields.io/badge/Control-ANFIS%20%7C%20Fuzzy%20Logic-6A1B9A)

A **Raspberry Pi** system that reads soil moisture, temperature and humidity, logs readings to
**Firestore**, plots them live, and decides how much to irrigate with two models: a trained
**ANFIS** (adaptive neuro-fuzzy inference system) and a **15-rule fuzzy-logic** controller.

## How it works

```
DHT11 (temp/humidity) ─┐
                       ├─► Raspberry Pi (Python) ──► Firestore `sensor_data` ──► Live chart (Graph_Plot_NEW.py)
Soil moisture (DO pin) ┘           │
                                   ▼
                     Irrigation decision: ANFIS model / 15-rule fuzzy controller
```

| File | What it does |
|---|---|
| `reshestcode.py` | Reads the DHT11 every 3 s (with retries) and saves each reading to Firestore |
| `Graph_Plot_NEW.py` | Live chart of the last hour of readings from the same Firestore collection |
| `MoistureSensor1.py` | Reads the soil sensor's digital output: **Wet** or **Dry** (irrigation needed) |
| `ANFIS_MODEL_.ipynb` | Trains a Takagi–Sugeno ANFIS (hybrid learning: least squares + gradient descent) to predict litres of irrigation from moisture, temperature, humidity, rain and water level; compares it with a baseline |
| `15_Rules_Fuzzy_logic.ipynb` | Fuzzy controller with 15 rules (scikit-fuzzy), in a 3-level and a 5-level version |
| `Data/weather_data.csv` | Half-hourly temperature, humidity, soil moisture and rain readings (2023) |

## Hardware

Raspberry Pi · DHT11 temperature/humidity sensor (data on GPIO 4) · soil moisture sensor module
(DO on GPIO 21)

## Run it

**1. Firebase:** create a project with Firestore and download a service-account key (JSON).
Keep the key out of Git and point the scripts to it:

```bash
export FIREBASE_CREDENTIALS=/home/pi/credentials.json
```

**2. On the Raspberry Pi:**

```bash
pip install firebase-admin Adafruit_DHT RPi.GPIO
python reshestcode.py        # log temperature and humidity
python MoistureSensor1.py    # soil moisture wet/dry
```

**3. On your computer (live chart):**

```bash
pip install firebase-admin matplotlib
python Graph_Plot_NEW.py
```

**4. Models:**

```bash
pip install numpy pandas scikit-learn scikit-fuzzy matplotlib openpyxl jupyter
jupyter notebook
```

The ANFIS notebook expects the training file `Data/agriculture_data_for_ann.xlsx` with columns
`Moisture(%)`, `Temperature(C)`, `Humidity(%)`, `Rain(cm)`, `Water Level(mm)` and
`Irrigation amount needed(l)`.

## Fixes (Oct 2026)

- **ANFIS was never trained:** rule parameters stayed random and only a forward pass ran. It now
  trains with the hybrid learning rule and reports test RMSE against a baseline.
- **Live chart showed nothing:** it read the Realtime Database while the logger writes to
  Firestore. Both now use Firestore.
- **Moisture sensor:** the 0/1 digital reading was mapped onto 0–500 ranges, so it could only
  print "Very low" or "Low". It now reports Wet / Dry.
- **Fuzzy notebook:** the 5-level version crashed (missing rule list, wrong term name) and the
  3-level example used a rain value outside its 0–100 range. Both now run.
- Firebase key paths moved to the `FIREBASE_CREDENTIALS` environment variable.

**Tech:** Python · Raspberry Pi · RPi.GPIO · Adafruit_DHT · Firebase Firestore · scikit-learn ·
scikit-fuzzy · NumPy · pandas · Matplotlib
