"""
Visualization functions for Bayesian analysis
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

class Visualizer:
    def __init__(self, config):
        """Initialize visualizer with configuration"""
        self.config = config
        
        # Set style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = config.FIGURE_SIZE
        plt.rcParams['figure.dpi'] = config.DPI
        
        # Create output directory
        if config.SAVE_PLOTS:
            Path(config.OUTPUT_DIR).mkdir(exist_ok=True)
    
    def plot_likelihood(self, theta, likelihood, mle, theta_true):
        """Plot likelihood function"""
        fig, ax = plt.subplots()
        
        ax.plot(theta, likelihood, 'k-', linewidth=2, label='Likelihood')
        ax.axvline(mle, color='red', linestyle='--', 
                   linewidth=2, label=f'MLE = {mle:.3f}')
        ax.axvline(theta_true, color='purple', linestyle='--', 
                   linewidth=2, label=f'True θ = {theta_true:.3f}')
        
        ax.set_xlabel('θ (Prevalence)', fontsize=8)
        ax.set_ylabel('Likelihood', fontsize=8)
        ax.set_title('Likelihood Function', fontsize=6, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        self._save_figure(fig, 'likelihood')
        return fig
    
    def plot_bayesian_updating(self, theta, results, data, theta_true):
        """Plot comprehensive Bayesian updating visualization"""
        fig, ax = plt.subplots()
        
        # Normalize curves
        likelihood_norm = results['likelihood'] / np.max(results['likelihood'])
        prior_flat_norm = results['prior_flat'] / np.max(results['prior_flat'])
        posterior_flat_norm = results['posterior_flat'] / np.max(results['posterior_flat'])
        
        # Plot
        ax.plot(theta, likelihood_norm, 'm-', linewidth=1.5, 
                label='Likelihood', alpha=0.8)
        ax.plot(theta, prior_flat_norm, 'b--', linewidth=2, 
                label='Prior (flat)', alpha=0.7)
        ax.plot(theta, posterior_flat_norm, 'r-', linewidth=2, 
                label='Posterior (flat)', alpha=0.8)
        
        # Reference lines
        ax.axvline(data['mle'], color='red', linestyle=':', 
                   linewidth=1.5, alpha=0.5)
        ax.axvline(theta_true, color='purple', linestyle=':', 
                   linewidth=1.5, alpha=0.5)
        
        ax.set_xlabel('θ (Prevalence)', fontsize=8)
        ax.set_ylabel('Scaled Density', fontsize=8)
        ax.set_title('Bayesian Updating: Prior → Posterior', 
                    fontsize=10, fontweight='bold')
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3)
        
        self._save_figure(fig, 'bayesian_updating')
        return fig
    
    def plot_prior_sensitivity(self, theta, results, data, theta_true):
        """Plot comparison of different priors"""
        fig, ax = plt.subplots()
        
        # Normalize
        likelihood_norm = results['likelihood'] / np.max(results['likelihood'])
        prior_flat_norm = results['prior_flat'] / np.max(results['prior_flat'])
        posterior_flat_norm = results['posterior_flat'] / np.max(results['posterior_flat'])
        prior_info_norm = results['prior_info'] / np.max(results['prior_info'])
        posterior_info_norm = results['posterior_info'] / np.max(results['posterior_info'])
        
        # Plot
        # ax.plot(theta, likelihood_norm, 'k-', linewidth=3, 
                # label='Likelihood', alpha=0.8)
        ax.plot(theta, prior_flat_norm, 'b--', linewidth=2, 
                label='Prior (flat)', alpha=0.6)
        ax.plot(theta, posterior_flat_norm, 'r-', linewidth=2, 
                label='Posterior (flat)', alpha=0.8)
        ax.plot(theta, prior_info_norm, color='gray', linestyle='-', 
                linewidth=2, label='Prior (informative)', alpha=0.6)
        ax.plot(theta, posterior_info_norm, 'g-', linewidth=2, 
                label='Posterior (informative)', alpha=0.8)
        
        ax.set_xlabel('θ (Prevalence)', fontsize=8)
        ax.set_ylabel('Density', fontsize=8)
        ax.set_title('Prior Sensitivity Analysis', 
                    fontsize=10, fontweight='bold')
        ax.legend(loc='best', fontsize=8)
        ax.grid(False)
        
        self._save_figure(fig, 'prior_sensitivity')
        return fig
    
    def plot_all(self, theta, results, data, theta_true):
        """Generate all plots"""
        figs = []
        figs.append(self.plot_likelihood(theta, results['likelihood'], 
                                        data['mle'], theta_true))
        figs.append(self.plot_bayesian_updating(theta, results, 
                                                data, theta_true))
        figs.append(self.plot_prior_sensitivity(theta, results, 
                                                data, theta_true))
        return figs
    
    def _save_figure(self, fig, name):
        """Save figure to output directory"""
        if self.config.SAVE_PLOTS:
            filepath = Path(self.config.OUTPUT_DIR) / f"{name}.{self.config.PLOT_FORMAT}"
            fig.savefig(filepath, bbox_inches='tight', dpi=self.config.DPI)
            print(f"Saved: {filepath}")