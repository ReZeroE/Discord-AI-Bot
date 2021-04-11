import datetime
import time
from datetime import date
import discord

from animeInfo import animeInfo
aniInfoPointer = animeInfo()

to_date = ''
to_time = ''

class TimerClass:
    def __init__(self):
        self.countdown_gate = False
        self.countdown = ''

        self.anime_dates = aniInfoPointer.getAnimeDates()
        self.anime_time = aniInfoPointer.getAnimeTime()
        self.anime_name = aniInfoPointer.getAnimeName()

    # define the countdown func
    def countdown(self, t):
        secs, mins, hours, days = 0
        while t:
            mins, secs = divmod(t, 60)
            hours, mins = divmod(mins, 60)
            days, hours = divmod(hours, 24)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            countdown_gate = True
            countdown_result = f"{days} days and {timer}"

        countdown_result = 'Countdown ended!'
        countdown_gate = False


    # get today's date
    def get_today_date(self):
        today = date.today()
        d1 = today.strftime("%m/%d/%Y")
        return d1


    # get today's time
    def get_today_time(self):
        today_time = str(datetime.datetime.now().time())
        return today_time


    # convert date and time to sec
    def convert_date_to_time(self, to_date, to_time):
        today = self.get_today_date()
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

        time_now = self.get_today_time()
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


    def next_ep_date(self, anime_dates, anime_time):
        counter = 1
        ep_array = []  # [next ep date, next ep number]

        for x in anime_dates:
            if self.convert_date_to_time(x, anime_time) > 0:
                ep_array.append(x)  # next epsiode date
                ep_array.append(str(counter))  # next episode number
                return ep_array
            print(
                f'\nEpisode {counter} is already out. Auto checking the date for the next episode.')
            counter += 1
        return -1

    def refreshTimer(self) -> str:
        to_date = self.next_ep_date(self.anime_dates, self.anime_time)[0]
        to_time = self.anime_time

        if to_date == '' or to_time == '': 
            return "Countdown Timer Failure"
        else: 
            return "Countdown timer refreshed successfully!"

    def timerCalc(self):
        to_date = self.next_ep_date(self.anime_dates, self.anime_time)[0]
        to_time = self.anime_time

        initial_time = int(self.convert_date_to_time(to_date, to_time))
        mins, secs = divmod(initial_time, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        return [secs, mins, hours, days]
    
    def pastEpisodeCalc(self, input):
        int_temp ='' # user input ep num
        for c in input:
            if c.isdigit():
                int_temp += str(c)

        if int_temp == "0":
            print('Index Error - user episode input incorrect')
            return ("Episode zero doesn't exist!")

        try: 
            next_ep_array = self.next_ep_date(self.anime_dates, self.anime_time)
            print(f"Error Array: {next_ep_array}")
            next_ep_num = next_ep_array[1]

            if int(next_ep_num) <= int(int_temp): # make sure the ep has not been out yet
                test = self.anime_dates[int(int_temp) - 1] # if False then the ep does not exit
                return (f"Episode {int_temp} isn't out yet!")
            else:
                return (f'Episode {int_temp} was released on {self.anime_dates[int(int_temp)-1]}!')
                
        except IndexError: # ep does not exist
            print('Index Error - user episode input incorrect')
            return (f'{self.anime_name} only has 12 episodes!')