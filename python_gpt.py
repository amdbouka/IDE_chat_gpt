'''Important: add your chat_gpt API in .env file'''


import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Get user input for task description
user_prompt = input("Write here: ")

# Define API endpoint and API key
api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.environ['API_KEY']

# Set up request headers
request_header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}
# Set up request data
request_data = {
      "model": "text-davinci-003",
      "prompt": f"write python script to {user_prompt}. provide only code",
      "max_tokens": 1000,
      "temperature": 0.5
}

# Send a POST request to the API endpoint
response = requests.post(api_endpoint, headers=request_header, json=request_data)

# Initialize a serial number for the output file
serial = 1

# Check if a file with the same name already exists, if so, increment the serial number
while os.path.exists(f"file_{serial}.py"):
    serial += 1

# Generate a unique file name
file_name = f"file_{serial}.py"

# If the request is successful, save the response code to the output file
if response.status_code == 200:
    response_text = (response.json()["choices"][0]["text"])
    with open(file_name, "w") as file:
        file.write(response_text)
    print(f"Code saved in '{file_name}'")
else:
    print(f"Request failed with status code {str(response.status_code)}")