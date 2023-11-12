import numpy as np

from stream_generator import simulate_data_stream
from visualizer import visualize_data_stream
from config import n,anomaly_rate
def main():

    t = np.arange(n)
    data_stream = simulate_data_stream(num_points=n,anomaly_rate=anomaly_rate)
    
    # Visualize data stream and anomalies
    visualize_data_stream(data_stream)

if __name__ == "__main__":
    main()


