# data_generator.py
import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)
n_samples = 500

# Simulated FEA inputs
data = {
    'length': np.random.uniform(1.0, 10.0, n_samples),
    'width': np.random.uniform(0.5, 5.0, n_samples),
    'thickness': np.random.uniform(0.1, 2.0, n_samples),
    'load': np.random.uniform(100, 1000, n_samples),
    'youngs_modulus': np.random.uniform(1e5, 2e5, n_samples),
}

df = pd.DataFrame(data)

# Synthetic stress output (von Mises-like)
df['stress'] = (
    df['load'] * df['length'] / (df['width'] * df['thickness']) +
    np.random.normal(0, 5, n_samples)  # Add small noise
)

df.to_csv("fea_synthetic_data.csv", index=False)
print("Synthetic FEA data saved to fea_synthetic_data.csv")
