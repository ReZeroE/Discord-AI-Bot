from google_trans_new import google_translator
from inputimeout import inputimeout, TimeoutOccurred
import random
import discord
import re
import sys

sys.path.append("./AnilistPython")
from botSupport import botSupportClass
anilistBot = botSupportClass()

from passcodes import passcodeGen
passcodeGenPointer = passcodeGen()

from clearanceScan import clearanceScan
clScanPointer = clearanceScan

from outputScan import outputScan
outputScanPointer = outputScan()

class botFunctions:

    def translation(self, input):
        translator = google_translator()

        string_test = translator.detect(input)
        res = isinstance(string_test, str) and not re.search('[a-zA-Z]', input) # see if the item is an string with no letters

        if not res:
            if translator.detect(input)[0] == 'ja' and input.find('//') == -1:
                translated_text = translator.translate(input, lang_tgt='en')

                print(f"Translated Text: {translated_text}")
                if outputScanPointer.scan_output(translated_text) == 'G':
                    return translated_text
                else:
                    return "ReZeroK told me that it's not good to say those words!"
        print("Translation Terminated (0)")
        
        return "NONE"

    def purgeCheck(self, input) -> str:
        print(f"Purge Request: {input}")
        input_temp = input.replace('// ', '')  # input_temp = purge 6
        purge_temp = input_temp.lower().split(' ')  # purge temp = ['purge', '6']
        try:
            print(f"Purge Array: {purge_temp}")
            purge_number = int(purge_temp[1])
        except ValueError:
            return '**ERROR** - Purge number format incorrect'

        if purge_number > 100:
            result = self.terminalPasscode()
            if result == 'passcode correct':
                return f'Message Purge Initiated ({purge_number} messages will be purged in 3 seconds)'
            elif result == 'timeout':
                return '**ERROR** - Timeout Has Occurred'
            else:
                return '**ERROR** - Passcode Incorrect'

        return f'Message Purge Initiated ({purge_number} messages will be purged in 3 seconds)'

    def purgeNum(self, input):
        input_temp = input.replace('// ', '')  # input_temp = purge 6
        purge_temp = input_temp.lower().split(' ')  # purge temp = ['purge', '6']
        return int(purge_temp[1])

    def terminalPasscode(self):
        gen_passcode = passcodeGenPointer.get_passcode()

        print(f'New Generated Passcode: {gen_passcode}')
        try:
            passcode_entered = inputimeout(prompt='Please input the passcode:', timeout=10)
        except TimeoutOccurred:
            return 'timeout'
            passcode_entered = 'timeout'

        if gen_passcode == passcode_entered:
            return 'passcode correct'

    def pickItemEmbed(self, input):
        tempInput = input
        tempInput = tempInput.replace("//pick", "")
        itemArr = [] 
        itemArr = tempInput.split(";")

        print(f"Item Array (to pick from): {itemArr}")
        if len(itemArr) == 1:
            string = 'You need to give me more than one item to pick from!\n(Example: //pick watch anime; sleep; play Genshin Impact)'
            itemEmbedE = discord.Embed(title="Milim's Choice!", description=f"{string}!", color=0xFFC0CB)
            return itemEmbedE
        elif len(itemArr) > 100:
            string = 'That is too many items for me to pick from!'
            itemEmbedE = discord.Embed(title="Milim's Choice!", description=f"{string}!", color=0xFFC0CB)
            return itemEmbedE

        itemChoosen = itemArr[random.randint(0, len(itemArr) - 1)]
        if itemChoosen == None:
            string = "I don't want to talk to you anymore"
            itemEmbedE = discord.Embed(title="Milim's Choice!", description=f"{string}!", color=0xFFC0CB)
            return itemEmbedE

        itemEmbed = discord.Embed(title="Milim's Choice!", description=f"I pick {itemChoosen}!", color=0xFFC0CB)
        return itemEmbed

    def pickItemNonEmbed(self, input): # user orginal input needed
        tempInput = input
        tempInput = tempInput.replace("//pick ", "")
        itemArr = [] 
        itemArr = tempInput.split(";")

        if len(itemArr) == 1:
            return 'You need to give me more than one item to pick from!\n(Example: //pick watch anime; sleep; play Genshin Impact)'
        elif len(itemArr) > 100:
            return 'That is too many items for me to pick from! (MAX < 100)'

        itemChoosen = itemArr[random.randint(0, len(itemArr) - 1)]
        if itemChoosen == None:
            return "I don't want to talk to you anymore"

        outputScanResult = outputScanPointer.scan_output(itemChoosen)

        if outputScanResult == 'G':
            return f"\nI think I'll choose '**{itemChoosen}**'!"
        elif outputScanResult.find("unavailable") != -1:
            return f"Sorry! I can't use the '@' sign!"
        else:
            return "I'm going to tell ReZeroK that you are trying to make me say a bad word! ʕっ•ᴥ•ʔっ"

    def rateItem(self, input):
        tempInput = input
        tempInput = tempInput.replace("//rate ", "")
        randNum = random.randint(0, 10)
        emoji = ''

        if randNum < 3:
            emoji = " ( ╥﹏╥) ノシ"
        elif randNum < 5:
            emoji = " (っˆڡˆς)"
        elif randNum < 7:
            emoji = " ٩( ๑╹ ꇴ╹)۶"
        else:
            emoji = " ~\(≧▽≦)/~"

        outputScanResult = outputScanPointer.scan_output(tempInput)

        if outputScanResult == 'G':
            return f"I think I will give '{tempInput}' a **{randNum}/10**! {emoji}"
        elif outputScanResult.find("unavailable") != -1:
            return f"Sorry! I can't use the '@' sign!"
        else:
            return "I'm going to tell ReZeroK that you are trying to make me say a bad word! ʕっ•ᴥ•ʔっ"

    def getPerm(self, userName, userID):
        print(f"UserID: {userID}")
        string = f"Username: {userName}\nUser iD: {userID}\nPermission: {clScanPointer.clearanceScan(clScanPointer, int(userID))}"
        itemEmbed = discord.Embed(title="My Permission", description=string, color=0xFFC0CB)
        return itemEmbed

    def searchAnimeInfo(self, animeName):
        animeName = animeName.strip().replace("// get anime ", "")
        animeName = animeName.strip().replace("// search anime ", "")
        print(f"Anime Name >{animeName}<")

        data = anilistBot.getAnimeInfo(animeName)
        eng_name = data["name_english"]
        jap_name = data["name_romaji"]
        desc = data['desc']
        starting_time = data["starting_time"]
        ending_time = data["ending_time"]
        cover_image = data["cover_image"]
        airing_format = data["airing_format"]
        airing_status = data["airing_status"]
        airing_ep = data["airing_episodes"]
        season = data["season"]
        genres = data["genres"]
        next_airing_ep = data["next_airing_ep"]

        anime_link = f'https://anilist.co/anime/{anilistBot.getAnimeID(animeName)}/'

        #parse genres
        genres_new = ''
        count = 1
        for i in genres:
            if count != len(genres):
                genres_new += f'{i}, '
            else:
                genres_new += f'{i}'
            count += 1

        #parse time
        next_ep_string = ''
        try:
            initial_time = next_airing_ep['timeUntilAiring']
            mins, secs = divmod(initial_time, 60)
            hours, mins = divmod(mins, 60)
            days, hours = divmod(hours, 24)
            timer = f'{days} days {hours} hours {mins} mins {secs} secs'
            next_ep_num = next_airing_ep['episode']
            next_ep_string = f'Episode {next_ep_num} is releasing in {timer}!\
                            \n\n[AniList Page]({anime_link})\
                            \n[AnilistPython Documentation](https://pypi.org/project/AnilistPython/)'
        except:
            next_ep_string = f'The anime has already ended or its release date has not been confirmed!\
                            \n\n[AniList Page]({anime_link})\
                            \n[AnilistPython Documentation](https://pypi.org/project/AnilistPython/)'

        #parse desc
        if desc != None and len(desc) != 0:
            desc = desc.strip().replace('<br>', '')
            desc = desc.strip().replace('<i>', '')
            desc = desc.strip().replace('</i>', '')
        
        info_arr = [eng_name, jap_name, desc, starting_time, ending_time, cover_image, airing_format, airing_status, airing_ep, season, genres_new, next_ep_string]
        info = self.embedValueCheck(self, info_arr)


        anime_embed = discord.Embed(title=jap_name, description=eng_name, color=0xFF8DA1)
        anime_embed.set_image(url=cover_image)
        anime_embed.add_field(name="Synopsis", value=info[2], inline=False)
        anime_embed.add_field(name="Airing Date", value=info[3], inline=True)
        anime_embed.add_field(name="Ending Date", value=info[4], inline=True)
        anime_embed.add_field(name="Season", value=info[9], inline=True)
        anime_embed.add_field(name="Airing Format", value=info[6], inline=True)
        anime_embed.add_field(name="Airing Status", value=info[7], inline=True)
        anime_embed.add_field(name="Genres", value=info[10], inline=True)
        anime_embed.add_field(name="Next Episode ~", value=info[11], inline=False)
        anime_embed.set_footer(text='Supported by the AnilistPython Library (ReZeroK)')

        return anime_embed

    def searchCharacterInfo(self, characterName):
        characterName = characterName.strip().replace("// get character ", "")
        characterName = characterName.strip().replace("// search character ", "")
        print(f"Character Name >{characterName}<")

        data = anilistBot.getCharacterInfo(characterName)
        first_name = data['first_name']
        last_name = data['last_name']
        native_name  = data['native_name']
        desc = data['desc']
        image = data['image']

        char_name = f"{first_name} {last_name}"

        character_link = f'https://anilist.co/character/{anilistBot.getCharacterID(characterName)}/'
        link = f"[AniList Page]({character_link})\
                \n[AnilistPython Documentation](https://pypi.org/project/AnilistPython/)"

        #parse desc
        if desc != None and len(desc) != 0:
            desc = desc.strip().replace('<br>', '')
            desc = desc.strip().replace('<i>', '')
            desc = desc.strip().replace('</i>', '')
        
        info = [first_name, last_name, native_name, desc, image]
        info = self.embedValueCheck(self, info)
        print(len(info[3]))
        print(len(link))

        char_embed = discord.Embed(title=char_name, description=native_name, color=0xFF8DA1)
        char_embed.set_image(url=image)
        char_embed.add_field(name="Description", value=info[3], inline=False)
        char_embed.add_field(name="Links", value=link, inline=False)
        char_embed.set_footer(text='Supported by the AnilistPython Library (ReZeroK)')

        return char_embed

    # Helper Functions ===================================================================================
    def removeSpecialChar(self, input) -> str:
        message = input
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        for i in message:
            if re.search("[A-Za-z0-9]", i) == None and regex.search(i) == None:
                message = message.replace(i, ' ')
        return message

    def embedValueCheck(self, arr) -> list:
        MAXLEN = 1024
        index = 0
        for i in arr:

            # Null value check ===============================================
            if i == None:
                arr[index] = 'Not Available'
            if isinstance(i, str) and len(i) == 0:
                arr[index] = 'Not Available'

            # Length check ===================================================
            if isinstance(i, str) and len(i) >= MAXLEN:
                toCrop = (len(i) - MAXLEN) + 3
                arr[index] = i[: -toCrop] + "..."
                        
            index += 1
        return arr