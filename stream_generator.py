import numpy as np

def simulate_data_stream(num_points=1000, anomaly_rate=0.05):
    """
    Function that returns a numpy array of float values which represent the data stream
    
    Parameters
    ----------
    num_points : int
                 number of values required in the data stream
    
    anomaly_rate : float
                   percentage of anomalies present in the data stream
    
    Returns
    -------
    data_stream : list
                  float values representing the data stream with anomalies included in it
    """
    # Simulate data stream with pattern, seasonality, and noise
    np.random.seed(42)
    time = np.arange(num_points)

    pattern = np.sin(0.02 * time) 
    seasonality = 0.2 * np.sin(0.005 * time)
    noise = np.random.normal(0, 0.5, num_points)
    
    data_stream = pattern + seasonality + noise #data stream will be the resultant of pattern, seasonality and noise
    
    # Introduce anomalies
    anomalies = np.random.choice(np.arange(num_points), size=int(anomaly_rate * num_points), replace=False)
    data_stream[anomalies] += 5 * np.random.normal(0, 1, len(anomalies))
    
    return data_stream