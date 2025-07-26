import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
data = pd.read_csv("data/energy_data.csv")

# Preprocess the data
X = data[["temperature", "humidity"]]
y = data["energy_usage"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, "models/energy_optimizer_model.pkl")
print("Model trained and saved successfully.")


### end_code

#### implement autopilot 