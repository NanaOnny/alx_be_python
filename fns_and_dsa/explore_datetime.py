import datetime
def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    """
    Calculate a future date based on user input (number of days).
    """
    try:
        number_of_days = int(input("Enter number of days to add: "))
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date after {number_of_days} days: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
