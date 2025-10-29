# Get pokedex data from pokeapi, put it into a json file
import os, json
from config import BASE_URL, POKEDEX_URL
import requests
import pandas as pd

# Request data from pokeapi
response = requests.get(BASE_URL + POKEDEX_URL) 
data = response.json()

# Build a list to save to a json file
pokedex_list = []

for entry in data["pokemon_entries"]:
    
    # Extract name and number
    name = entry["pokemon_species"]["name"] 
    no = entry["entry_number"]
    
    # To get the pokemon type(s) and stats, we need another api call
    # Do NOT use pokemon name, use id, as pokemon like wormadam cause issues
    # since their names are 'wormadam-plant' and such
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

# Save in JSON file
pokedex_file = "data/json/sinnoh_pokedex_raw.json"

with open(pokedex_file, "w", encoding="utf-8") as f:
    json.dump(pokedex_list, f, indent=2)
    

