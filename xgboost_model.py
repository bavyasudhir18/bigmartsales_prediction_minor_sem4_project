import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import xgboost as xgb
import joblib

# ========== Load Dataset ==========
df = pd.read_csv('train.csv')
print(f"Initial Shape: {df.shape}")

# ========== Preprocessing ==========
# Replace inconsistent categories
df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({
    'LF': 'Low Fat', 'low fat': 'Low Fat', 'reg': 'Regular'
})

# Fill missing values
df['Item_Weight'].fillna(df['Item_Weight'].median(), inplace=True)
df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0], inplace=True)

# Replace 0s in visibility
df['Item_Visibility'] = df['Item_Visibility'].replace(0, df['Item_Visibility'].median())

# Drop identifiers
df.drop(columns=['Item_Identifier', 'Outlet_Identifier'], inplace=True)

# Encode categorical variables
label_encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# ========== Define Features & Target ==========
X = df.drop('Item_Outlet_Sales', axis=1)
y = df['Item_Outlet_Sales']

# ========== Train-Test Split ==========
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ========== Hyperparameter Tuning ==========
print("\nTuning XGBoost...")

param_grid = {
    'n_estimators': [100, 200],
    'learning_rate': [0.05, 0.1],
    'max_depth': [3, 5, 7],
    'subsample': [0.8, 1.0]
}

xgb_model = xgb.XGBRegressor(random_state=42)
grid = GridSearchCV(estimator=xgb_model, param_grid=param_grid,
                    scoring='neg_mean_squared_error', cv=3, n_jobs=-1, verbose=1)

grid.fit(X_train, y_train)

print(f"Best Parameters: {grid.best_params_}")

# ========== Final Model ==========
best_model = grid.best_estimator_

# ========== Evaluation ==========
y_pred = best_model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"\n✅ Model Performance:")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# ========== Save Model ==========
joblib.dump(best_model, 'xgb_model.pkl')
print("\nModel saved as 'xgb_model.pkl'")
