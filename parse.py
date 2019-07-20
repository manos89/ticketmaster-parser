import requests
import json
import argparse

def validate_date(date):
    pass

def get_events():
    pass

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="write your ticketmaster API key")
    parser.add_argument("--start", help="Write the starting date")
    parser.add_argument("--end", help="Write the ending date")
    args = parser.parse_args()
    return args.key, args.start, args.end

def main():
    key, start, end = get_args()
    print(key)

if __name__ == "__main__":
    main()
