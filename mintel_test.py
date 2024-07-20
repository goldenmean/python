import time

def format_time(input_time):
    return time.strftime("%a_%b_%d:%H:%M:%S_%Y", time.gmtime(float(input_time)))


def normalise(input_time):
    """
    Args:
        input_time (int)
    """
    finished = None
    # This produces a formatted string like:
    #   Thu_Nov_24:18:22:48_1986
    str_time = format_time(input_time)
    while str_time[1:4] != "Sun":
        input_time -= 24*60*60
        str_time = format_time(input_time)
    while str_time[11:13] != "00":
        input_time -= 60*60
        str_time = format_time(input_time)
    while str_time[14:16] != "00":
        str_time = format_time(input_time)
        input_time -= 60
    while str_time[17:19] != "00":
        input_time -= 1
        str_time = format_time(input_time)
    return input_time


def new_normalise(input_time):
    """
    Args:
        input_time (float): Unix timestamp
    Returns:
        float: Normalized Unix timestamp
    """
    # Convert input_time to a datetime object for easier manipulation
    dt = time.gmtime(input_time)

    # Calculate adjustments to normalize to Sunday at 00:00:00
    days_until_sunday = (dt.tm_wday + 1) % 7  # tm_wday is Monday=0, ..., Sunday=6
    hours_adjustment = dt.tm_hour * 3600
    minutes_adjustment = dt.tm_min * 60
    seconds_adjustment = dt.tm_sec

    # Adjust input_time to the beginning of the next Sunday
    normalized_time = input_time - days_until_sunday * 86400 - hours_adjustment - minutes_adjustment - seconds_adjustment

    return normalized_time



#example code to test the normalise function
x=time.time()
#Y=normalise(x)
#print(x)
print(time.strftime("%a_%b_%d:%H:%M:%S_%Y", time.gmtime(float(x))))
Y=new_normalise(x)
print(time.strftime("%a_%b_%d:%H:%M:%S_%Y", time.gmtime(float(Y))))

#time.strftime("%a_%b_%d:%H:%M:%S_%Y", time.gmtime(x))