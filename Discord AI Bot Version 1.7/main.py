# Quick remainder for my future self for program running
# cmd > cd to directory > activate chatbot > python main.py

from datetime import date
import re
from inputimeout import inputimeout, TimeoutOccurred
import datetime
import time
from google_trans_new import google_translator
import sys
import discord
from discord.ext import commands
import os
import pickle
import random
import json
import tensorflow
import tflearn
import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer

from timer import TimerClass
timerPointer = TimerClass()

from animeInfo import animeInfo
aniInfoPointer = animeInfo()

from inputScan import inputScan
inputScanPointer = inputScan()

from botFunctions import botFunctions
functionPointer = botFunctions()

from embed import discordEmbed
embedPointer = discordEmbed()

stemmer = LancasterStemmer()


# access info -----------------------------------------------------------------
client = discord.Client()
bot_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
server_id = 000000000000000000000
channel_name = "xxxxxxxxxxxxxxxxxx"

# Milim xxxxxxxxxxxxxxxxxx
# Neiru xxxxxxxxxxxxxxxxxx
# Emilia xxxxxxxxxxxxxxxxxx
# Testing ML xxxxxxxxxxxxxxxxxx

# EMT: xxxxxxxxxxxxxxxxxx
# CCC: xxxxxxxxxxxxxxxxxx
# CSL: xxxxxxxxxxxxxxxxxx
# WEP: xxxxxxxxxxxxxxxxxx 
# DMS: xxxxxxxxxxxxxxxxxx
# MMM: xxxxxxxxxxxxxxxxxx
# BAL: xxxxxxxxxxxxxxxxxx
# FBK: xxxxxxxxxxxxxxxxxx

file_name = "xxxxxxxxxxxxxxxxxx.json"

# for fun: "xxxxxxxxxxxxxxxxxx.json"
# HololiveEN: "xxxxxxxxxxxxxxxxxx.json"
# end--------------------------------------------------------------------------------------

bot_functions = "\n \nYou can ask me about (primary functionalities):\
                \n**1.** General Information regarding the anime Wonder Egg Priority (synopsis, author, studio, OP, ED, etc.)\
                \n**2.** Where to watch this anime\
                \n**3.** When the next episode is airing\
                \n**4.** Try asking me any question! (under dev.)\
                \n\nThere are also other hidden things I can do ~(>_>)~"

new_features_list = "\n \nThe following's probably not very interesting if you aren't into programming...\
                    \n**1.** Timer Update - Every countdown timer call will initiate the calculation sequence (No long need manual timer refresh).\
                    \n**2.** Milim Output Word Filter - All non-preprogrammed output will be auto-scanned before sending.\
                    \n**3.** Clearance Scan - Function calls will now scan user clearance level before execution.\
                    \n**4.** Server Wide Implementation - Milim is now able to function in all channels within the designated server.\
                    (Permission Override allows Milim to function in other servers as well)\
                    \n**5.** Optimization - Milim's source code has been optimized from top to bottom. (Not perfect still, but much better than before)\
                    \n**6.** New Functions - New functions like pick and rate has been added upon request.\
                    \n**7.** Deep-learning Model - The model has been slightly adjusted for better learning output.\
                    \n**8.** Replies Addition - More question/replies has been added to Milim. Please contact ReZeroK if you have any suggestions."

# --------------------------------------------------------------------------------------------

# passcode for certain functions
passcode_stored = 'xxxxxxxxxxxxxxxxxx'

# --------------------------------------------------------------------------------------------

bot_ver = 1.6

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

    # one-hot encoded
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


net = tflearn.input_data(shape=[None, len(training[0])]) # input neuron layer with starting number of words

net = tflearn.fully_connected(net, 16) # 16 neurons fully connect - hidden neuron layer one
net = tflearn.fully_connected(net, 16) # 16 neurons fully connect - hidden neuron layer two
# net = tflearn.fully_connected(net, 16)  # 16 neurons fully connect - hidden neuron layer three

net = tflearn.fully_connected(net, len(output[0]), activation="softmax")  # output neuron layer with softmax (probability)
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
        model.fit(training, output, n_epoch=2000, batch_size=10, show_metric=True)
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

# -----------------------------------------------------------------------------------------------------------
@client.event  # run the code when the bot goes online
async def on_ready():
    bot_testing = client.get_channel(server_id)  # accessing the channel
    # code for execution
    # await bot_testing.change_presence(activity=discord.Game(name="and searching for honey"))
    # await ensures that the message is sent after the bot is online

    #new_message = "Hello! Nice to meet you all! I am a Deep-Learning AI bot coded by ReZeroK!"
    #await bot_testing.send(new_message)


@client.event
async def on_message(message):
    #bot_testing = client.Bot(command_prefix = '//')
    user_input = message.content.lower().replace('//milim', '//')
    user_input = user_input.replace('//', '// ')
    original_input = message.content
    new_message = True
    messServerID = message.guild.id
    userID = message.author.id
    userName = message.author.name

    print(f"User Info: {[userName, userID]}")
    print(f"Categorized Input: {inputScanPointer.scanInput(user_input, messServerID, userID)}")
    print(f"Bot reply (boolean): {message.author == client.user}")

    while message.author != client.user and new_message == True and not message.author.bot:
        scannedResult = inputScanPointer.scanInput(user_input, messServerID, userID)
        print(f"Scanned results: {scannedResult}")

        user_input = user_input.replace("permission override>> ", "")
        user_input = user_input.replace("permission override>>", "")
        original_input = original_input.replace("permission override>> ", "")
        original_input = original_input.replace("permission override>>", "")

        # Not command
        if scannedResult.find('None-Command') != -1:
            new_message = False
            break

        # check if permission is denied
        if scannedResult.find('C1D') != -1 or scannedResult.find('C2D') != -1 or scannedResult.find('C0D') != -1:
            await message.channel.send(scannedResult)
            new_message = False
            break

        # bot called in a different server
        if scannedResult.find('Error 0') != -1:
            await message.channel.send(f"I'm currently only working in the {aniInfoPointer.getAnimeName()} server!")
            new_message = False
            break

        # Translator
        elif scannedResult.find('Passive 0') != -1:
            translationStr = functionPointer.translation(user_input)
            if translationStr != "NONE":
                await message.channel.send(f"**Translated Text: **{translationStr}")
            new_message = False
            break

        # Pick command
        elif scannedResult.find('Command 0') != -1:
            print("Milim Pick Initiated")
            # await message.channel.send(embed=functionPointer.pickItem(original_input))
            await message.channel.send(functionPointer.pickItemNonEmbed(original_input))
            new_mewssage = False
            break

        # rate command
        elif scannedResult.find('Command 1') != -1:
            print("Milim Rate Initiated")
            await message.channel.send(functionPointer.rateItem(original_input))
            new_mewssage = False
            break

        # Program Termination
        elif scannedResult.find('Code 0') != -1:
            print("Program Terminated")
            await message.channel.send("Program Terminated Successfully")
            exit(0)

        # Timer - Refresh
        elif scannedResult.find('Code 1') != -1:
            await message.channel.send(timerPointer.refreshTimer())
            new_mewssage = False
            break

        # contact mods embed
        elif scannedResult.find('Code 2') != -1:
            feedback_channelID = 773014247399358464
            await message.channel.purge(limit=1)
            await message.channel.send(embed=embedPointer.contact_mods(feedback_channelID))
            new_mewssage = False
            break

        # Purge
        elif scannedResult.find('Code 3') != -1:
            await message.channel.send("**Password Required (purge > 100)** - please enter the password in the back-end terminal")
            purge_message = functionPointer.purgeCheck(user_input)
            if purge_message.lower().find('error') != -1:
                await message.channel.send(purge_message)
            else:
                await message.channel.purge(limit=2)
                await message.channel.send(purge_message)
                time.sleep(3)
                await message.channel.purge(limit=functionPointer.purgeNum(user_input) + 1)
            new_mewssage = False
            break

        # embed rules
        elif scannedResult.find('Code 4') != -1:
            await message.channel.send("Rules embed is currently disabled")
            new_mewssage = False
            break

        # get perm
        elif scannedResult.find('Code 5') != -1:
            await message.channel.send(embed=functionPointer.getPerm(userName, userID))
            new_mewssage = False
            break

        # anime search
        elif scannedResult.find('Code 6') != -1:
            await message.channel.send(embed=botFunctions.searchAnimeInfo(botFunctions, user_input))
            new_message = False
            break

    # deep learning section ---------------------------------------------------------------------------------

        results = model.predict([bag_of_words(user_input, words)])[0]
        # returns the greatest value's index
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        # back-end probability for each neuron nodes (likeliness)
        print("======================================================================")
        print(results)
        print(f' - Tag: > {tag} <')  # back-end tag return

        # data base answers -------------------------------------------------------------------------------------
        print(f' - Accuracy: > {results[results_index]} <')
        print("======================================================================")
        if results[results_index] > 0.999:  # accuracy threshold for a database reply
            for tg in data["replyData"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

            if tag.lower() == "confirmation" or tag.lower() == 'no_replies':
                break

            await message.channel.send(random.choice(responses))

            # extra message -------------------------------------------------------------------------
            if tag.lower() == "when_new_episode":
                anime_name = aniInfoPointer.getAnimeName()
                anime_dates = aniInfoPointer.getAnimeDates()
                anime_time = aniInfoPointer.getAnimeTime()

                timerArr = timerPointer.timerCalc()

                secs = timerArr[0]
                mins = timerArr[1]
                hours = timerArr[2]
                days = timerArr[3]

                # function call
                if days < 0:
                    await message.channel.send("This new episode has already been released!")
                else:
                    next_ep_array = timerPointer.next_ep_date(anime_dates, anime_time)
                    next_ep_num = next_ep_array[1]  # Next ep num
                    next_ep_date_out = next_ep_array[0]  # Next date

                    await message.channel.purge(limit=1)
                    await message.channel.send(f'The next episode of {anime_name} (Ep.{next_ep_num}) is coming out on **{next_ep_date_out}**!')
                    await message.channel.send(f"Time left until the next episode:"
                                        f" **{days} days {hours} hours {mins} minutes {secs} seconds**")

            if tag.lower() == "function_info":  # extra message ------------------------------------------------------------------------------
                await message.channel.send(bot_functions)
                
            new_message = False

            if tag.lower() == "music":  # extra message ---------------------------------------------------------------------------------------
                await message.channel.send(embed=aniInfoPointer.getOPED())

            if tag.lower() == "past_episodes":  # extra message -----------------------------------------------------------------------------------
                await message.channel.send(timerPointer.pastEpisodeCalc(user_input))

            if tag.lower() == "new_features":
                await message.channel.send(new_features_list)
            

        # no database answers ----------------------------------------------------------------------------------
        else:
            await message.channel.send(f"I'm not sure I understand. Please try again or ask a different question! (Beta Version {bot_ver})")
            new_message = False


client.run(bot_id)

# Check channel name
# Check bot ID
# Check channel ID

# cd Programming\Python\Pycharm\Workspace\AIChatBot1.0Discord
# activate chatbot
# python main.py

# cd C:\Coding\Workspace\Discord AI Bot (Ver 1.6)


'''
                    await bot_testing.send("**Password Required** - please enter the password in the back-end terminal")
                    gen_passcode = get_passcode()

                    print(f'New Generated Passcode: {gen_passcode}')
                    try:
                        passcode_entered = inputimeout(prompt='Please input the passcode:', timeout=10)
                    except TimeoutOccurred:
                        await bot_testing.send("**ERROR** - Timeout Has Occurred")
                        passcode_entered = 'timeout'
                        break

                    if gen_passcode == passcode_entered:
                        # delete the call messages
                        await message.channel.purge(limit=3)
                        
                        # code here -------------------------------------------

                        break

                    else:
                        print('Passcode Incorrect')
                        break
'''

# send rules---------------------------------------------------------------------------------------------

# if user_input.lower().find('update rules') != -1:
#     await bot_testing.send("**Password Required** - please enter the password in the back-end terminal")
#     gen_passcode = get_passcode()

#     print(f'New Generated Passcode: {gen_passcode}')
#     try:
#         passcode_entered = inputimeout(
#             prompt='Please input the passcode:', timeout=10)
#     except TimeoutOccurred:
#         await bot_testing.send("**ERROR** - Timeout Has Occurred")
#         passcode_entered = 'timeout'
#         break

#     if gen_passcode == passcode_entered:
#         delete the call messages
#         await message.channel.purge(limit=3)

#         embed_infoVar = embed_info()
#         embed_imageVar = embed_image_one()
#         embed_imageRules = embed_image_rules()
#         embed_staffVar = embed_staff()

#         await bot_testing.send(embed=embed_infoVar)
#         await bot_testing.send(embed=embed_imageRules)

#         await bot_testing.send(embed=embed_rules_one())
#         await bot_testing.send(embed=embed_rules_two())
#         await bot_testing.send(embed=embed_rules_three())
#         await bot_testing.send(embed=embed_rules_four())
#         await bot_testing.send(embed=embed_rules_five())
#         await bot_testing.send(embed=embed_rules_six())
#         await bot_testing.send(embed=embed_rules_seven())
#         await bot_testing.send(embed=embed_rules_eight())
#         await bot_testing.send(embed=embed_rules_nine())
#         await bot_testing.send(embed=embed_rules_ten())

#         await bot_testing.send(embed=embed_imageVar)
#         await bot_testing.send(embed=embed_staffVar)
#         await bot_testing.send(embed=test_embed())
#         break
#     else:
#         print('Passcode Incorrect')
#         break