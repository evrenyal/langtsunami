import os
import requests
import json

# Color codes
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Path to the results folder
results_folder_path = 'results'

# API endpoint
url = 'http://localhost:11434/api/generate'

# Get all JSON files in the results folder
json_files = [f for f in os.listdir(results_folder_path) if f.endswith('.json')]

# Initialize an empty list to store all responses
all_responses = []

# Iterate over each JSON file
for json_file in json_files:
    json_file_path = os.path.join(results_folder_path, json_file)
    
    # Read the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Get all value entries in the JSON file
    prompts = data.values()
    
    # Make an API request for each value
    for prompt in prompts:
        try:
            # Create the API request with a timeout
            response = requests.post(url, json={
                'model': 'orca-mini:latest',
                'prompt': prompt,
                'stream': False
            }, timeout=10)
            
            # Check the response
            if response.status_code == 200:
                try:
                    # Parse the response as JSON
                    response_json = response.json()
                    # Get the `response` key from the response
                    response_value = response_json.get('response', 'Response key not found')
                    print(f"Prompt: {prompt}", flush=True)
                    print(f"{GREEN}Response: {response_value}{RESET}", flush=True)
                    
                    # Append the response to the list
                    all_responses.append({
                        'prompt': prompt,
                        'response': response_value
                    })
                except json.JSONDecodeError:
                    print(f"Prompt: {prompt}", flush=True)
                    print(f"{RED}Error: Failed to decode JSON response{RESET}", flush=True)
            else:
                print(f"Prompt: {prompt}", flush=True)
                print(f"{RED}Error: Received status code {response.status_code}{RESET}", flush=True)
        
        except requests.Timeout:
            print(f"Prompt: {prompt}", flush=True)
            print(f"{RED}Error: Request timed out{RESET}", flush=True)
        except requests.RequestException as e:
            print(f"Prompt: {prompt}", flush=True)
            print(f"{RED}Error: {str(e)}{RESET}", flush=True)

# Write all responses to a new JSON file
output_file_path = os.path.join(results_folder_path, 'results/fuzz.json')
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(all_responses, f, ensure_ascii=False, indent=4)
