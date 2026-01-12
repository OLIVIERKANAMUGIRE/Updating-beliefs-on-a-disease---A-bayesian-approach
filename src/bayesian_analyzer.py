"""
Main Bayesian analysis logic
"""
import numpy as np
from .statistical_functions import StatisticalFunctions

class BayesianAnalyzer:
    def __init__(self, data, config):
        """
        Initialize Bayesian analyzer
        
        Parameters:
        -----------
        data : dict
            Dictionary with 'y' (outcomes) and summary stats
        config : Config
            Configuration object
        """
        self.data = data
        self.config = config
        self.stats_func = StatisticalFunctions()
        
        # Create theta grid
        self.theta = np.linspace(0, 1, config.THETA_GRID_SIZE)
        
        # Initialize results storage
        self.results = {}
    
    def compute_likelihood(self):
        """Compute likelihood function"""
        k = self.data['positives']
        n = self.data['n']
        self.results['likelihood'] = self.stats_func.binomial_likelihood(
            k, n, self.theta
        )
        return self.results['likelihood']
    
    def compute_flat_prior_analysis(self):
        """Compute analysis with flat Beta(1,1) prior"""
        alpha = self.config.PRIOR_FLAT_ALPHA
        beta = self.config.PRIOR_FLAT_BETA
        
        # Prior
        self.results['prior_flat'] = self.stats_func.beta_prior(
            self.theta, alpha, beta
        )
        
        # Posterior
        k = self.data['positives']
        n = self.data['n']
        posterior, alpha_post, beta_post = self.stats_func.beta_posterior(
            self.theta, alpha, beta, k, n
        )
        
        self.results['posterior_flat'] = posterior
        self.results['flat_params'] = (alpha_post, beta_post)
        
        # Credible interval
        lower, upper = self.stats_func.credible_interval(alpha_post, beta_post)
        self.results['flat_ci'] = (lower, upper)
        
        return self.results
    
    def compute_informative_prior_analysis(self):
        """Compute analysis with informative Beta(10,3) prior"""
        alpha = self.config.PRIOR_INFO_ALPHA
        beta = self.config.PRIOR_INFO_BETA
        
        # Prior
        self.results['prior_info'] = self.stats_func.beta_prior(
            self.theta, alpha, beta
        )
        
        # Posterior
        k = self.data['positives']
        n = self.data['n']
        posterior, alpha_post, beta_post = self.stats_func.beta_posterior(
            self.theta, alpha, beta, k, n
        )
        
        self.results['posterior_info'] = posterior
        self.results['info_params'] = (alpha_post, beta_post)
        
        # Credible interval
        lower, upper = self.stats_func.credible_interval(alpha_post, beta_post)
        self.results['info_ci'] = (lower, upper)
        
        return self.results
    
    def run_full_analysis(self):
        """Run complete Bayesian analysis"""
        self.compute_likelihood()
        self.compute_flat_prior_analysis()
        self.compute_informative_prior_analysis()
        return self.results
    
    def get_summary(self):
        """Generate text summary of results"""
        summary = []
        summary.append(f"Sample size: {self.data['n']}")
        summary.append(f"Positive tests: {self.data['positives']}")
        summary.append(f"MLE: {self.data['mle']:.3f}")
        
        if 'flat_ci' in self.results:
            lower, upper = self.results['flat_ci']
            summary.append(f"95% CI (flat prior): [{lower:.3f}, {upper:.3f}]")
        
        if 'info_ci' in self.results:
            lower, upper = self.results['info_ci']
            summary.append(f"95% CI (informative prior): [{lower:.3f}, {upper:.3f}]")
        
        return "\n".join(summary)