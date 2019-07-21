# ticketmaster-parser

# Project Explanation
The purpose of this project is to collect music events from ticketmaster's website using its API, and then export the results to a CSV file, according to the provided schema.

To make the solution easier to understand, it will be divided into 3 parts:
## 1) Getting all the inputs and formatting the date
  - User inputs his/her API key, the starting date and the ending date. All the events will be between this date range.
  - First, we have to convert the date from a string to a datetime object. Datetime objects are useful because they come with some         methods and some attributes. In our case, we have to convert them to this format so we can compare them to our current date and also to     compare the starting and ending date (ending date must be after starting date).
  - Then we make the comparison, which is similar to comparing numbers/integers. In real life we can check if 10<11, and in the same way       we can find out if starting date < ending date.
  - Finally, we have to convert them from a datetime object to a text in a format that can be used to make the request (YYYY-MM-               DDTHH:mm:ssZ)
  
### Summary of first  step:
Take the input -> check dates format -> convert dates to datetime objects -> perform check of whether those datetime objects are correct -> convert the datetime objects back to string/text
## 2) Making the request
  - Create the url. We have a URL which has 3 placeholders. We replace them with the API key, starting date, and ending date                 accordingly.
  - Make the request and return the results in a JSON format. Making the request is exactly the same as visiting a webpage in our         browser. The browser displays the page, whereas when we make the request from python we receive the code of this page.
  
  ### Summary of second step:
  create the url -> make the request -> return the response(code of the page) in a JSON format.
## 3) Collecting the needed results
  This is the most tricky step, as I had to group the events by state in order to collect the results.
  Assuming that you are familiar with lists and dictionaries I will try to explain the logic behind this grouping.
  First, after converting the API's response to JSON I ended up with a list of dictionaries. Each dictionary contains a different event.
  You can find the state nested under the ["venues"][0]["state"] field.
  I did the grouping in this way:
  a) Creating a new dictionary (states_dictionary)
  b) Iterating through all the events
  c) Adding the state as a key in this new dictionary and then appending the event as a value.
  
  To get a better view, here's an example of the states_dictionary:
  original_response = [{event1}, {event2}, {event3}, {event4}]. 
  Let's assume that event1 and event3 belong to California, event2 to New York, and event4 to Texas.
  Our new states_dictionary will have this format:

  states_dictionary = {"California": [{event1}, {event3}], "New York": [{event2}], "Texas": [{event4}]}

  Getting the most expensive event, price, and artist, after having done this was relatively simple. I could iterate through each       state and access each state's events separately, and then I was able to get all the artists'/venues' names and find the one that         repeats itself the most. Finally, I sorted the events by price and picked the first price, name, and artist's name, and then wrote the results to a CSV.
  
  ### Summary of third step:
  create new dictionary -> adding each state as a key and appending each event to a list as a value -> iterating on the new dictionary's   keys -> getting artist with most shows in a state -> getting venues with most shows in a state -> getting max price, max price           artist's name, and max price event's name -> write to csv
  
  
# How to run

To run this script you'll need to have python 3.7 (https://www.python.org/downloads/) and pip (https://pypi.org/project/pip/)

To download and install the dependencies:
1) Clone the repository (git clone https://github.com/manos89/ticketmaster-parser.git)
2) Install the requirements (pip install requirements.txt)

Running the script requires you to input some command line arguments. In general you can run python scripts by typing: 
python script_name.py where you replace script_name with the name of the .py file, in our case parse.

Here's an example on how to run the script:

python parse.py --key 35dfsdffe342fef4534saed --start 2019-08-01 --end 2019-08-10

You can replace "35dfsdffe342fef4534saed" with your key, "2019-08-01" with the starting date of your choice and "2019-08-10" with the ending date of your choice. Visit this page -> https://developer-acct.ticketmaster.com/user/login to generate your API key.

Please, don't forget that you will have to navigate to the directory where the script is. You can do this in many ways, depending on the OS you use.
