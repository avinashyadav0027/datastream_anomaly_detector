import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from anomaly_detector import detect_anomalies

def update(frame: int):
    """
    Update function for animating the anomaly detection in a data stream.

    Parameters
    ----------
    frame : int
        Current frame or time step in the animation.

    Notes
    -----
    This function assumes the existence of the following global variables:
    - anomaly_generator: A generator that yields the set of anomalies detected in the stream.
    - data_stream: The entire data stream being analyzed.

    It also assumes the existence of a global variable 'ax', representing a Matplotlib AxesSubplot.
    """
    # Get the set of anomalies detected so far in the stream
    anomalies = next(anomaly_generator) 

    # Clear the current plot for the next frame
    ax.clear()

    # Plot the data stream up to the current frame
    ax.plot(data_stream[:frame + 1], label='Data Stream')

    # Scatter plot the anomalies on the data stream
    ax.scatter(anomalies, data_stream[anomalies], color='red', label='Anomalies')

    # Set plot title and labels
    ax.set_title('Anomaly Detection in Data Stream')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')

    # Display the legend indicating the data stream and anomalies
    ax.legend()

def visualize_data_stream(data_str: list):
    """
    Visualizes a data stream and its anomalies using Matplotlib animation.

    Parameters
    ----------
    data_str : list
        List representing the data stream to be visualized.

    Notes
    -----
    This function assumes the existence of the following global variables:
    - data_stream: The entire data stream being visualized.
    - anomaly_generator: A generator that yields the set of anomalies detected in the stream.
    - ax: Matplotlib AxesSubplot for updating the plot.

    It also assumes the existence of the 'update' function for animation.

    The visualization includes a line plot of the data stream and scatter plot of detected anomalies.
    """
    # Make the variables global so that they don't need to be passed as parameters in the 'update' function
    global data_stream
    global anomaly_generator
    global ax

    # Set the global data_stream variable
    data_stream = data_str

    # The anomaly generator will yield a list of anomalies detected so far
    anomaly_generator = detect_anomalies(data_stream)

    # Create a figure and subplot for visualization
    fig, ax = plt.subplots()

    # Create animation of the data stream
    animation = FuncAnimation(fig, update, frames=len(data_stream), repeat=False)

    # Display the animation
    plt.show()
