import random
import time

def simulate_energy_usage():
    while True:
        temperature = random.uniform(15, 35)  # Simulating temperature between 15 and 35°C
        humidity = random.uniform(30, 70)  # Simulating humidity between 30% and 70%
        print(f"Simulated Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%")
        time.sleep(5)  # Sleep for 5 seconds to simulate real-time usage

if __name__ == "__main__":
    simulate_energy_usage()
