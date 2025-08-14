import pandas as pd

# Mock sensor data
data = pd.DataFrame({
    "time": range(10),
    "water_level": [0.3, 0.5, 0.6, 1.2, 0.4, 0.3, 0.8, 1.5, 0.9, 0.2]
})

threshold = 1.0
data["anomaly"] = data["water_level"] > threshold

print("IoT Flood Dashboard - Anomaly Detection")
print(data)
