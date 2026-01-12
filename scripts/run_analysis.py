"""
Main script to run the complete Bayesian malaria analysis
"""
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent))

from config.config import Config
from src.data_simulator import DataSimulator
from src.bayesian_analyzer import BayesianAnalyzer
from src.visualizer import Visualizer
import matplotlib.pyplot as plt

def main():
    """Run complete analysis pipeline"""
    print("=" * 60)
    print("BAYESIAN MALARIA PREVALENCE ANALYSIS")
    print("=" * 60)
    
    # Load configuration
    config = Config()
    
    #  Simulate data
    print("\n[1/4] Simulating malaria test data...")
    simulator = DataSimulator(seed=config.RANDOM_SEED)
    y = simulator.simulate_binary_outcomes(
        n=config.SAMPLE_SIZE,
        theta_true=config.TRUE_PREVALENCE
    )
    data = simulator.get_summary_stats(y)
    data['y'] = y
    
    print(f"   Tested: {data['n']} people")
    print(f"   Positive: {data['positives']} tests")
    print(f"   Observed prevalence: {data['prevalence_observed']:.3f}")
    
    # Bayesian analysis
    print("\n[2/4] Running Bayesian analysis...")
    analyzer = BayesianAnalyzer(data, config)
    results = analyzer.run_full_analysis()
    
    print("\n" + analyzer.get_summary())
    
    #  Visualization
    print("\n[3/4] Generating visualizations...")
    visualizer = Visualizer(config)
    figs = visualizer.plot_all(
        analyzer.theta,
        results,
        data,
        config.TRUE_PREVALENCE
    )
    
    #Display
    print("\n[4/4] Displaying plots...")
    plt.show()
    
    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()