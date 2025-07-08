# app/utils/image_analysis.py

import random
import json

def simulate_change_detection(aoi_geojson, start_date, end_date):
    try:
        geometry = json.loads(aoi_geojson)
        # Optionally validate it's a polygon or bbox
        if geometry["type"] not in ["Feature", "Polygon"]:
            raise ValueError("Unsupported geometry type")

    except Exception as e:
        print("❌ Invalid GeoJSON:", e)
        return {
            "start_date": start_date,
            "end_date": end_date,
            "ndvi_start": "N/A",
            "ndvi_end": "N/A",
            "change": "N/A",
            "interpretation": "Invalid AOI",
            "status": "error"
        }

    # Simulate NDVI values (mock)
    ndvi_start = round(random.uniform(0.3, 0.8), 2)
    ndvi_end = round(random.uniform(0.1, 0.9), 2)
    delta = round(ndvi_end - ndvi_start, 2)

    if delta > 0.1:
        interpretation = "Increased Vegetation"
    elif delta < -0.1:
        interpretation = "Decreased Vegetation"
    else:
        interpretation = "Minimal Change"

    print(f"📊 NDVI Start: {ndvi_start}, NDVI End: {ndvi_end}, ΔNDVI: {delta} → {interpretation}")

    return {
        "start_date": start_date,
        "end_date": end_date,
        "ndvi_start": ndvi_start,
        "ndvi_end": ndvi_end,
        "change": delta,
        "interpretation": interpretation,
        "status": "success"
    }
