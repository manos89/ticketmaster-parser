import requests
import json
import argparse
import datetime
import pandas as pd
from collections import Counter

def validate_date(date):
    """
    validate_date function checks if the user's input is properly formated. If yes, it returns the date in a datetime
    format.
    :param date: date equals to the input we have from the user. That means that it can be either the starting or
                 the ending date.
    :return: This function returns a datetime object which will be modified in the next lines of the program, so we can
             get the proper format.
    """
    try:
        return datetime.datetime.strptime(date, '%Y-%m-%d')
    except AttributeError:
        print("You must provide a proper date of the following format: YYYY-MM-DD")

def format_date(datetime_obj):
    return datetime_obj.strftime("%Y-%m-%dT%H:%M:%SZ")

def check_future_date(start_datetime_object, end_datetime_object):
    """
    This function performs a check of whether the starting and ending dates are within the proper range.
    Proper range means 2 things:
    1) the starting date must be in the future and not in the past.
    2) the ending date must be bigger then the starting date
    """
    if datetime.datetime.now() > start_datetime_object:
        raise ValueError("Your starting date must not be in the past")
    if start_datetime_object > end_datetime_object:
        raise ValueError("Your ending date must be after your starting date")

def make_request(url):
    r = requests.get(url)
    return json.loads(r.text)

def get_args():
    """
    get_args function is used to retrieve the arguments from the command line and return them
    :return: 1) Key, the API key of the user
             2) Start, which is the starting date of the events
             3) End, which is the ending date of the events
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="write your ticketmaster API key")
    parser.add_argument("--start", help="Write the starting date")
    parser.add_argument("--end", help="Write the ending date")
    args = parser.parse_args()
    return args.key, args.start, args.end

def create_the_url(key, start, end):
    return "https://app.ticketmaster.com/discovery/v2/events?apikey={0}&locale=&preferredCountry=us&size=200" \
           "&startDateTime={1}&endDateTime={2}".format(key, start, end)

def get_events(data):
    states_dictionary = {}
    for event in data["_embedded"]["events"]:
        try:
            try:
                states_dictionary[event["_embedded"]["venues"][0]["state"]["stateCode"]].append(event)
            except KeyError:
                states_dictionary[event["_embedded"]["venues"][0]["state"]["stateCode"]] = [event]
        except KeyError:
            pass
    return states_dictionary


def get_artist_with_most_shows(events):
    artists = [artist["_embedded"]["attractions"][0]["id"] for artist in events]
    most_shows_artist = Counter(artists)
    return list(most_shows_artist.keys())[0]

def get_venue_with_most_shows(events):
    venues = [artist["_embedded"]["venues"][0]["id"] for artist in events]
    most_shows_venues = Counter(venues)
    return list(most_shows_venues.keys())[0]

def main():
    key, start, end = get_args()
    start_datetime_object = validate_date(start)
    end_datetime_object = validate_date(end)
    check_future_date(start_datetime_object, end_datetime_object)
    start_formatted = format_date(start_datetime_object)
    end_formatted = format_date(end_datetime_object)
    url = create_the_url(key, start_formatted, end_formatted)
    data = make_request(url)
    states_dictionary = get_events(data)
    for key in states_dictionary.keys():
        artist_id = get_artist_with_most_shows(states_dictionary[key])
        venue_id = get_venue_with_most_shows(states_dictionary[key])
        print(venue_id)



if __name__ == "__main__":
    main()
