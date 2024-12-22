from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/sensor-data', methods=['GET'])
def sensor_data():
    return jsonify({
        "temperature": round(random.uniform(-10, 50), 1),
        "humidity": round(random.uniform(10, 100), 1),
        "voltage": round(random.uniform(110, 230), 1),
        "current": round(random.uniform(0, 30), 1)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
