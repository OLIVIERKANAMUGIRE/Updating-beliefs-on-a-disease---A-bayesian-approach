"""
Module for simulating malaria test data
"""
import numpy as np

class DataSimulator:
    def __init__(self, seed=None):
        """Initialize the data simulator with optional random seed"""
        if seed is not None:
            np.random.seed(seed)
    
    def simulate_binary_outcomes(self, n, theta_true):
        """
        Simulate binary test outcomes (positive/negative)
        
        Parameters:
        -----------
        n : int
            Number of people tested
        theta_true : float
            True malaria prevalence (0 to 1)
        
        Returns:
        --------
        y : np.array
            Binary outcomes (1 = positive, 0 = negative)
        """
        y = np.random.binomial(1, theta_true, n)
        return y
    
    def get_summary_stats(self, y):
        """Calculate summary statistics from simulated data"""
        return {
            'n': len(y),
            'positives': np.sum(y),
            'prevalence_observed': np.mean(y),
            'mle': np.mean(y)
        }