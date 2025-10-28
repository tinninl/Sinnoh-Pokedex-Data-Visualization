from pathlib import Path

data_dir = Path("data") / "clean"

BASE_DIR = Path(__file__).parent.parent
JSON_CLEAN = BASE_DIR / "data" / "json" / "sinnoh_pokedex_clean.json"
CSV_DIR = BASE_DIR / "data" / "csv"