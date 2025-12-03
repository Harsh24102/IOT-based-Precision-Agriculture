# 🧠 IOT-Based Precision Agriculture System: ANFIS & Fuzzy Control

![Status: Complete](https://img.shields.io/badge/Status-Complete-green.svg)
[![Tech Stack](https://img.shields.io/badge/Control_System-ANFIS%20|%20Fuzzy%20Logic-red.svg)](https://en.wikipedia.org/wiki/Adaptive_neuro_fuzzy_inference_system)
[![Tech Stack](https://img.shields.io/badge/Microcomputer-Raspberry%20Pi-red.svg)](https://www.raspberrypi.com/)
[![Tech Stack](https://img.shields.io/badge/Cloud_DB-Firebase%20Firestore-orange.svg)](https://firebase.google.com/docs/firestore)
[![Tech Stack](https://img.shields.io/badge/Python-GPIO%20|%20Matplotlib-blue.svg)](https://www.python.org/)

## 1. Project Goal & Value Proposition

The objective was to develop an intelligent **Precision Agriculture System** that uses **Raspberry Pi** as an edge computer for real-time monitoring and advanced crop optimization. By employing **ANFIS (Adaptive Neuro-Fuzzy Inference System)**, the system achieves highly accurate decision-making for automated irrigation, ensuring optimal resource allocation and maximizing yield.

## 2. Advanced Features and Methodology

This project goes beyond simple sensor thresholds by integrating advanced control and data systems:

* **Adaptive Neuro-Fuzzy Inference System (ANFIS):** Developed and trained an **ANFIS model** in a Jupyter Notebook (`ANFIS_MODEL_.ipynb`) to predict the optimal irrigation amount based on inputs like **Moisture, Temperature, Humidity, and Rain**.
* **Fuzzy Logic Control:** Implemented a supplementary **Fuzzy Logic system** (`15_Rules_Fuzzy_logic.ipynb`) using 15 predefined rules to map sensor conditions to control actions, offering robust and human-readable decision logic for irrigation management.
* **Edge Computing & GPIO Control:** Utilized **Python with the RPi.GPIO library** (`MoistureSensor1.py`) on the Raspberry Pi to interface directly with the hardware, read soil moisture levels, and categorize them (e.g., "Very low", "Medium", "High").
* **Cloud Data Logging:** Python scripts (`reshestcode.py`) were configured to capture real-time temperature and humidity data from the DHT11 sensor and securely log it into a **Google Firestore** database.
* **Real-time Visualization:** A separate Python script (`Graph_Plot_NEW.py`) connects to the Firebase Realtime Database and uses **Matplotlib** to generate and update live plots of temperature and humidity data.

## 3. Technology Stack

| Category | Tools and Libraries |
| :--- | :--- |
| **Control System** | **ANFIS (Adaptive Neuro-Fuzzy Inference System), Fuzzy Logic** |
| **Microcomputer** | **Raspberry Pi** |
| **Programming** | **Python** (Pandas, NumPy, scikit-fuzzy, Adafruit_DHT, RPi.GPIO) |
| **Cloud/Data** | **Firebase Firestore, Firebase Realtime Database** |
| **Visualization** | **Matplotlib** (for real-time plotting) |

## 4. Setup and Operation

1.  **Hardware:** Raspberry Pi, Soil Moisture Sensor, DHT11 Sensor (Temperature/Humidity).
2.  **Cloud Setup:** Configure a project in Firebase and set up the service account credentials for Firestore access.
3.  **Deployment:** Run the primary Python scripts (`MoistureSensor1.py` and `reshestcode.py`) on the Raspberry Pi to start reading sensors, executing control logic, and pushing data to the cloud.
4.  **Monitoring:** Execute `Graph_Plot_NEW.py` on a local machine to view the real-time sensor data plots.

---

This is a fantastic repository, showcasing high-level skills in AI-driven control systems and cloud integration. Great job getting the code fixed and uploaded!
