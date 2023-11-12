import numpy
import rrcf

from shingle import shingle
from config import num_trees,shingle_size,tree_size,threshold

def detect_anomalies(data_stream:list):
    """
    Generator that returns list anomalies detected so far in the data stream
    
    Parameters
    ----------
    data_stream : list of floating point values of the time series data

    Yields
    ------
    list
        list of anomalies detected so far in the data stream

    """

    # Create a forest of empty trees
    forest = []
    for _ in range(num_trees):
        tree = rrcf.RCTree()
        forest.append(tree)
        
    # Use the "shingle" generator to create rolling window
    points = shingle(data_stream, size=shingle_size)

    # Create a dict to store anomaly score of each point
    avg_codisp = {}
    
    #Create a list to store the points which are anomalies
    anomalies = []
    
    # define varibales to calculate moving average and moving standard deviation of the datastream using welford's algorithm
    # these wil be used to detect anomalies

    count = 0 # number of data points considered so far
    moving_average = 0 # average of the anomaly scores of the data points in the range 1 to count inclusive
    M2 = 0 #will be used to calculate standard deviation of the anomaly scores of the data points in the range 1 to count inclusive

    # For each shingle...
    for index, point in enumerate(points):
        # For each tree in the forest...
        for tree in forest:
            # If tree is above permitted size, drop the oldest point (FIFO)
            if len(tree.leaves) > tree_size:
                tree.forget_point(index - tree_size)
            # Insert the new point into the tree
            tree.insert_point(point, index=index)
            # Compute codisp on the new point and take the average among all trees
            if not index in avg_codisp:
                avg_codisp[index] = 0
            avg_codisp[index] += tree.codisp(index) / num_trees
        
        #calculate current standard deviation
        curr_std = 0  
        if(count >= 2):
            curr_std = (M2 / (count - 1))**(0.5)
        
        # if the difference between anomaly score and mean is more than threshold times the standard deviation, then treat current point as anomaly.
        if(count >= 2 and abs(avg_codisp[index] - moving_average)/(curr_std) > threshold): anomalies.append(index)
        
        # update the variables according to welford's formulas
        count += 1
        delta = avg_codisp[index] - moving_average
        moving_average+= delta / count
        delta2 = avg_codisp[index] - moving_average
        M2 += delta * delta2
        
        yield anomalies
        

