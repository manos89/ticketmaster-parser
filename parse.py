import requests
import json
import argparse
import datetime
import csv
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
    """
    returns an objecet in the proper format for making the request YYYY-MM-DDTHH:mm:ssZ
    :param datetime_obj: a datetime object (starting and ending date)
    :return: a string which has the proper format
    """
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
    """
    Making the request and returns the response in JSON format
    :param url: The url used to make the call
    :return: returns the response in a JSON format
    """
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
    """
    :param key: The API key
    :param start: Starting Date in the appropriate string format
    :param end: Ending Date in the appropriate string format
    :return: the url properly formatted, containng the key and both the starting and ending dates
    """
    return "https://app.ticketmaster.com/discovery/v2/events.json?apikey={0}&size=200" \
           "&startDateTime={1}&endDateTime={2}&classificationName=Musician".format(key, start, end)


def get_events(data):
    """
    This function takes the response and creates a new dictionary in the format that is more useful for us.
    The format is like this {"stateName": [event1, event2]}, where event1 and event2 are objects too.
    :param data: The response in a JSON format
    :return: A dictionary that has state names as keys and array of events as value
    """
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
    """
    This function returns the artist with the most shows in a state. To achieve that we get as a parameter the events
    in a state and we use the Counter function from the collections library.
    First we get all the artist names in this state. Then we sort them (using the Counter) according on how many times
    they appear in each state and we get the first (it's a reverse sort)
    :param events: Events belonging to a specific state
    :return: The artist with the most shows in each state
    """
    artists = [artist["_embedded"]["attractions"][0]["name"] for artist in events]
    most_shows_artist = Counter(artists)
    return list(most_shows_artist.keys())[0]


def get_venue_with_most_shows(events):
    """
    This function returns the venues with the most shows in a state. To achieve that we get as a parameter the events
    in a state and we use the Counter function from the collections library.
    First we get all the venues names in this state. Then we sort them (using the Counter) according on how many times
    they appear in each state and we get the first (it's a reverse sort)
    :param events: Events belonging to a specific state
    :return: The venues with the most shows in each state
    """
    venues = [artist["_embedded"]["venues"][0]["name"] for artist in events]
    most_shows_venues = Counter(venues)
    return list(most_shows_venues.keys())[0]


def most_expensive_ticket(events):
    """
    To get the event with the most expensive price we have to sort them according to the price and then return the
    needed variables of the first event.
    :param events: Events belonging to a specific state
    :return: 3 variable.
            1) Name of the event with the most expensive price
            2) Most expensive price
            3) Name of the artist with the most expensive price
    """
    try:
        sorted_by_price = sorted([e for e in events if "priceRanges" in e.keys()],
                                 key=lambda k: k['priceRanges'][0]["max"],
                                 reverse=True)
        return sorted_by_price[0]["name"], sorted_by_price[0]["priceRanges"][0]["max"], \
               sorted_by_price[0]["_embedded"]["attractions"][0]["name"]
    except IndexError:
        print("The events don't have a price")
        return "NA", "NA", "NA"


def main():
    # 1st Step
    key, start, end = get_args()
    start_datetime_object = validate_date(start)
    end_datetime_object = validate_date(end)
    check_future_date(start_datetime_object, end_datetime_object)
    start_formatted = format_date(start_datetime_object)
    end_formatted = format_date(end_datetime_object)
    # 2nd step
    url = create_the_url(key, start_formatted, end_formatted)
    data = make_request(url)
    # 3rd step
    states_dictionary = get_events(data)
    csvfile = open('results.csv', 'w')
    spamwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(
        ["State", "Musician with the most events", "Venue with the most events", "Most expensive ticket",
         "Most expensive ticket event name", "Most expensive ticket artist"])
    for key in states_dictionary.keys():
        artist = get_artist_with_most_shows(states_dictionary[key])
        venue = get_venue_with_most_shows(states_dictionary[key])
        max_event, max_price, max_artist = most_expensive_ticket(states_dictionary[key])
        spamwriter.writerow([key, artist, venue, max_price, max_event, max_artist])
    csvfile.close()


if __name__ == "__main__":
    main()
