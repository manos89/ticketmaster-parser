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

To download and install the dependencies:
1) Clone the repository (git clone https://github.com/manos89/ticketmaster-parser.git)
2) Install the requirements (pip install requirements.txt)

Running the script requires you to input some command line arguments. In general you can run python scripts by typing: 
python script_name.py where you replace script_name with the name of the .py file, in our case parse.

In our case here's an example on how to run the script:
python parse.py --key 35dfsdffe342fef4534saed --start 2019-08-01 --end 2019-08-10

You can replace "35dfsdffe342fef4534saed" with your key "2019-08-01" with the starting date you want and "2019-08-10" with the ending date you want.

Please don't forget that you will have to navigate to the directory where the script is. You can do this in many ways, depending on the OS you use.
