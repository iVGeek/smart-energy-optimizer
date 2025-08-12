import subprocess
import sys
import os

# Function to upgrade pip and install wheel
def upgrade_pip():
    print("Upgrading pip and installing wheel...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "wheel"])

# Function to install requirements from the requirements.txt file
def install_requirements():
    try:
        print("Upgrading pip and installing required packages...")
        upgrade_pip()
        
        # Install dependencies with no cache, preferring binary wheels
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", 
                               "--prefer-binary", "--no-cache-dir", "--use-feature=fast-deps", 
                               "-i", "https://pypi.org/simple"])

        print("Installation complete.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
        sys.exit(1)

# Main function to run the script
if __name__ == "__main__":
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("requirements.txt file not found. Please make sure it is in the current directory.")
        sys.exit(1)
    
    # Start installing requirements
    install_requirements()


### implement autopilot 
### get pre data_auto