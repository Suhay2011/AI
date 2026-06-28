import requests



# Example of fetching a random joke

url = "https://catfact.ninja/fact"



# Send GET request to fetch a joke

response = requests.get(url)



# Check if the request was successful

if response.status_code == 200:

    fact_data = response.json()

    print(f"fact: {fact_data['fact']}")
else:

    print(f"Failed to retrieve fact. Status code: {response.status_code}")
