# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

print("Loading dataset...")
# Load the dataset you provided
df = pd.read_csv('house_price_regression_dataset.csv')

# Define features (X) and target (y)
X = df[['Square_Footage', 'Num_Bedrooms', 'Num_Bathrooms', 'Year_Built', 'Lot_Size', 'Garage_Size', 'Neighborhood_Quality']]
y = df['House_Price']

print("Training the Linear Regression model...")
model = LinearRegression()
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'house_price_model.pkl')
print("Model trained successfully and saved as 'house_price_model.pkl'")