# plot_results.py
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load the model
model = joblib.load('fea_surrogate_model.pkl')

# Load the synthetic data
df = pd.read_csv('fea_synthetic_data.csv')

# Features and target
X = df[['length', 'width', 'thickness', 'load', 'youngs_modulus']]
y_true = df['stress']

# Predict with the trained model
y_pred = model.predict(X)

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(y_true, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], color='red', linestyle='--', label='Ideal Prediction')
plt.xlabel('Actual Stress')
plt.ylabel('Predicted Stress')
plt.title('Predicted vs Actual Stress')
plt.legend()
plt.grid(True)
plt.show()
