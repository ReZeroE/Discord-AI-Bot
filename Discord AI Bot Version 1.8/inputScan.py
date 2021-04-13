import re
from clearanceScan import clearanceScan
clScanPointer = clearanceScan()

guild_ID = 000000000000000000

class inputScan:
    def __init__(self):
        #layer zero - passive functions / override
        self.translationPrefix = 'translated text:'
        self.override = 'permission override>>'

        # layer one - prefix
        self.prefix = '//'
        self.web = 'https'

        # layer two - specified commands
        self.exitCommand = 'sys.exit(0)'
        self.timerCheck = 'check timer'
        self.timerRefresh = 'refresh timer'
        self.staffEmbed = 'update staff embed'
        self.purge = 'purge'
        self.rulesEmbed = 'update rules'
        self.getPermission = 'get perm'

        # layer two - non specified commands
        self.pickCommand = 'pick'
        self.rateCommand = 'rate'

        self.getAnimeInfo = 'get anime'
        self.getAnimeInfo2 = 'search anime'
        self.getCharacter = 'get character'
        self.getCharacter2 = 'search character'

        self.getAnimeID = 'get anime id'
        self.getCharacterID = 'get character id'

    def scanInput(self, userInput, guildID, userID):
        clearance = clScanPointer.clearanceScan(userID)

        # admin override
        if userInput.find(self.override) != -1:
            
            if clearance == 'C2':
                print('Admin 0 - override')
                clearance = 'C1'
                pass
            else:
                return "Permission Override Denied (C0D)"

        # Not functioning in guild
        if guildID != guild_ID and userInput.find(self.prefix) != -1:
            if clearance == 'C1':
                pass
            elif userInput.find(self.web) == -1:
                return 'Error 0 - None functional guild'

        # layer zero - passive functions ===================================================================
        if userInput.find(self.translationPrefix) == -1 and re.search('[a-zA-Z]', userInput) == None\
            and userInput.find(self.prefix) == -1:
            return 'Passive 0 - Translation'

        # layer one - prefix ===============================================================================
        if userInput.find(self.prefix) != -1 and userInput.find(self.web) == -1:
            
            #self.pickCommand ==============================================================================
            if userInput.find(self.pickCommand) != -1:
                return 'Command 0 - Pick Message'

            if userInput.find(self.rateCommand) != -1:
                return 'Command 1 - Rate Message'

            # layer two - specified commands ===============================================================
            if userInput.find(self.exitCommand) != -1:
                if clearance == 'C1' or clearance == 'C2':
                    return 'Code 0 - Program Exit'
                else:
                    return "You don't have enough clearance to use this command! (C2D)"

            elif userInput.find(self.timerCheck) != -1 or userInput.find(self.timerRefresh) != -1:
                return 'Code 1 - Check/Refresh Timer'

            elif userInput.find(self.staffEmbed) != -1:
                if clearance == 'C1' or clearance == 'C2':
                    return 'Code 2 - Staff Embed'
                else:
                    return "You don't have enough clearance to use this command! (C2D)"

            elif userInput.find(self.purge) != -1:
                if clearance == 'C1' or clearance == 'C2':
                    return 'Code 3 - Purge'
                else:
                    return "You don't have enough clearance to use this command! (C2D)"

            elif userInput.find(self.rulesEmbed) != -1:
                if clearance == 'C1':
                    return 'Code 4 - Rules Embed'
                else:
                    return "You don't have enough clearance to use this command! (C1D)"

            elif userInput.find(self.getPermission) != -1:
                return 'Code 5 - Get Permission'

            elif userInput.find(self.getAnimeInfo) != -1 or userInput.find(self.getAnimeInfo2) != -1:
                return "Code 6 - Search Anime Info"

            elif userInput.find(self.getCharacter) != -1 or userInput.find(self.getCharacter2) != -1:
                return "Code 7 - Search Character Info"

            return 'Not-Specified-Command'
        return 'None-Command'
