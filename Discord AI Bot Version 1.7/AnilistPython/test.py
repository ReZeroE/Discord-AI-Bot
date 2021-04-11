'''
Test Cases

from __init__ import Anilist
instance = Anilist()
'''

from botSupport import botSupport
anilistBot = botSupport()

data = anilistBot.getCharacterID("Harutora")
print(data)