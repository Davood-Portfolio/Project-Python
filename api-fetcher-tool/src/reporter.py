import json

def save_json(data, path="output/response.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def save_summary(message, path="output/summary.txt"):
    with open(path, "w", encoding="utf-8") as f:
        f.write("API Fetch Summary\n")
        f.write("=================\n")
        f.write(message + "\n")
