# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load the synthetic data
df = pd.read_csv('fea_synthetic_data.csv')

# Features and target variable
X = df[['length', 'width', 'thickness', 'load', 'youngs_modulus']]
y = df['stress']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choose your model (Random Forest, SVR, MLP)
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Save the trained model
joblib.dump(model, 'fea_surrogate_model.pkl')
