# ticketmaster-parser

# Project Explanation
The purpose of this project is to collect music events from ticketmaster website using its API, and then export the results, according to the provided format, to a CSV file.

To make the solution easier to understand I will divide it to 3 big parts:
## 1) Getting all the inputs and formatting the date
  - User inputs his/her API key, the starting date and the ending date. All the events must be between this date range.
  - First we will have to convert the date from a string to a datetime object. Datetime objects are useful because they come with some         methods and some attributes. In our case we have to convert them to this format so we can compare them to our current date and also to     compare the starting and ending date (ending date must be after starting date).
  - Then we make the comparison, which is similar to comparing numbers/integers. In real life we can check if 10<11, and in the same way       we can find out if starting date < ending date.
  - Finally, we have to convert them from a datetime object to a text in a format that can be used to make the request (YYYY-MM-               DDTHH:mm:ssZ)
  
## 2) Making the request
## 3) Collecting the needed results

# How to run

To run this script you'll need to have python 3.7 (https://www.python.org/downloads/) and pip (https://pypi.org/project/pip/)

To install the dependencies:
1) Clone the repository (git clone https://github.com/manos89/ticketmaster-parser.git)
2) Install the requirements (pip install requirements.txt)
