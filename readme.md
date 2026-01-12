# Bayesian Malaria Prevalence Analysis

A modular Python implementation for understanding Bayesian inference through simulated malaria test data.

## 📋 Features

- **Modular Design**: Separated concerns across multiple files
- **Statistical Functions**: Likelihood, priors, posteriors, credible intervals
- **Visualizations**: Beautiful plots showing Bayesian updating
- **Configurable**: Easy parameter adjustment via config file
- **Educational**: Clear code structure for learning

## Quick Start

### Installation
```bash
# Clone or download the project
cd bayesian_malaria_project

# Install dependencies
pip install -r requirements.txt
```

### Run Analysis
```bash
python scripts/run_analysis.py
```

## 📊 What It Does

1. **Simulates** malaria test data with known prevalence
2. **Computes** likelihood, prior, and posterior distributions
3. **Compares** flat vs informative priors
4. **Visualizes** Bayesian updating process
5. **Generates** publication-quality plots

## 🎓 Learning Objectives

- Understand frequentist likelihood
- Learn Bayesian prior specification
- See how posteriors combine prior + data
- Explore prior sensitivity
- Visualize statistical concepts

## 📁 Project Structure

See project structure diagram above for complete file organization.

## ⚙️ Configuration

Edit `config/config.py` to adjust:
- Sample size
- True prevalence
- Prior parameters
- Visualization settings

## 📖 Usage Examples

### Basic Usage
```python
from config.config import Config
from src.data_simulator import DataSimulator
from src.bayesian_analyzer import BayesianAnalyzer

config = Config()
simulator = DataSimulator(seed=1)
y = simulator.simulate_binary_outcomes(20, 0.7)
# ... continue analysis
```

### Custom Analysis
```python
# Modify config
config = Config()
config.SAMPLE_SIZE = 100
config.PRIOR_INFO_ALPHA = 5
config.PRIOR_INFO_BETA = 5
```

## 📈 Output

- **Plots**: Saved to `outputs/` directory
- **Console**: Summary statistics and credible intervals

## 🤝 Contributing

Feel free to extend with:
- Different likelihood functions
- Alternative priors
- More visualization options
- Interactive Jupyter notebooks

## 📝 License

Educational use - freely available

---

**Author**: Generated for educational purposes
**Date**: 2026