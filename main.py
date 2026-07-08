import json
import requests

API_KEY = "ibAb9WY4Vxv2y9PK5H61ODXMc8LCzFmpZFigsrCc"
API_URL = "https://api.api-ninjas.com/v1/animals"


def load_data_from_api(animal_name):
    params = {"name": animal_name}
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(API_URL, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"error: {response.status_code}")
        return []


def read_html(file_path):
    with open(file_path, "r") as handle:
        return handle.read()


def write_html(file_path, content):
    with open(file_path, "w") as handle:
        handle.write(content)


def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    if "diet" in animal_obj:
        output += f'      <strong>Diet:</strong> {animal_obj["diet"]}<br/>\n'
    if "locations" in animal_obj:
        output += f'      <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
    if "type" in animal_obj:
        output += f'      <strong>Type:</strong> {animal_obj["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


animal_name = input("Enter a name of an animal: ").strip()

if not animal_name:
    print(" Please enter an animal name!")
    exit()

html_content = read_html("animals_template.html")
animals_data = load_data_from_api(animal_name)

if animals_data:
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    final_html = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

    write_html("animals.html", final_html)
    print("Website was successfully generated to the file animals.html.")
else:
    print(f" No animals found with name '{animal_name}'")