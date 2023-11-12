# Anomaly Detection in Data Streams

This project implements an anomaly detection system for data streams using Robust Random Cut Forest (RRCF). The main goal is to identify anomalies or outliers in a streaming dataset.

## Files and Structure

- `config.py`: Configuration file containing parameters for the data stream and the RRCF algorithm.
  - `n`: Number of points in the data stream.
  - `num_trees`: Number of trees in the RRCF ensemble.
  - `shingle_size`: Size of the shingle used for rolling window.
  - `tree_size`: Size of a single tree in the ensemble.
  - `threshold`: Threshold value for anomaly detection.

- `main.py`: Main script to run the anomaly detection on a simulated data stream.
  - Uses `simulate_data_stream` from `stream_generator.py` to generate a data stream.
  - Calls `visualize_data_stream` from `visualizer.py` to visualize the data stream and detected anomalies.

- `visualizer.py`: Module for visualizing the data stream and detected anomalies using Matplotlib animation.
  - Contains the `update` function for animation and `visualize_data_stream` function for overall visualization.

- `anomaly_detector.py`: Module implementing the anomaly detection logic using RRCF.
  - Defines the `detect_anomalies` generator function, which yields a list of detected anomalies in the data stream.

- `stream_generator.py`: Module for simulating a data stream.
  - Provides the `simulate_data_stream` function to generate a synthetic data stream with anomalies.

## Running the Code

To run the anomaly detection on a simulated data stream, execute the `main.py` script:

```bash
python main.py
