# CO326 Telegraf Configuration

This repository contains the configuration and scripts for setting up Telegraf to collect sensor data from an HTTP endpoint and send it to InfluxDB Cloud. The project is designed for monitoring a building's electrical system, focusing on metrics like temperature, humidity, voltage, and current.

## Features
- Collects JSON-formatted sensor data via HTTP.
- Sends data to InfluxDB Cloud for storage and visualization.
- Includes a Python script to simulate sensor data for testing.

## Prerequisites
- Telegraf (latest version for your operating system).
- An InfluxDB Cloud account.
- Python 3.x (for optional data simulation).
- Flask (for running the sensor data simulation server).

## Repository Contents
- `telegraf.conf`: Configuration file for Telegraf.
- `sensor_data_server.py`: Python script to simulate sensor data.
- `README.md`: Documentation for the repository.

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/Bimbara28/CO326_Telegraf.git
cd CO326_Telegraf
```

### Install Telegraf
1. Download Telegraf from [InfluxData Downloads](https://portal.influxdata.com/downloads/).
2. Follow the installation instructions for your platform.
3. Verify the installation:
```bash
telegraf --version
```

### Configure Telegraf
1. Open `telegraf.conf`.
2. Replace the placeholders:
   - `your-influxdb-token`: Replace with your InfluxDB Cloud token.
   - `your-org-name`: Replace with your InfluxDB organization name.
   - `your-bucket-name`: Replace with your bucket name.
3. Save the file.

### Simulate Sensor Data (Optional)
1. Install Flask:
```bash
pip install flask
```
2. Run the simulation script:
```bash
python sensor_data_server.py
```
   - The server will start at `http://localhost:8080/sensor-data`.

### Run Telegraf
Start Telegraf with the provided configuration:
```bash
telegraf --config telegraf.conf
```

## Testing and Validation
1. Test the configuration:
```bash
telegraf --config telegraf.conf --test
```
2. Check data in InfluxDB Cloud:
   - Log in to your InfluxDB account.
   - Navigate to your bucket in the Data Explorer.
3. Ensure real-time data is flowing from the simulated endpoint if used.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For issues or questions, open an issue in this repository or contact the repository owner.
