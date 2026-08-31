import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.

    Args:
        animal_name (str): The name of the animal to search for

    Returns:
        list: A list of animals matching the search query
              Returns empty list if no animals found or error occurs
    """

    # Check if API_KEY is set
    if not API_KEY:
        print("Error: API_KEY not found in .env file!")
        return []

    params = {"name": animal_name}
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(API_URL, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: API returned status code {response.status_code}")
            return []

    except requests.RequestException as e:
        print(f"Error: Network error while fetching data - {e}")
        return []
    except Exception as e:
        print(f"Error: