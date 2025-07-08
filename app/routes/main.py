from flask import Blueprint, render_template, request, session
from app.utils.image_analysis import simulate_change_detection
from app.utils.email_alert import send_alert_email

main = Blueprint("main", __name__)

# Home Page – Manual Coordinate Input
@main.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# AOI Selection via Leaflet Map
@main.route("/aoi", methods=["GET"])
def aoi_page():
    return render_template("aoi.html")

# Process AOI Submission (Map or Manual)
@main.route("/process-aoi", methods=["POST"])
def process_aoi():
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    aoi_geojson = request.form.get("aoi_geojson")  # From Leaflet map if available

    # 📧 Replace this with user session logic if you implement login
    user_email = "manasdeshmukh512@gmail.com"

    # --- Option 1: AOI from GeoJSON (map) ---
    if aoi_geojson:
        print("✅ AOI received as GeoJSON")
        print("🗓️ Start Date:", start_date)
        print("🗓️ End Date:", end_date)
        print("📦 GeoJSON:", aoi_geojson)

        result = simulate_change_detection(aoi_geojson, start_date, end_date)

        # ✅ Send Email Alert
        subject = "🛰️ AkashDrishti: Change Detected in Selected AOI"
        summary = f"NDVI changed from {result['ndvi_start']} to {result['ndvi_end']} ({result['interpretation']})"
        send_alert_email(user_email, subject, summary, start_date, end_date)

        return render_template("results.html", **result)

    # --- Option 2: AOI from Manual Coordinates ---
    try:
        lat1 = float(request.form.get("lat1"))
        lon1 = float(request.form.get("lon1"))
        lat2 = float(request.form.get("lat2"))
        lon2 = float(request.form.get("lon2"))

        print("✅ AOI received as Manual Coordinates")
        print(f"Top-Left: ({lat1}, {lon1})")
        print(f"Bottom-Right: ({lat2}, {lon2})")
        print("🗓️ Start Date:", start_date)
        print("🗓️ End Date:", end_date)

        # Convert to GeoJSON-style polygon
        polygon = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [lon1, lat1],  # top-left
                    [lon2, lat1],  # top-right
                    [lon2, lat2],  # bottom-right
                    [lon1, lat2],  # bottom-left
                    [lon1, lat1]   # close polygon
                ]]
            }
        }

        aoi_geojson = str(polygon)
        result = simulate_change_detection(aoi_geojson, start_date, end_date)

        # ✅ Send Email Alert
        subject = "🛰️ AkashDrishti: Change Detected in Selected AOI"
        summary = f"NDVI changed from {result['ndvi_start']} to {result['ndvi_end']} ({result['interpretation']})"
        send_alert_email(user_email, subject, summary, start_date, end_date)

        return render_template("results.html", **result)

    except Exception as e:
        print("❌ Error parsing manual AOI coordinates:", e)
        return "Invalid AOI coordinates. Please go back and re-enter.", 400
