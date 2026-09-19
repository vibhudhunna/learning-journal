import requests

print("--- Initiating Network Request ---")

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

print(f"Server Status: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    
    # Extract the exact data points we need
    name = data['name']
    city = data['address']['city']
    
    # Format them cleanly
    print(f"Target Acquired -> Name: {name} | Location: {city}")
    
else:
    print("Failed to retrieve data.")