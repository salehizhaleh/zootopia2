import data_fetcher


def read_html(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_html(file_path, content):
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    characteristics = animal_obj.get("characteristics", {})

    if "diet" in characteristics:
        output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'      <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    if "type" in characteristics:
        output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

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


print("=" * 50)
print("Zootopia - Web Generator")
print("=" * 50)

animal_name = input("Enter a name of an animal: ").strip()

if not animal_name:
    print("Error: Please enter an animal name!")
    exit()

print(f"🔍 Searching for: {animal_name}...")

animals_data = data_fetcher.fetch_data(animal_name)

try:
    html_content = read_html("template.html")
except FileNotFoundError:
    print(" Error: template.html not found!")
    exit()

if animals_data:
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    print(f"✅ Found {len(animals_data)} animal(s)")
else:
    output = create_error_message(animal_name)
    print(f"No animals found with name '{animal_name}'")

final_html = html_content.replace("<!-- ANIMALS_PLACEHOLDER -->", output)

write_html("animals.html", final_html)
print("Website was successfully generated to the file animals.html.")
print("=" * 50)