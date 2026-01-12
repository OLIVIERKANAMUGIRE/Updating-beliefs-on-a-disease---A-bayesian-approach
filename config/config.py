"""
Configuration parameters for Bayesian malaria analysis
"""

class Config:
    # Simulation parameters
    SAMPLE_SIZE = 100

    RANDOM_SEED = 1

    TRUE_PREVALENCE = 0.7
    
    # Prior parameters
    PRIOR_FLAT_ALPHA = 1
    PRIOR_FLAT_BETA = 1
    PRIOR_INFO_ALPHA = 2
    PRIOR_INFO_BETA = 18
    
    # Visualization parameters
    THETA_GRID_SIZE = 1000
    FIGURE_SIZE = (4, 4)
    DPI = 600
    
    # Output settings
    SAVE_PLOTS = True
    OUTPUT_DIR = "outputs"
    PLOT_FORMAT = "png"

    #http://localhost:5173/