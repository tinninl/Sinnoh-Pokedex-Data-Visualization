# This script utilizes the PokeAPI, a free open-source API, 
# to fetch the necessary pokemon data and cache it into a JSON file

import json
import requests
from config import BASE_URL, POKEDEX_URL, JSON_RAW_FILENAME

# Step 1: Fetch the pokedex data
# This will give us the list of all the pokemon we want
response = requests.get(BASE_URL + POKEDEX_URL) 
data = response.json()

# Step 2: Build a list of pokemon information to be later saved to a JSON file
# We will gather the pokemon's number, name, type(s), and base stats (hp, atk, def, etc)

pokedex_list = []

for entry in data["pokemon_entries"]:
    
    # Extract name and number
    no = entry["entry_number"]
    name = entry["pokemon_species"]["name"] 
    
    # In order to gather types and base stats, we need to make an individual call 
    # for each and every pokemon.
    
    # We can extract the id number from the url to make our API calls
    species_url = entry["pokemon_species"]["url"]
    species_id = species_url.rstrip("/").split("/")[-1]   
    
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{species_id}/")
    data = response.json()

    # Extract types
    types = [t["type"]["name"] for t in data["types"]]
    type1 = types[0]
    type2 = types[1] if len(types) > 1 else None
    
    # Extract stats
    stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
    hp = stats.get("hp")
    atk = stats.get("attack")
    defense = stats.get("defense")
    sp_atk = stats.get("special-attack")
    sp_def = stats.get("special-defense")
    spd = stats.get("speed")

    # Add the pokemon's information to the list
    pokedex_list.append({
        "No": no, 
        "Name": name, 
        "Type 1": type1, 
        "Type 2": type2,
        "Hp": hp,
        "Atk": atk,
        "Def": defense,
        "Sp. Atk": sp_atk,
        "Sp. Def": sp_def,
        "Spd": spd
    })

# Save the list in a JSON file
# We will title it "raw" for now and later we will create a "clean" JSON file
pokedex_file = JSON_RAW_FILENAME

with open(pokedex_file, "w", encoding="utf-8") as f:
    json.dump(pokedex_list, f, indent=2)
    

