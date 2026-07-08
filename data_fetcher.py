import requests

API_KEY = "ibAb9WY4Vxv2y9PK5H61ODXMc8LCzFmpZFigsrCc"
API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    params = {"name": animal_name}
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(API_URL, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return []