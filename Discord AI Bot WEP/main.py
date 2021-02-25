# Quick remainder for my future self for program running
# cmd > cd to directory > activate chatbot > python main.py

from passcodes import randomize_passcode
from passcodes import get_passcode

import datetime
import time
from datetime import date

import re
import sys
import discord
import os
import pickle
import random
import json
import tensorflow
import tflearn
import numpy

import nltk
from nltk.stem.lancaster import LancasterStemmer

from inputimeout import inputimeout, TimeoutOccurred

from embed import contact_mods
from embed import embed_staff
from embed import embed_rules_ten
from embed import embed_rules_nine
from embed import embed_rules_eight
from embed import embed_rules_seven
from embed import embed_rules_six
from embed import embed_rules_five
from embed import embed_rules_four
from embed import embed_rules_three
from embed import embed_rules_two
from embed import embed_rules_one
from embed import embed_image_rules
from embed import embed_image_one
from embed import embed_info

from google_trans_new import google_translator

stemmer = LancasterStemmer()


# access info -----------------------------------------------------------------
client = discord.Client()
bot_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
server_id = 000000000000000000
channel_name = "milim"

# Milim xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Neiru xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Mi Na xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# FBK: 000000000000000000
# EMT: 000000000000000000
# CCC: 000000000000000000
# CSL: 000000000000000000
# WEP: 000000000000000000
# DMS: 000000000000000000
# MMM: 000000000000000000
# BAL: 000000000000000000

file_name = "WonderEgg.json"

# for fun: "replyDataFile.json"
# HololiveEN: "WonderEgg.json"
# end--------------------------------------------------------------------------------------

anime_name = 'Wonder Egg Priority'

# dates when the WEP airs
anime_dates = []
anime_dates.append('1/12/2021')
anime_dates.append('1/19/2021')
anime_dates.append('1/26/2021')
anime_dates.append('2/2/2021')
anime_dates.append('2/9/2021')
anime_dates.append('2/16/2021')
anime_dates.append('2/23/2021')
anime_dates.append('3/2/2021')
anime_dates.append('3/9/2021')
anime_dates.append('3/16/2021')
anime_dates.append('3/23/2021')
anime_dates.append('3/6/2021')

# exact time when the ep is coming out
anime_time = '10:30:00'

# --------------------------------------------------------------------------------------------

# passcode for certain functions
passcode_stored = 'wSCxcy9faE7ZATzw'

# --------------------------------------------------------------------------------------------

with open(file_name) as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    # insert all the data into the pre-created lists ----------------------------------------------
    for replyData in data["replyData"]:
        for pattern in replyData["patterns"]:
            # tokenizing all words (wrds is already a list)
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(replyData["tag"])

        if replyData["tag"] not in labels:
            labels.append(replyData["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    # pre-processing data -------------------------------------------------------------------------
    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)  # append term to 1 if the word exist
            else:
                bag.append(0)  # append term to 0 if the word DNE

        output_row = out_empty[:]
        # look through labels[], identify its index and set it to 1
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    # saves the processed data from above
    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

# model building with tflearn ------------------------------------------------------------------
tensorflow.reset_default_graph()

# input neuron layer with starting number of words
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 16) # 16 neurons fully connect - hidden neuron layer one
net = tflearn.fully_connected(net, 16) # 16 neurons fully connect - hidden neuron layer two
# net = tflearn.fully_connected(net, 16)  # 16 neurons fully connect - hidden neuron layer three
net = tflearn.fully_connected(net, len(output[0]),
                              activation="softmax")  # output neuron layer with softmax (probability)
net = tflearn.regression(net)

try:
    model = tflearn.DNN(net)  # DNN is a type of neural network
except:
    model = tflearn.DNN(net)

# fitting the model ------------------------------------------------------------------------------
try:
    # check if there is already trained AI data in the directory
    if os.path.exists("model.tflearn.meta"):
        model.load("model.tflearn")
    else:
        model.fit(training, output, n_epoch=2000,
                  batch_size=10, show_metric=True)
        model.save("model.tflearn")
except:
    # passing training data
    # n_epoch is the number at which the program sees the data
    model.fit(training, output, n_epoch=2000, batch_size=15, show_metric=True)
    model.save("model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]  # word storage

    s_words = nltk.word_tokenize(s)  # word tokenization through nltk modules
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


reply = ""
user_input = ""


# Timer -----------------------------------------------------------------------------------------------------
# define the countdown func
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


def next_ep_date(anime_dates, anime_time):
    counter = 1
    ep_array = []  # [next ep date, next ep number]

    for x in anime_dates:
        if convert_date_to_time(x, anime_time) > 0:
            ep_array.append(x)  # next epsiode date
            ep_array.append(str(counter))  # next episode number
            return ep_array
        print(
            f'\nEpisode {counter} is already out. Auto checking the date for the next episode.')
        counter += 1
    return -1
# -----------------------------------------------------------------------------------------------------------
# Python Translator


def translate_to_eng(message):
    translator = google_translator()
    translated_text = translator.translate(message, lang_tgt='en')
    return translated_text


# -----------------------------------------------------------------------------------------------------------
@client.event  # run the code when the bot goes online
async def on_ready():
    bot_testing = client.get_channel(server_id)  # accessing the channel
    # code for execution
    # await bot_testing.change_presence(activity=discord.Game(name="and searching for honey"))
    new_message = "Hello! Nice to meet you all! I am a Deep-Learning AI bot coded by ReZeroK!"
    # await ensures that the message is sent after the bot is online
    await bot_testing.send(new_message)


@client.event
async def on_message(message):
    bot_testing = client.get_channel(server_id)
    user_input = message.content.lower().replace('//', ' ')
    new_message = True

    global to_date
    global to_time

    # Translator ----------------------------------------------------------------------------------------------
    if (user_input.find('Translated Text:')) == -1 and re.search('[a-z][A-Z]', user_input) == None:
        translator = google_translator()

        string_test = translator.detect(user_input.lower())
        res = isinstance(string_test, str)  # see if the item is an string  

        # translator.detect(user_input.lower())[0] == 'ja' and
        if not res:
            # if the input japanese has english chars (and (has_letters is None))
            # has_letters = re.search('[a-z][A-Z]', user_input)
            if translator.detect(user_input)[0] == 'ja' and user_input.find('//') == -1 \
                    and str(message.channel) == channel_name:
                await bot_testing.send(f'**Translated Text:** {translate_to_eng(user_input)}')

                # orginial_language = translator.detect(user_input.lower())[1]
                # await bot_testing.send(f'**Original Language:** {orginial_language}')

    # ----------------------------------------------------------------------------------------------------------
    # make sure that the message is sent in the right channel and is not a website link
    if str(message.channel) == channel_name.lower() and user_input.find('https') == -1:
        if user_input.find('//') != -1 or user_input.find('//milim') != -1:
            while new_message:

                # Timer ----------------------------------------------------------------------------------------
                if user_input.lower().find("start timer") != -1 or user_input.lower().find("refresh timer") != -1:
                    # input time in seconds (month/day/year)
                    await bot_testing.send('Countdown timer updated!')
                    to_date = next_ep_date(anime_dates, anime_time)[0]
                    to_time = anime_time

                    if to_date == -1:
                        await bot_testing.send('The final episode of the anime Wonder Egg Priority is already out!')
                        new_message = False
                        continue

                    break

                # exit------------------------------------------------------------------------------------------

                if user_input.lower().find('sys.exit(0)') != -1:  # type quit to stop the program
                    print("Program Terminated")
                    await bot_testing.send("Program Terminated Successfully")
                    sys.exit(0)
                    break

                # send rules---------------------------------------------------------------------------------------------

                if user_input.lower().find('update rules') != -1:
                    await bot_testing.send("**Password Required** - please enter the password in the back-end terminal")
                    gen_passcode = get_passcode()

                    print(f'New Generated Passcode: {gen_passcode}')
                    try:
                        passcode_entered = inputimeout(
                            prompt='Please input the passcode:', timeout=10)
                    except TimeoutOccurred:
                        await bot_testing.send("**ERROR** - Timeout Has Occurred")
                        passcode_entered = 'timeout'
                        break

                    if gen_passcode == passcode_entered:
                        # delete the call messages
                        await message.channel.purge(limit=3)

                        embed_infoVar = embed_info()
                        embed_imageVar = embed_image_one()
                        embed_imageRules = embed_image_rules()
                        embed_staffVar = embed_staff()

                        await bot_testing.send(embed=embed_infoVar)
                        await bot_testing.send(embed=embed_imageRules)

                        await bot_testing.send(embed=embed_rules_one())
                        await bot_testing.send(embed=embed_rules_two())
                        await bot_testing.send(embed=embed_rules_three())
                        await bot_testing.send(embed=embed_rules_four())
                        await bot_testing.send(embed=embed_rules_five())
                        await bot_testing.send(embed=embed_rules_six())
                        await bot_testing.send(embed=embed_rules_seven())
                        await bot_testing.send(embed=embed_rules_eight())
                        await bot_testing.send(embed=embed_rules_nine())
                        await bot_testing.send(embed=embed_rules_ten())

                        await bot_testing.send(embed=embed_imageVar)
                        await bot_testing.send(embed=embed_staffVar)
                        # await bot_testing.send(embed=test_embed())
                        break
                    else:
                        print('Passcode Incorrect')
                        break

                # contact staff embed ------------------------------------------------------------------------------------
                contact_mods_ID = 811156156113223718
                
                if user_input.lower().find('update staff embed') != -1:
                    await bot_testing.send("**Password Required** - please enter the password in the back-end terminal")
                    gen_passcode = get_passcode()

                    print(f'New Generated Passcode: {gen_passcode}')
                    try:
                        passcode_entered = inputimeout(
                            prompt='Please input the passcode:', timeout=10)
                    except TimeoutOccurred:
                        await bot_testing.send("**ERROR** - Timeout Has Occurred")
                        passcode_entered = 'timeout'
                        break

                    if gen_passcode == passcode_entered:
                        # delete the call messages
                        await message.channel.purge(limit=3)
                        await bot_testing.send(embed=contact_mods(contact_mods_ID))
                        break

                    else:
                        print('Passcode Incorrect')
                        break

                # purge command -----------------------------------------------------------------------------------------

                if user_input.lower().find('purge') != -1:

                    await bot_testing.send("**Password Required** - please enter the password in the back-end terminal")
                    gen_passcode = get_passcode()

                    print(f'New Generated Passcode: {gen_passcode}')
                    try:
                        passcode_entered = inputimeout(
                            prompt='Please input the passcode:', timeout=10)
                    except TimeoutOccurred:
                        await bot_testing.send("**ERROR** - Timeout Has Occurred")
                        passcode_entered = 'timeout'
                        break

                    if gen_passcode == passcode_entered:
                        # delete the call messages
                        await message.channel.purge(limit=2)

                        input_temp = user_input.replace(
                            '//', '')  # input_temp = purge 6
                        purge_temp = input_temp.lower().split(
                            ' ')  # purge temp = ['purge', '6']
                        try:
                            purge_number = int(purge_temp[2])
                        except ValueError:
                            await bot_testing.send('**ERROR** - Purge number format incorrect')
                            break

                        await bot_testing.send(f'Message Purge Initiated ({purge_number} messages will be purged in 3 seconds)')
                        time.sleep(3)
                        await message.channel.purge(limit=(purge_number+1))
                        print('Purge Complete')
                        break
                    else:
                        print('Passcode Incorrect')
                        break

                # deep learning section ---------------------------------------------------------------------------------

                results = model.predict([bag_of_words(user_input, words)])[0]
                # returns the greatest value's index
                results_index = numpy.argmax(results)
                tag = labels[results_index]

                # back-end probability for each neuron nodes (likeliness)
                print(results)
                print(tag)  # back-end tag return

                # data base answers -------------------------------------------------------------------------------------
                if results[results_index] > 0.999:  # accuracy threshold for a database reply
                    for tg in data["replyData"]:
                        if tg['tag'] == tag:
                            responses = tg['responses']

                    if tag.lower() == "confirmation" or tag.lower() == 'no_replies':
                        break

                    await bot_testing.send(random.choice(responses))

                    # extra message -------------------------------------------------------------------------
                    if tag.lower() == "when_new_episode":
                        # function call
                        initial_time = int(convert_date_to_time(to_date, to_time))
                        t = initial_time
                        mins, secs = divmod(t, 60)
                        hours, mins = divmod(mins, 60)
                        days, hours = divmod(hours, 24)
                        timer = '{:02d}:{:02d}:{:02d}'.format(
                            hours, mins, secs)
                        print(timer, end="\r")
                        if days < 0:
                            await bot_testing.send("This new episode has already been released!")
                        else:
                            next_ep_array = next_ep_date(
                                anime_dates, anime_time)
                            next_ep_num = next_ep_array[1]  # Next ep num
                            next_ep_date_out = next_ep_array[0]  # Next date

                            await message.channel.purge(limit=1)
                            await bot_testing.send(f'The next episode of {anime_name} (Ep.{next_ep_num}) is coming out on **{next_ep_date_out}**!')
                            await bot_testing.send(f"Time left until the next episode:"
                                                   f" **{days} days {hours} hours {mins} minutes {secs} seconds**")

                    if tag.lower() == "function_info":  # extra message ------------------------------------------------------------------------------
                        await bot_testing.send("\n \nYou can ask me about (primary functionalities):"
                                               "\n**1.** General Information regarding the anime Wonder Egg Priority "
                                               "(synopsis, author, studio, OP, ED, etc.)"
                                               "\n**2.** Where to watch this anime"
                                               "\n**3.** When the next episode is airing"
                                               "\n**4.** Try asking me any question! (under dev.)"
                                               "\n\u200b\n"
                                               "There are also other hidden things I can do ~(>_>)~")
                    new_message = False

                    if tag.lower() == "music":  # extra message ---------------------------------------------------------------------------------------
                        embed = discord.Embed()
                        embed.description = "Sudachi no Uta [Opening] \
                                            \n[Youtube Link](https://youtu.be/-EuXOT4lb0s) - [Spotify Link](https://open.spotify.com/track/0U3JBftbH2K1rzaMM2fav3) \
                                            \nLife is Cider [Ending] \
                                            \n[Youtube Link](https://youtu.be/7TGgvqNN0yk) - [Spotify Link](https://open.spotify.com/track/0U3JBftbH2K1rzaMM2fav3)"
                        await bot_testing.send(embed=embed)

                    if tag.lower() == "past_episodes":  # extra message -----------------------------------------------------------------------------------
                        int_temp ='' # user input ep num
                        for c in user_input:
                            if c.isdigit():
                                int_temp += str(c)

                        if int_temp == "0":
                            print('Index Error - user episode input incorrect')
                            await bot_testing.send(f"Episode zero doesn't exit!")
                            break

                        try: 
                            next_ep_array = next_ep_date(anime_dates, anime_time)
                            next_ep_num = next_ep_array[1]

                            if int(next_ep_num) <= int(int_temp): # make sure the ep has not been out yet
                                test = anime_dates[int(int_temp) - 1] # if False then the ep does not exit
                                await bot_testing.send(f"Episode {int_temp} isn't out yet!")
                            else:
                                await bot_testing.send(f'Episode {int_temp} was released on {anime_dates[int(int_temp)-1]}!')
                                
                        except IndexError: # ep does not exist
                            print('Index Error - user episode input incorrect')
                            await bot_testing.send(f'Wonder Egg Priority only has 12 episodes!')
                        break

                # no database answers ----------------------------------------------------------------------------------
                else:
                    await bot_testing.send("I'm not sure I understand. Please try again or ask a different question!"
                                           "\n(Beta Version 1.5)")
                    new_message = False


client.run(bot_id)

