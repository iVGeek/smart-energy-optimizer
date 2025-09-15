import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load("models/energy_optimizer_model.pkl")

# Function to predict energy usage
def predict_energy_usage(temperature, humidity):
    input_data = pd.DataFrame([[temperature, humidity]], columns=["temperature", "humidity"])
    return model.predict(input_data)[0]

# Function to visualize predicted vs real energy usage
def visualize_predictions(real, predicted):
    plt.scatter(real, predicted, color='blue')
    plt.xlabel("Real Energy Usage")
    plt.ylabel("Predicted Energy Usage")
    plt.title("Predicted vs Real Energy Usage")
    plt.show()

if __name__ == "__main__":
    # Real energy usage values
    real_usage = [120, 150, 130, 180, 160, 125]
    
    # Simulating predictions for the corresponding inputs
    predicted_usage = [
        predict_energy_usage(20, 50), 
        predict_energy_usage(25, 60), 
        predict_energy_usage(22, 55), 
        predict_energy_usage(30, 70), 
        predict_energy_usage(28, 65), 
        predict_energy_usage(21, 60)
    ]
    
    visualize_predictions(real_usage, predicted_usage)



####opt_get_all_tp_=all_tine_get