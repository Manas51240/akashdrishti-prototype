// Initialize the map centered over India
var map = L.map("map").setView([20.5937, 78.9629], 5);

// Add OpenStreetMap tiles
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© OpenStreetMap contributors"
}).addTo(map);

// Layer group to hold drawn AOIs
var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);

// Leaflet Draw control config
var drawControl = new L.Control.Draw({
  draw: {
    polygon: false,
    polyline: false,
    circle: false,
    marker: false,
    circlemarker: false,
    rectangle: {
      shapeOptions: {
        color: "#4ADE80"
      }
    }
  },
  edit: {
    featureGroup: drawnItems
  }
});
map.addControl(drawControl);

// On draw event
map.on("draw:created", function (e) {
  var layer = e.layer;

  // Remove previous AOIs
  drawnItems.clearLayers();

  // Add the new AOI
  drawnItems.addLayer(layer);

  // Convert the drawn layer to GeoJSON
  var geojson = layer.toGeoJSON();

  // Stringify and store in hidden input
  document.getElementById("aoi_geojson").value = JSON.stringify(geojson);

  console.log("✅ AOI GeoJSON:", JSON.stringify(geojson));
});
