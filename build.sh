# Create a virtual environment in the current directory
py -m venv .venv

# Activate the virtual environment
# For Unix/Linux systems, use:
source .venv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install dependencies from the requirements.txt file
pip install -r requirements.txt

# Initialize reflex for the project
reflex init

# Export the frontend part of the project only
reflex export --frontend-only
rm -rf ./public

# Extract the frontend.zip archive to the public directory
# Replace PowerShell command with Unix/Linux command
unzip frontend.zip -d ./public

rm ./frontend.zip

# Deactivate the virtual environment
deactivate