# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(current_date):
    # Ask the user for number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)
    # Format future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


# Run the functions
if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)
