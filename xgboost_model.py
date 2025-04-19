import pandas as pd
import xgboost as xgb
import joblib

# Load and preprocess the dataset
df = pd.read_csv('train.csv')
df.dropna(inplace=True)
X = df.drop('Item_Outlet_Sales', axis=1)._get_numeric_data()
y = df['Item_Outlet_Sales']

# Train model
model = xgb.XGBRegressor()
model.fit(X, y)

# Save the model
joblib.dump(model, 'xgb_model.pkl')
