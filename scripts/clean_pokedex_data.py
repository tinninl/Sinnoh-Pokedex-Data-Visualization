import json
import pandas as pd
from config import JSON_RAW_FILENAME, JSON_CLEAN_FILENAME

# Load raw json 
with open(JSON_RAW_FILENAME, "r") as f:
    df = pd.read_json(f)

# Capitalize Pokémon names and types
df["Name"] = df["Name"].str.capitalize()
df["Type 1"] = df["Type 1"].str.capitalize()
df["Type 2"] = df["Type 2"].str.capitalize()

# Replace null values with the empty string "" in the "Type 2" column
df['Type 2'] = df['Type 2'].fillna("")

df.to_json(JSON_CLEAN_FILENAME,orient="records",indent=2)


