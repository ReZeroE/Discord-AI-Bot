from datetime import date
import datetime

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        global countdown_gate
        global countdown_result
        countdown_gate = True
        countdown_result = f"{days} days and {timer}"

    countdown_result = 'Countdown ended!'
    countdown_gate = False


# get today's date
def get_today_date():
    today = date.today()
    d1 = today.strftime("%m/%d/%Y")
    return d1


# get today's time
def get_today_time():
    today_time = str(datetime.datetime.now().time())
    return today_time


# convert date and time to sec
def convert_date_to_time(to_date, to_time):
    today = get_today_date()
    today_arr = today.split("/")
    to_arr = to_date.split("/")

    # define months with 31 days
    month_day_number = 30
    this_month = today_arr[0]
    if int(to_arr[0]) > int(today_arr[0]):
        if int(this_month) == 1 or int(this_month) == 3 or int(this_month) == 5 or int(this_month) == 7 \
                or int(this_month) == 8 or int(this_month) == 10 or int(this_month) == 12:
            month_day_number = 31
        elif int(this_month) == 2:
            month_day_number = 28

    month_to_sec = (int(to_arr[0]) - int(today_arr[0])
                    ) * month_day_number * 24 * 3600
    date_to_sec = (int(to_arr[1]) - int(today_arr[1])) * 24 * 3600
    year_to_sec = (int(to_arr[2]) - int(today_arr[2])) * 365 * 30 * 24 * 3600

    time_now = get_today_time()
    time_now_arr = time_now.split(":")
    time_to_arr = to_time.split(":")

    hours_to_sec = (int(time_to_arr[0]) - int(time_now_arr[0])) * 3600
    min_to_sec = (int(time_to_arr[1]) - int(time_now_arr[1])) * 60
    sec_total = (int(float(time_to_arr[2])) - int(float(time_now_arr[2])))

    total_sec = month_to_sec + date_to_sec + \
        year_to_sec + hours_to_sec + min_to_sec + sec_total

    print(f"Time to: {time_to_arr[0]}")
    print(f"Time now: {time_now_arr[0]}")
    print(f"In sec: {hours_to_sec}")

    print(f"Current Time: {time_now}")
    print("Today's date: " + today)
    print(f'Total time in seconds: {total_sec}')
    return total_sec

to_date = "3/2/2021"
to_time = "10:30:00"

print(convert_date_to_time(to_date, to_time))

t = int(convert_date_to_time(to_date, to_time))
mins, secs = divmod(t, 60)
hours, mins = divmod(mins, 60)
days, hours = divmod(hours, 24)
timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
print('=======================')
print(f'Day: {days}')
print(f'Hours: {hours}')
print(f'Min: {mins}')
print(f'Sec: {secs}')