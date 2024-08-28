'''
Using datetime.datetime
'''



import time
from datetime import datetime

# Define the specific past date
past_date = datetime(2000, 1, 1)  # Example: January 1, 2000

# Get the current time
current_time = datetime.now() # datetime.today( ) also works for getting current date, time

# Calculate the difference
time_difference = current_time - past_date

# Get days, seconds, and microseconds
days_passed = time_difference.days
seconds_passed = time_difference.seconds
microseconds_passed = time_difference.microseconds

print(f"Days passed: {days_passed}")
print(f"Seconds passed: {seconds_passed}")
print(f"Microseconds passed: {microseconds_passed}")

# Approximate number of months (assuming 30.44 days per month on average)
months_passed = days_passed / 30.44

# Approximate number of years (assuming 365.24 days per year on average)
years_passed = days_passed / 365.24

print(f"Approximate months passed: {months_passed}")
print(f"Approximate years passed: {years_passed}")