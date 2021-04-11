import discord


# info ---------------------------------------------------------------------------------------------------------------------------------------

line_one = '--------------------------------------------------'             
title_one = '★ Welcome to the Wonder Egg Priority Discord Server! ★'
value_one = "A story of troubled girls, spun by screenwriter Shinji Nojima in the world of anime.\
            \n\u200b\nLed by a mysterious voice while on a midnight stroll, 14-year-old girl Ai Ooto picks\
            up an egg. The voice coaxes her: \"If you want to change the future, you only need to choose now.\
            Now, believe in yourself and break the egg.\"\
            \n\u200b\nWhat awaits Ai after the breaking of the egg...\
            \n\u200b\nPermanent Server Invite Link: https://discord.gg/RxahGwTGmG"

# Image ---------------------------------------------------------------------------------------------------------------------------------------

image_link = "https://i.imgur.com/pszaNjj.png"

image_link2 = 'https://i.imgur.com/1uVBU2h.jpg'

# rules ---------------------------------------------------------------------------------------------------------------------------------------

# spoiler dis: <#798635188867170364>
# contact mods: <#797943336542797844>

rule_sub_title = "\u200b"

rule_title_one = '#1 No Foul/Inappropriate content'
rules_one = "- No offensive or inappropriate messages. If it's filtered, do not evade. Evading will result in extra consequences.\
            \n- Do not denounce characters or series for meme reasons. Constructive discussions are welcome, but doing otherwise \
            might result in unwanted rifts in the community."

rule_title_two = '#2 No advertising'
rules_two = "- Includes inviting people to other servers, social media accounts, etc.\
            \n- If you are invited by someone who you do not know to another server, report it to Staff immediately.\
            \n- In addition to the person who sent the invite, people who fail to report and join are at risk of being banned themselves." 

rule_title_three = '#3 Impersonation'
rules_three = "- No offensive or inappropriate messages. If it's filtered, do not evade. Evading will result in extra consequences." 

rule_title_four = '#4 Appeals and Issues'
rules_four = '- Do not discuss staff actions in the channels or staff DMs.\
            \n- If you wish to contest an infraction or discuss a staff action, please use the <#797943336542797844> channel.'

rule_title_five = '#5 No awkward/controversial topics'
rules_five = '- Religion, politics, flirting, etc.\
            \n- This includes anything controversial as well as anything regarding suicide. (Exceptions include the #serious-chat channel.\
            To access this channel please go to <#799055225448824863>).\
            \n- Staff members are not counselors if necessary seek professional help.'

rule_title_six = '#6 Use only English'
rules_six = '- Unless you are quoting text in the context of the series. Currently the staff team is unable to moderate any\
            language other than English. '

rule_title_seven = '#7 No public drama and roleplay'
rules_seven = '- Solve any issues through the <#797943336542797844> channel.\
            \n- Any inappropriate DMs from users should be reported to staff as soon as possible.'

rule_title_eight = '#8 Do not attempt to take advantage of server rules loopholes'
rules_eight = '- This will have corresponding consequences if done on purpose. A direct ban may be placed under certain conditions without any warning.'

rule_title_nine = '#9 Regarding Spoilers'
rules_nine = '- All contents in an episode are considered to be in spoiler territory until the next episode airs.\
            \n- Spoiler content can only be sent in <#798635188867170364>.'

rule_title_ten = '#10 Lastly, abide by Discord Terms of Service and Guidelines at all times'
rules_ten = '\nAny further issue not stated here is up to the discretion of moderators and these rules are subject to change at any time without prior notice.'


# staff ---------------------------------------------------------------------------------------------------------------------------------------

staff_title = 'Server Staff ♔'
staff_subtitle = "♔"
staff_cont = "These members help out in various parts of the server and outside of it, they are listed below for convenience in the case you need to contact one of these members.\
            \n\u200b\nAdmin:\n<@273474320544694274>\
            \n\u200b\nServer Moderators:\n<@624227532685967380>\n<@186563462330056704>\
            \n\u200b\nGeneral Moderators: <@405049915719286794>, <@342031270244515851>\
            \nAffiliation Moderators: <@357985032792440834>, <@186563462330056704>\
            \nReception Moderators: <@640921854478909465>\
            \nReddit Moderators: <@357985032792440834>, <@186563462330056704>\
            \n\u200b\nNote: If an urgent matter arises, feel free to use the <#797943336542797844> channel for the fastest reply."


class discordEmbed():

    def embed_info(self):
        embedPlacehold = discord.Embed(title=title_one, description=value_one, color=0x2bcf39)
        return embedPlacehold

    def embed_image_one(self):
        e = discord.Embed(color=0x2bcf39)
        e.set_image(url=image_link)
        return e

    def embed_image_rules(self):
        e = discord.Embed(color=0x2bcf39)
        e.set_image(url=image_link2)
        return e

    def embed_rules_one(self):
        embedPlacehold = discord.Embed(title=rule_title_one, description=rules_one, color=0x2bcf39)
        return embedPlacehold

    def embed_rules_two(self):
        embedPlacehold = discord.Embed(title=rule_title_two, description=rules_two, color=0x2bcf39)
        return embedPlacehold

    def embed_rules_three(self):
        embedPlacehold = discord.Embed(title=rule_title_three, description=rules_three, color=0x2bcf39)
        return embedPlacehold

    def embed_rules_four(self):
        embedPlacehold = discord.Embed(title=rule_title_four, description=rules_four, color=0x2bcf39)
        return embedPlacehold

    def embed_rules_five(self):
        embedPlacehold = discord.Embed(title=rule_title_five, description=rules_five, color=0x2bcf39)
        return embedPlacehold

    def embed_rules_six(self):
        embedPlacehold = discord.Embed(title=rule_title_six, description=rules_six, color=0x2bcf39)
        return embedPlacehold

    def embed_rules_seven(self):
        embedPlacehold = discord.Embed(title=rule_title_seven, description=rules_seven, color=0x2bcf39)
        return embedPlacehold

    def embed_rules_eight(self):
        embedPlacehold = discord.Embed(title=rule_title_eight, description=rules_eight, color=0x2bcf39)
        return embedPlacehold

    def embed_rules_nine(self):
        embedPlacehold = discord.Embed(title=rule_title_nine, description=rules_nine, color=0x2bcf39)
        return embedPlacehold

    def embed_rules_ten(self):
        embedPlacehold = discord.Embed(title=rule_title_ten, description=rules_ten, color=0x2bcf39)
        return embedPlacehold


    def embed_staff(self):
        embedPlacehold = discord.Embed(title=staff_title, description=staff_cont, color=0x2bcf39)
        return embedPlacehold



    # contact staff ---------------------------------------------------------------------------------------------------------------------------------------
    # contact-mods channel ID: <#811156156113223718>

    def contact_mods(self, contactmod_channel_ID):
        contact_staff_title = "How to contact moderators ♔"
        contact_staff = f"For any server suggestion or feedback, feel free to leave them in <#{contactmod_channel_ID}>\
                    Please only use 'Contact Mods' when an urgent issue arises (user reports/server malfunctions/etc).\
                    \n(Feel free to use this if it is an server collab request or similar)\
                    \n\nA server admin or mod will be with you shortly once you've clicked on the 'letter' reaction below."

        embedPlacehold = discord.Embed(title=contact_staff_title, description=contact_staff, color=0xFFC0CB)
        return embedPlacehold

'''
def test_embed():
    embedPlacehold = discord.Embed(title='title', color=0xffbf00)
    embedPlacehold.add_field(name="abc\aabc", value='test\ntest2\atest3\u200btest4', inline=False)
    return embedPlacehold

# embedPlacehold.add_field(name="Rule One", value="Test - This is rule #1", inline=False)
'''




'''
        \n\n**#2 No advertising**\
        \n- Includes inviting people to other servers, social media accounts, etc.\
        \n- If you are invited by someone who you do not know to another server, report it to Staff immediately.\
        \n- In addition to the person who sent the invite, people who fail to report and join are at risk of being banned themselves.\
        \
        \n\n**#3 Impersonation**\
        \n- No offensive or inappropriate messages. If it's filtered, do not evade. Evading will result in extra consequences.\
        \
        \n\n**#4 Appeals and Issues**\
        \n- Do not discuss staff actions in the channels or staff DMs.\
        \n- If you wish to contest an infraction or discuss a staff action, please use the #contact-mods channel.\
        \
        \n\n**#5 No awkward/controversial topics**\
        \n- Religion, politics, flirting, etc.\
        \n- This includes anything controversial as well as anything regarding suicide.\
        \n- Staff members are not counselors if necessary seek professional help.\
        \
        \n\n**#6 Use only English**\
        \n- Unless you are quoting text in the context of the series.\
        \
        \n\n**#7 No public drama and roleplay**\
        \n- Solve any issues through the #contact-mods channel.\
        \n- Any inappropriate DMs from users should be reported to staff as soon as possible.\
        \
        \n\n**#8 Do not attempt to take advantage of server rules loopholes.**\
        \n- This will have corresponding consequences if done on purpose.\
        \
        \n\n**#9 Regarding Spoilers**\
        \n- All contents in an episode are considered to be in spoiler territory until the next episode airs.\
        \n- Spoiler content can only be sent in #spoiler-discussion.\
        \
        \n\n**#10 Lastly, abide by Discord Terms of Service and Guidelines at all times**\
        \
        \n\nAny further issue not stated here is up to the discretion of moderators and these rules are subject to change at any time without prior notice."
        '''