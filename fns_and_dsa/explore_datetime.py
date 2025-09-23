from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")
display_current_datetime()
extra = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    today = date.today()
    future_date = today + timedelta(days=extra)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
calculate_future_date()