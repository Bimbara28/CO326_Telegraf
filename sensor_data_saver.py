from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/sensor-data', methods=['GET'])
def sensor_data():
    return jsonify({
        "temperature": round(random.uniform(-10, 50), 1),  # Temperature in Celsius
        "voltage": round(random.uniform(110, 240), 1),    # Voltage in Volts
        "current": round(random.uniform(0, 30), 1),       # Current in Amperes
        "power": round(random.uniform(50, 5000), 1),      # Power in Watts
        "smoke_detector": random.choice(["No Smoke", "Smoke Detected"])  # Smoke detector status
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
