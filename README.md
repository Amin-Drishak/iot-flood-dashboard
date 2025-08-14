# GRASS–GEE → SWMM Urban Hydrology Pipeline

**Author:** Muhammad Amin Khan

## Overview
This open-source prototype integrates:
- **GRASS GIS** for spatial preprocessing
- **Google Earth Engine (GEE)** for remote-sensing & land-use data
- **EPA SWMM** for urban hydrology modeling
- **Optimization** with SciPy Differential Evolution and **CMA-ES** (via `cma`)
- **Sensitivity/uncertainty** scaffolds for robust, decision-ready outputs
- Fully reproducible via **Conda** (geospatial stack) or minimal **pip** (no heavy geo deps)

**Goal:** A transparent, reproducible workflow for automated **catchment preprocessing → hydrologic modeling → calibration → sensitivity**, supporting **climate-resilient infrastructure planning**.

---

## Features
- Automated catchment & land-use preprocessing (GRASS/GEE)
- SWMM input scaffolding (rainfall, subcatchments, parameters)
- Calibration via Differential Evolution / CMA-ES
- Global sensitivity hooks
- Clean, modular Python (`main.py`, `pipeline.py`)
- Example **IoT Flood Dashboard** (mock API + anomaly detection)

---

## Repository Layout
