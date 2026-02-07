import json
import argparse
from fetcher import fetch_data
from validator import validate_response
from reporter import save_json, save_summary

def load_endpoints():
    with open("config/endpoints.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="API Fetcher Tool")
    parser.add_argument("--endpoint", required=True, help="API endpoint name")
    parser.add_argument("--params", nargs="*", help="Query parameters (key=value)")

    args = parser.parse_args()

    endpoints = load_endpoints()

    if args.endpoint not in endpoints:
        print("Invalid endpoint name")
        return

    endpoint = endpoints[args.endpoint]
    url = endpoint["url"]

    params = {}
    if args.params:
        for p in args.params:
            key, value = p.split("=")
            params[key] = value

    data = fetch_data(url, params)
    save_json(data)

    valid, message = validate_response(data)
    save_summary(message)

    print("Request completed.")
    print("Summary:", message)

if __name__ == "__main__":
    main()
