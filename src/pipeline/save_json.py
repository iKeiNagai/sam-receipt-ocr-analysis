from pathlib import Path
import json

# Saves JSON data into a structured directory based on its type
def save_json(data: dict, filename: str)-> None:
    data_type = data.get('type')

    if not data_type:
        raise ValueError("Missing Type in data")

    base_dir = Path("xraw-data/processed") / data_type
    base_dir.mkdir(parents=True, exist_ok=True)

    path = base_dir / filename

    with open(path, "w") as file:
        json.dump(data, file, indent=4)

