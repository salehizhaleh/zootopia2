import data_fetcher


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

    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'      <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    if "type" in animal_obj:
        output += f'      <strong>Type:</strong> {animal_obj["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def create_error_message(animal_name):
    error_html = f'''
    <div class="error-message">
        <h2>The animal "{animal_name}" does not exist.</h2>
        <p>Please try searching for a different animal.</p>
    </div>
    '''
    return error_html


# Main Program
print("=" * 50)
print("Zootopia - Web Generator")
print("=" * 50)

animal_name = input("Enter a name of an animal: ").strip()

if not animal_name:
    print("Error: Please enter an animal name!")
    exit()

print(f"Searching for: {animal_name}...")

# Get data from data_fetcher
animals_data = data_fetcher.fetch_data(animal_name)

try:
    html_content = read_html("animals_template.html")
except FileNotFoundError:
    print("Error: animals_template.html not found!")
    exit()

if animals_data:
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    print(f"Found {len(animals_data)} animal(s)")
else:
    output = create_error_message(animal_name)
    print(f"No animals found with name '{animal_name}'")

final_html = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

write_html("animals.html", final_html)
print("Website was successfully generated to the file animals.html.")
print("=" * 50)