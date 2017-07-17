import datetime
import pytz # new import

current_time = datetime.datetime.now() #system time

server_timezone = pytz.timezone("US/Eastern")
new_timezone = pytz.timezone("US/Pacific")

# returns datetime in the new timezone. Profit!
current_time_in_new_timezone = server_timezone.localize(current_time).astimezone(new_timezone)