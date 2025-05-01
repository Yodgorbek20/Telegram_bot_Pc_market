import json

def read_db():
    with open("database.json", "r", encoding="utf-8") as f:
        return json.load(f)

def write_db(data):
    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)