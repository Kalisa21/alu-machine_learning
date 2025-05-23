#!/usr/bin/env python3
"""
Exponential distribution
"""


class Exponential():
    """
    exponential distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        data is a list of the data to be used to estimate the distribution
        lambtha is the expected number of occurences in a given interval
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given time period
        """
        if x < 0:
            return 0
        e = 2.7182818285
        return (self.lambtha * (e ** (-self.lambtha * x)))

    def cdf(self, x):
        """
        Calculates the cdf for a given time period
        """
        if x < 0:
            return 0
        e = 2.7182818285
        return (1 - (e ** (-self.lambtha * x)))
