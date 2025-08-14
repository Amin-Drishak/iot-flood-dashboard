
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Step 1: Mock IoT API data retrieval
times = pd.date_range(datetime.now(), periods=50, freq="H")
levels = np.random.normal(1.5, 0.1, size=50)

# Inject anomalies
levels[10] += 0.5
levels[30] += 0.7

# Step 2: Z-score anomaly detection
z_scores = (levels - np.mean(levels)) / np.std(levels)
anomalies = np.abs(z_scores) > 2

# Step 3: Plot dashboard
plt.plot(times, levels, label="Water Level")
plt.scatter(times[anomalies], levels[anomalies], color="red", label="Anomaly")
plt.xlabel("Time")
plt.ylabel("Water Level (m)")
plt.title("IoT Flood Monitoring Dashboard")
plt.legend()
plt.tight_layout()
plt.savefig("dashboard.png")
print("Dashboard plot saved to dashboard.png")
