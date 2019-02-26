import numpy as np


def square(x):
    """Calculate the square energy of the signal.

    Some more detail about calculating the square signal energy.

    Parameters
    ----------
    x : ndarray
        The signal for which to compute the energy.

    Returns
    -------
    energy : float
        The sum of squares of the input signal.

    """
    return np.sum(x**2)
