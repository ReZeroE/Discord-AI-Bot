'''
Test Cases

from __init__ import Anilist
instance = Anilist()
'''

from botSupport import botSupportClass
anilistBot = botSupportClass()

data = anilistBot.getCharacterInfo("Madoka")
print(data)