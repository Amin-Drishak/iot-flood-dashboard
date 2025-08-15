# GRASS–GEE → SWMM Urban Hydrology Pipeline

**Author:** Muhammad Amin Khan

---

## Overview

This open-source prototype integrates:

- **GRASS GIS** for spatial preprocessing  
- **Google Earth Engine (GEE)** for remote-sensing & land-use data  
- **EPA SWMM** for urban hydrology modeling  
- **Optimization** with SciPy Differential Evolution and CMA-ES (via `cma`)  
- **Sensitivity/uncertainty scaffolds** for robust, decision-ready outputs  

The workflow is **fully reproducible** via Conda (geospatial stack) or minimal pip (no heavy geospatial dependencies).  

**Goal:** A transparent, reproducible workflow for automated catchment preprocessing → hydrologic modeling → calibration → sensitivity, supporting climate-resilient infrastructure planning.

---

## Features

- Automated catchment & land-use preprocessing (GRASS/GEE)  
- SWMM input scaffolding (rainfall, subcatchments, parameters)  
- Calibration via Differential Evolution / CMA-ES  
- Global sensitivity hooks  
- Clean, modular Python (`main.py`, `pipeline.py`)  
- Example **IoT Flood Dashboard** (mock API + anomaly detection)

---

## Tools & Libraries

- Python 3.x  
- GRASS GIS, Google Earth Engine API  
- EPA SWMM  
- Pandas, NumPy, Matplotlib  
- SciPy (`differential_evolution`), CMA-ES (`cma`)  

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd GRASS-GEE-SWMM-Urban-Hydrology-Pipeline
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate # Linux/macOS
### **3. Install dependencies**
   ```bash
   pip install -r requirements.txt

---

### **4. Run the simulation**
   ```bash
   python main.py

---

### **5. Check the output hydrograph**
   - The hydrograph image will be saved as `hydrograph.png` in the project folder.

Author / Contact

Muhammad Amin Khan
Email: ameenkhan8823813@gmail.com
WhatsApp: +8618852000702
WeChat: Aminkhan786
