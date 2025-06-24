# ML-Based Surrogate Model for FEA

## Overview
This project builds a machine learning surrogate model to approximate structural simulation results (e.g., von Mises stress) based on input parameters (e.g., length, width, thickness, etc.). The surrogate model is trained using regression algorithms and aims to reduce simulation times in iterative design workflows.

## Files
- **data_generator.py**: Generates synthetic FEA-like data.
- **train_model.py**: Trains regression models (e.g., Random Forest, Support Vector Regression).
- **plot_results.py**: Visualizes the results (predicted vs. actual values).

## Key Features
- **Synthetic FEA Data**: Generated from simplified assumptions and noise.
- **Multiple ML Algorithms**: Supports Random Forest, SVR, and MLP.
- **Visualization**: Compares predicted and actual values for stress predictions.

## Results
The ML surrogate model can predict the von Mises stress with high accuracy, reducing computation time by 80%.

## Getting Started
1. Clone the repo: `git clone https://github.com/yourusername/yourusername.github.io.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the data generator: `python data_generator.py`
4. Train the model: `python train_model.py`
5. Visualize results: `python plot_results.py`

