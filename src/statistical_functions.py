"""
Core statistical functions for Bayesian analysis
"""
import numpy as np
from scipy import stats
from scipy.special import beta as beta_func

class StatisticalFunctions:
    
    @staticmethod
    def binomial_likelihood(k, n, theta):
        """
        Compute binomial likelihood P(data | theta)
        
        Parameters:
        -----------
        k : int
            Number of successes observed
        n : int
            Number of trials
        theta : float or np.array
            Probability parameter(s)
        
        Returns:
        --------
        likelihood : float or np.array
            Likelihood value(s)
        """
        return stats.binom.pmf(k, n, theta)
    
    @staticmethod
    def beta_prior(theta, alpha, beta):
        """
        Compute Beta prior distribution
        
        Parameters:
        -----------
        theta : np.array
            Grid of theta values
        alpha, beta : float
            Beta distribution parameters
        
        Returns:
        --------
        prior : np.array
            Prior density values
        """
        return stats.beta.pdf(theta, alpha, beta)
    
    @staticmethod
    def beta_posterior(theta, alpha_prior, beta_prior, k, n):
        """
        Compute Beta posterior distribution
        
        Parameters:
        -----------
        theta : np.array
            Grid of theta values
        alpha_prior, beta_prior : float
            Prior Beta parameters
        k : int
            Number of successes observed
        n : int
            Number of trials
        
        Returns:
        --------
        posterior : np.array
            Posterior density values
        alpha_post, beta_post : float
            Posterior Beta parameters
        """
        alpha_post = alpha_prior + k
        beta_post = beta_prior + (n - k)
        posterior = stats.beta.pdf(theta, alpha_post, beta_post)
        return posterior, alpha_post, beta_post
    
    @staticmethod
    def normalize_curve(values):
        """Normalize curve to have maximum value of 1"""
        max_val = np.max(values)
        if max_val > 0:
            return values / max_val
        return values
    
    @staticmethod
    def credible_interval(alpha_post, beta_post, credibility=0.95):
        """
        Calculate credible interval for posterior
        
        Parameters:
        -----------
        alpha_post, beta_post : float
            Posterior Beta parameters
        credibility : float
            Credibility level (e.g., 0.95 for 95% CI)
        
        Returns:
        --------
        lower, upper : float
            Bounds of credible interval
        """
        lower = stats.beta.ppf((1 - credibility) / 2, alpha_post, beta_post)
        upper = stats.beta.ppf(1 - (1 - credibility) / 2, alpha_post, beta_post)
        return lower, upper