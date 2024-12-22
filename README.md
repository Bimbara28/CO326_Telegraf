# CO326 Telegraf Configuration

This repository contains the configuration and scripts for setting up Telegraf to collect and process sensor data for a building's electrical system. The collected data includes **temperature**, **voltage**, **current**, **power**, and **smoke detector status**. The data is forwarded to InfluxDB Cloud for visualization and analysis.

## Features
- **Real-Time Data Collection**: Collects sensor data from an HTTP endpoint in JSON format.
- **Customizable Configuration**: Easily configurable to accommodate additional data fields or sources.
- **Integration with InfluxDB Cloud**: Automatically forwards processed data to InfluxDB for storage and visualization.
- **Data Simulation**: Includes a Python script to simulate sensor data for testing and validation.

## Prerequisites
- **Telegraf**: Installed and configured on your system.
- **InfluxDB Cloud Account**: For storing and visualizing data.
- **Python 3.x**: For running the sensor data simulation script.
- **Flask**: To serve simulated data.

## Repository Contents
- `telegraf.conf`: Configuration file for Telegraf.
- `sensor_data_server.py`: Python script to simulate sensor data.
- `README.md`: Documentation for this repository.

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
1. Open `telegraf.conf` in a text editor.
2. Replace the placeholders:
   - `your-influxdb-token`: Replace with your InfluxDB token.
   - `your-org-name`: Replace with your InfluxDB organization name.
   - `your-bucket-name`: Replace with your bucket name.
3. Save the file.

### Simulate Sensor Data
1. Install Flask:
   ```bash
   pip install flask
   ```
2. Run the simulation script:
   ```bash
   python sensor_data_server.py
   ```
   The server will start at `http://localhost:8080/sensor-data`.

### Start Telegraf
Start Telegraf with the provided configuration:
```bash
telegraf --config telegraf.conf
```

## Testing and Validation
1. Use the following command to test the Telegraf configuration:
   ```bash
   telegraf --config telegraf.conf --test
   ```
2. Log in to your InfluxDB Cloud account and verify that the data is being sent to your bucket.
2. Check data in InfluxDB Cloud:
   - Log in to your InfluxDB account.
   - Navigate to your bucket in the Data Explorer.
3. Ensure real-time data is flowing from the simulated endpoint if used.


