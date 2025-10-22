import os, json
import requests
    
response = requests.get("https://pokeapi.co/api/v2/pokedex/5/") 
data = response.json()

pokedex = []

for entry in data["pokemon_entries"]:
    
    name = entry["pokemon_species"]["name"] 
    no = entry["entry_number"]
    
    if name == "wormadam":
        response == requests.get("https://pokeapi.co/api/v2/pokemon/wormadam-plant")
    else:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
        
    details = response.json()

    # Extract types
    types = [t["type"]["name"] for t in details["types"]]
    
    # Extract stats
    stats = {s["stat"]["name"]: s["base_stat"] for s in details["stats"]}

    pokedex.append({
        "no": no,
        "name": name,
        "type1": types[0],
        "type2": types[1] if len(types) > 1 else None,
        "hp": stats.get("hp"),
        "atk": stats.get("attack"),
        "def": stats.get("defense"),
        "sp_atk": stats.get("special-attack"),
        "sp_atk": stats.get("special-defense"),
        "spd": stats.get("speed")
        })

# Save all Pokémon details in one JSON file
pokedex_file = "../data/original_sinnoh_pokedex.json"
with open(pokedex_file, "w", encoding="utf-8") as f:
    json.dump(pokedex, f, indent=2)

