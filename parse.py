import requests
import json
import argparse
import datetime

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

def get_events():
    pass

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

def main():
    key, start, end = get_args()
    start_datetime_object = validate_date(start)
    end_datetime_object = validate_date(end)
    check_future_date(start_datetime_object, end_datetime_object)
    start_formatted = format_date(start_datetime_object)
    end_formatted = format_date(end_datetime_object)


if __name__ == "__main__":
    main()
