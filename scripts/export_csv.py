import pandas as pd
from config import CLEAN_JSON, CSV_DIR

df = pd.read_json(CLEAN_JSON)

df.to_csv(CSV_DIR / "sinnoh_pokedex.csv", index=False)