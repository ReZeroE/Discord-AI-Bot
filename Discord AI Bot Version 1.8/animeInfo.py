
import discord

class animeInfo:
    def getAnimeName(self):
        return 'Wonder Egg Priority'
    
    def getAnimeDates(self):
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
        anime_dates.append('3/30/2021')
        return anime_dates

    def getAnimeTime(self):
        return '10:30:00'

    def getOPED(self):
        embed = discord.Embed()
        embed.description = "Sudachi no Uta [Opening] \
                            \n[Youtube Link](https://youtu.be/-EuXOT4lb0s) - [Spotify Link](https://open.spotify.com/track/0U3JBftbH2K1rzaMM2fav3) \
                            \nLife is Cider [Ending] \
                            \n[Youtube Link](https://youtu.be/7TGgvqNN0yk) - [Spotify Link](https://open.spotify.com/track/0U3JBftbH2K1rzaMM2fav3)"
        return embed
