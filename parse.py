import requests
import json
import argparse
import datetime

def validate_date(date):
    try:
        return datetime.datetime.strptime(date, '%Y-%m-%d')
    except AttributeError:
        print("You must provide a proper date of the following format: YYYY-MM-DD")

def format_date(datetime_obj):
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
    start_datetime = validate_date(start)
    end_datetime = validate_date(end)


if __name__ == "__main__":
    main()
