from collections import deque
import numpy as np


def shingle(sequence, size):
    """
    Generator that yields shingles (a rolling window) of a given size.

    Parameters
    ----------
    sequence : iterable
               Sequence to be shingled
    size : int
           size of shingle (window)
    
    Yields
    ------
    np.ndarray
        Points in the rolling window, represented as NumPy arrays.

    Raises
    ------
    IndexError
        If the provided sequence is smaller than the specified window size.
    """

    # Initialize an iterator for the input sequence
    iterator = iter(sequence)

    init = (next(iterator) for _ in range(size))

    window = deque(init, maxlen=size)
    
    # check if window length is greater than the size of whole sequence
    if len(window) < size:
        raise IndexError('Sequence smaller than window size')
    
    # Yield the initial shingle as a NumPy array
    yield np.asarray(window)

    # Iterate over the remaining elements in the sequence
    for elem in iterator:
        window.append(elem)
        yield np.asarray(window)