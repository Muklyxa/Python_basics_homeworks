seconds_in_day = 24 * 60 * 60
seconds_in_hour = 60 * 60
seconds_in_minute = 60
time_in_seconds = int(input("Enter the time in seconds: "))

if time_in_seconds > (seconds_in_day - 1):
    print("Too large value!")
elif time_in_seconds < 0:
    print("Only values greater than zero!")
else:
    hours = time_in_seconds // seconds_in_hour
    minutes = (time_in_seconds % seconds_in_hour) // seconds_in_minute
    seconds = (time_in_seconds % seconds_in_hour) % seconds_in_minute

    if hours < 10:
        hours = str(f"0{hours}")

    if minutes < 10:
        minutes = str(f"0{minutes}")

    if seconds < 10:
        seconds = str(f"0{seconds}")

    print(f"{hours:>2}:{minutes:>2}:{seconds:>2}")