from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# 🔑 Your API Key (Replace this with your actual key)
API_KEY = "HtbLe8NuKcSXtMrFC-_LOz-hvnkg0ZPgLBmzPiiEg-Y"

# Sample Health Data Storage (For Testing)
health_data = []

# Health Check Endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Apple Health API is running", "status": "healthy"})

# Get Health Data (Requires API Key)
@app.route("/health-data", methods=["GET"])
def get_health_data():
    if request.headers.get("X-API-Key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(health_data)

# Post Health Data (Requires API Key)
@app.route("/health-data", methods=["POST"])
def post_health_data():
    if request.headers.get("X-API-Key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json
    health_data.append(data)  # Store health data (for testing)
    return jsonify({"message": "Data received", "data": data})

# Run the Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
