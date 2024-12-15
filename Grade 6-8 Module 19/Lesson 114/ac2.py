import random
from datetime import datetime, timedelta

def generate_random_datetime():
    # Define a start and end date for the range
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2030, 12, 31)
    
    # Calculate the total seconds in the date range
    total_seconds = int((end_date - start_date).total_seconds())
    
    # Generate a random number of seconds within the range
    random_seconds = random.randint(0, total_seconds)
    
    # Add the random seconds to the start date
    random_datetime = start_date + timedelta(seconds=random_seconds)
    
    return random_datetime

# Print a random date and time
print("Random Date and Time:", generate_random_datetime())
