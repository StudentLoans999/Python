# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands

import asyncio
import random
import datetime

rpscpu_firsttogo = False
rpscpu_finished = False
rpscpu_gotime = 0
rpscpu_setround = 0
rpscpu_currentround = 0
rpscpu_go = False
dorpscpu = False
rpscpu_botsaidgo = False
rpscpu_rockcpu = False
rpscpu_papercpu = False
rpscpu_scissorscpu = False

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create Rock_Paper_Scissors_CPU Class
class Rock_Paper_Scissors_CPU(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

# # # Event Listener: Bot on_ready - For when Rock_Paper_Scissors_CPU has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('Rock_Paper_Scissors_CPU has loaded')

# # # Event Listener: Bot on_message - For when a User does !rps in the wrong channel [doesn't work with DMs], have that message deleted (so the channel doesn't get filled up)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # ignore messages from bot
    
        if isinstance(message.channel, discord.TextChannel) and message.channel.name != "rock-paper-scissors-cpu": # delete "isinstance(message.channel, discord.TextChannel) and" if it causes errors later
            if message.content == "!rps" or message.content == "!rock" or message.content == "!paper" or message.content == "!scissors":
                await message.delete()

###############################################################################################################################################################################################################

#
# # Command section ############################################################################
#

# # # Command: !rps ; When a User does !rps in the rock-paper-scissors-cpu channel, then the game: Rock, Paper, Scissors - CPU starts EX: !rps
    @commands.hybrid_command(name='rps', description = 'Play Rock, Paper, Scissors - CPU (go to rock-paper-scissors-cpu Channel first)')
    async def rps(self, ctx:commands.Context):
        global rpscpu_firsttogo # start the game
        global rpscpu_finished
        global rpscpu_setround
        global rpscpu_currentround
        global rpscpu_go
        global dorpscpu
        global rpscpu_botsaidgo

         # Makes sure !rps can only be run in the right channel
        if ctx.channel.name != "rock-paper-scissors-cpu": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!rps** which is specific to the Channel: <#1172306707049889812> Please go there and try it")    
        
        elif ctx.channel.name == "rock-paper-scissors-cpu": # the command was done in the correct Channel: rock-paper-scissors-cpu
            
            # Player did !rps but the Game has already started

            if rpscpu_firsttogo == True:
                await ctx.author.send("The game has already started, so **!rps** won't do anything")
            
            else: # rps has not been started already, so let it get started and run its logic
                rpscpu_firsttogo = True#9

                user = ctx.author
                channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu") # makes sure it only looks for users in the Channel: rock-paper-scissors-cpu
                members = channel.members

                for user in channel.members:#1234
                    fresh_member = await self.bot.fetch_user(user.id)
                    guild_member = channel.guild.get_member(fresh_member.id)
                    fresh_roles = guild_member.roles

                # Removes Eliminated and Winners Roles applied to users, and gives everyone the Players role, so that everything is fresh for a new game
                Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")

                for user in members:
                    if user.name == "ChatBot":
                        print()

                    else:
                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        for user in members:
                            if user.name == "ChatBot":
                                print()

                            else:
                                Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                                await user.add_roles(Players_role)
                                await user.remove_roles(Winners_role)
                                await user.remove_roles(Eliminated_role)
                                Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                                await user.remove_roles(Waiting_role)

##### Scoreboard section                    ######################

                # The last round has just finished, so do the scoreboard and conclusion logic
                if rpscpu_currentround > int(rpscpu_setround):

                    for user in channel.members:#1234
                        fresh_member = await self.bot.fetch_user(user.id)
                        guild_member = channel.guild.get_member(fresh_member.id)
                        fresh_roles = guild_member.roles

                    Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                    Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")

                    if Winners_role is not None: # if there are any Winners in the server             

                        if channel is not None and isinstance(channel, discord.TextChannel): # makes sure it only looks for users in the Channel: rock-paper-scissors-cpu
                            # Get a list of members with the target role in the specified channel
                            members_with_Winners_role = [member for member in channel.members if Winners_role in member.roles] # gets a list of users with the Winner role in the Channel: rock-paper-scissors-cpu
                            members_with_Winners_role_and_online = [member for member in Winners_role.members if member.status == discord.Status.online] # makes sure to only get users who are Online

                            if members_with_Winners_role_and_online: # outputs the Winners in the match and still Online in the match, if there are any 
                                user_list = "\n".join([member.name for member in members_with_Winners_role_and_online]) # prints the list of Online users with the Winners role in the Channel: rock-paper-scissors-cpu
                                print(f'Users with the role {Winners_role} in the channel {channel}:\n{user_list} are a Winner!!!')
                                await ctx.send(f'_ _ \nPlayer(s) who have won a round in this match and who are still Online are: \n**{user_list}**\n')
                            
                            else: # outputs that there are no Winners in this match
                                print(f'No users have the role {Winners_role} in the channel {channel}.')
                                await ctx.send(f'_ _ \nThere are no winners in this match')

                        else: # outputs that the wrong Channel has been called 
                            print(f'The channel {channel} does not exist or is not a text channel in this server.')
                    
                    else: # there are no Winners in the server
                            print(f'The role {Winners_role} does not exist in this server.')
                    
                    if Eliminated_role is not None: # if there are any Eliminated in the server                

                        if channel is not None and isinstance(channel, discord.TextChannel): # makes sure it only looks for users in the Channel: rock-paper-scissors-cpu
                            
                            members_with_Eliminated_role = [member for member in channel.members if Eliminated_role in member.roles] # gets a list of users with the Eliminated role in the Channel: rock-paper-scissors-cpu
                            members_with_Eliminate_role_and_online = [member for member in Eliminated_role.members if member.status == discord.Status.online] # makes sure to only get users who are Online

                            if members_with_Eliminate_role_and_online: # outputs the Eliminated and still Online in the match, if there are any
                                user_list = "\n".join([member.name for member in members_with_Eliminate_role_and_online]) # prints the list of Online users with the Eliminated role in the Channel: rock-paper-scissors-cpu
                                print(f'Users with the role {Eliminated_role} in the channel {channel}:\n{user_list} are a Loser :(')
                                await ctx.send(f'_ _ \nPlayer(s) who have been eliminated in this match and who are still Online are: \n**{user_list}**\n')
                            
                            else: # outputs that there are no Eliminated in this match
                                print(f'No users have the role {Eliminated_role} in the channel {channel}.')
                                await ctx.send(f'_ _ \nNo one has been eliminated in this match')
                        
                        else: # outputs that the wrong Channel has been called 
                            print(f'The channel {channel} does not exist or is not a text channel in this server.')
                    
                    else: # there are no Eliminated in the server
                            print(f'The role {Eliminated_role} does not exist in this server.')

                    # Concludes the game ; Removes Eliminated and Winners Roles applied to users, and gives everyone the Players role, so that everything is fresh for a new game
                    for user in members:
                        if user.name == "ChatBot":
                            print()

                        else:
                            for user in channel.members:#1234
                                fresh_member = await self.bot.fetch_user(user.id)
                                guild_member = channel.guild.get_member(fresh_member.id)
                                fresh_roles = guild_member.roles

                            for user in members:
                                if user.name == "ChatBot":
                                    print()

                                else:
                                    Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                                    await user.add_roles(Players_role)
                                    await user.remove_roles(Winners_role)
                                    await user.remove_roles(Eliminated_role)
                                    Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                                    await user.remove_roles(Waiting_role)
                            
                    await ctx.send(f'_ _ \nThe game has concluded. Thank you for playing!')
                    rpscpu_firsttogo = False#9
                    rpscpu_setround = 0
                    rpscpu_currentround = 0
                    rpscpu_go = False
                    dorpscpu = False
                    rpscpu_botsaidgo = False
                    return

##### First Round Setup section                    ######################

                # The game has just started, so do the first round logic
                if rpscpu_currentround == 0:
                    for user in members: # removes Eliminated and Winners Roles applied to users
                        if user.name == "ChatBot":
                            print()

                        else:
                            for user in channel.members:#1234
                                fresh_member = await self.bot.fetch_user(user.id)
                                guild_member = channel.guild.get_member(fresh_member.id)
                                fresh_roles = guild_member.roles

                            Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")
                            await user.remove_roles(Eliminated_role)
                            Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                            await user.remove_roles(Winners_role)
                            Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                            await user.remove_roles(Waiting_role)
                            Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                            await user.add_roles(Players_role)

                    def check(msg): # makes sure the user has input a number, and that it is the user who did !rps specifically  
                        if msg.author == ctx.author:
                            msg = msg.content
                            if [int(s) for s in msg.split() if s.isdigit()]:
                                return msg

                    try: # starts off the game by asking the player to input how many rounds they want to play
                        await ctx.reply("How many rounds would you like to play **Rock, Paper, Scissors - CPU**?\n\n Please enter a number:")
                        msg = None # default value
                        
                        try:
                            msg = await ctx.bot.wait_for("message", check = check, timeout = 10)
                        except Exception as e:
                            await ctx.reply("\nSorry, you didn't reply in time or you didn't input a positive integer! Please do **!rps** to try again")
                            rpscpu_firsttogo = False#9
                            return
                        
                        rpscpu_setround = msg.content

                        if int(rpscpu_setround) <= 0: # checks for if the user put in a zero or negative integer
                            print("Bad number")
                            print(rpscpu_setround)
                            await ctx.reply("\nIt seems like you don't want to play. Please do **!rps** when you do want to")
                            rpscpu_firsttogo = False#9
                            return
                        else:
                            print("Good number")
                            print(rpscpu_setround)

                        print(rpscpu_currentround)
                        rpscpu_currentround += 1
                        await ctx.send(f"""We are going to do **{rpscpu_setround}** round(s).
                                        \nThe rules of this game are to say "**!rock**" or "**!paper**" or "**!scissors**" as soon as "Go" appears, to try to beat the Bot.
                                        \nBut, do not say anything before that, or else you'll be eliminated for the entire match.
                                       \nOnly one person has to input something to throw within a random time limit between 3-15 seconds after "Go" appears.
                                       \nIf no one inputs a move within that time limit, then everyone will be eliminated.
                                        \nFor the person who did a move, if the Bot beats you, you'll be eliminated.
                                        \nIn the case of tying, you neither win nor lose the round (so you won't get eliminated).
                                        \n This is a game of luck and risk. Good luck and have fun!""")
                        
                    except asyncio.TimeoutError: # tells the user that the game has been cancelled and has to be rerun, because they didn't input the round request in time
                        print(rpscpu_currentround)
                        await ctx.reply("\nSorry, you didn't reply in time! Do **!rps** to try again")
                        rpscpu_firsttogo = False#9
                        return

##### Gameplay Setup section                    ######################

                # This is the first round of the game, or a round of the game has just finished, so do the gameplay (next round) logic
                if (rpscpu_currentround > 0) and (rpscpu_currentround <= int(rpscpu_setround)):
                    for user in channel.members:#1234
                        fresh_member = await self.bot.fetch_user(user.id)
                        guild_member = channel.guild.get_member(fresh_member.id)
                        fresh_roles = guild_member.roles

                    await ctx.send(f'_ _ \n**Round {rpscpu_currentround} of {rpscpu_setround}**\n')
                    await ctx.channel.send('_ _ \nReady')
                    await asyncio.sleep(1)
                    await ctx.channel.send('_ _ \nSet')
                    rpscpu_go = False
                    dorpscpu = False
                    rpscpu_randompause = random.randint(1, 10) # set to send "Go" at a random time between 1-10 seconds
                    await asyncio.sleep(rpscpu_randompause)

                    if rpscpu_go == False: # the Bot will send "Go" at a random time (this starts the gameplay)
                        sendcpu_go = await ctx.channel.send('_ _ \nGo') # use _ _ to do a new line at the beginning of a message
                        sendcpu_go # have to assign it as a variable in order to do .content.split() (I think, at least)
                        gocpu_sent = sendcpu_go.content.split()[2] # I did '2' instead of '0' because '0' only outputs the '_' instead of the actual word
                        gocpu_sent_comparison = gocpu_sent[:2] # I did '2' to get only the first two characters of the string (since I want to compare them to "Go")
                        
                        # Bot sent a message that said "Go"
                        if gocpu_sent_comparison == "Go":
                            bot_options = ["rock", "paper", "scissors"] # the different options for the Bot to draw
                            bot_decision = random.choice(bot_options) # set to have the Bot make a choice of what to deaw
                            bot_decision
                            print(bot_decision)

                            if bot_decision == "rock": # Bot chose rock
                                rpscpu_rockcpu = True#9
                                rpscpu_papercpu = False
                                rpscpu_scissorscpu = False
                            elif bot_decision == "paper": # Bot chose paper
                                rpscpu_rockcpu = False
                                rpscpu_papercpu = True
                                rpscpu_scissorscpu = False
                            elif bot_decision == "scissors": # Bot chose scissors
                                rpscpu_rockcpu = False
                                rpscpu_papercpu = False
                                rpscpu_scissorscpu = True

                            print(f"Rock CPU is: {rpscpu_rockcpu}")
                            print(f"Paper CPU is: {rpscpu_papercpu}")
                            print(f"Scissors CPU is: {rpscpu_scissorscpu}")

                            rpscpu_finished = True
                            rpscpu_go = True # sets the Bot to start off the gameplay

##### User did not do !rock or !paper or !scissors section                    ######################
            
                    while rpscpu_go == True and dorpscpu == False: # Bot sent a message that said "Go", so do the verification logic and then the timer for message response logic 
                        try: # first check if every user in the channel is eliminated, if not, then ; wait between 3-15 seconds, if no input given, then everyone gets eliminated
                            for user in members: # looks for all the people in the Channel rock-paper-scissors-cpu that have the Eliminated role
                                Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")
                            
                            if Eliminated_role is not None: # checks if there are any non-Eliminated players       

                                if channel is not None and isinstance(channel, discord.TextChannel): # makes sure it only looks for users in the Channel: rock-paper-scissors-cpu
                                    
                                    for member in channel.members:
                                        if Eliminated_role not in member.roles:

                                            print()#f'There are players who are not eliminated, so someone should be able to do !rock or !paper or !scissors, so go ahead and start the timer')
                                            rpscpu_randomwait = random.randint(3, 15) 
                                            await asyncio.sleep(rpscpu_randomwait)
                                            raise asyncio.TimeoutError

                        except asyncio.TimeoutError:
                            if rpscpu_go == True and dorpscpu == False:
                                await ctx.send("_ _ \n**No one responded in time ; the match is now concluded.**")
                                channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")
                                members = channel.members

                                # So make all users, except for Winners, eliminated
                                Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")

                                Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")
                                
                                for user in members: 
                                    members_with_role = [member for member in channel.members if Winners_role in member.roles] # gets a list of users with the Winner role in the Channel: rock-paper-scissors-cpu
                                    if members_with_role: 
                                        ctx.send(members_with_role) # bot says the Winners in the match, if there are any 
                                    elif user.name == "ChatBot": # bot can't get Eliminated
                                        await user.remove_roles(Eliminated_role)                           
                                    else:
                                        await user.add_roles(Eliminated_role) # everyone, besides the Winners, get Eliminated

                                # Now all users are eliminated, so go to scoreboard logic
                                Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                            
                                rpscpu_currentround = int(rpscpu_setround) + 1
                                print(rpscpu_currentround)
                                rpscpu_finished = False
                                rpscpu_firsttogo = False#9
                                
                                for user in channel.members:#1234
                                    fresh_member = await self.bot.fetch_user(user.id)
                                    guild_member = channel.guild.get_member(fresh_member.id)
                                    fresh_roles = guild_member.roles

                                rpscpu_restart = ctx.bot.get_command('rps')
                                await rpscpu_restart(ctx)
                            
                            else:
                                print(f'!rock or !paper or !scissors has been done or the next round has started')

##### Gameplay section                    ######################

# # # Command: !rock ; Player does !rock after he sees "Go" to try to beat scissors. EX: !rock
    @commands.hybrid_command(name='rock', description = 'Do this command when "Go" appears to beat scissors. (If done before "Go" appears, you lose)')
    async def rock(self, ctx:commands.Context):
        global rpscpu_firsttogo#9
        global rpscpu_finished
        global rpscpu_gotime
        global rpscpu_setround
        global rpscpu_currentround
        global rpscpu_go
        global dorpscpu
        global rpscpu_rockcpu
        global rpscpu_papercpu
        global rpscpu_scissorscpu

        # Makes sure !rock can only be run in the right channel 
        if ctx.channel.name != "rock-paper-scissors-cpu": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!rock** which is specific to the Channel: <#1172306707049889812> Please go there and try it")
        
        elif ctx.channel.name == "rock-paper-scissors-cpu": # the command was done in the correct Channel: rock-paper-scissors-cpu
            
            if rpscpu_firsttogo: # the game has been started
                user = ctx.author

                if rpscpu_finished == False: # the Bot has not said "Go" yet
                    Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")

                    for role in ctx.guild.roles:
                        if role.name == "Eliminated": # if an eliminated player does !rock, then they are told that they are already eliminated
                            await ctx.reply(f'You were already eliminated')

                        elif role.name != "Eliminated": # if a non-eliminated player does !rock, then they are eliminated for doing it too early
                            await ctx.reply(f'You went too early ; now you are eliminated')
                            await user.add_roles(Eliminated_role)
                            Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                            await user.remove_roles(Players_role)
                            return
                
                channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")

                if rpscpu_finished == True: # the Bot has said "Go"
                    rpscpu_rockcpu = True
                    print(f"rpscpu_scissorscpu is: {rpscpu_scissorscpu}")
                    print(f"rpscpu_papercpu is: {rpscpu_papercpu}")
                    print(f"rpscpu_rockcpu is: {rpscpu_rockcpu}")

                    if rpscpu_scissorscpu == True: # Bot did scissors, so Player beats Bot
                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")
                        members = channel.members
                        Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        
                        for user in members:
                            await user.add_roles(Waiting_role)

                        await ctx.reply(f'You **beat** the Bot since you did **rock** and it did **scissors**. Hooray, you have won this round!!\n')
                        await ctx.send("Doing next round now")
                        rpscpu_go = False 
                        dorpscpu = True
                        rpscpu_currentround +=1
                        print(rpscpu_currentround)
                        rpscpu_finished = False
                        rpscpu_firsttogo = False

                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        await ctx.message.author.remove_roles(Players_role)
                        Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                        await ctx.message.author.add_roles(Winners_role)

                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        for user in members:
                            if user.name == "ChatBot":
                                await user.remove_roles(Waiting_role)

                            else:
                                for role in ctx.guild.roles: # if a Winner or Eliminated, then stay that role, otherwise make everyone a Player again
                                    if role.name == "Winners":
                                        await user.remove_roles(Waiting_role)
                                    elif role.name == "Eliminated": 
                                        await user.remove_roles(Waiting_role)
                                    else:
                                        await user.remove_roles(Waiting_role)
                        
                        rpscpu_restart = ctx.bot.get_command('rps')
                        await rpscpu_restart(ctx)

                    elif rpscpu_papercpu == True: # Bot did paper, so Player lost to Bot
                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")
                        members = channel.members
                        Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        
                        for user in members:
                            await user.add_roles(Waiting_role)

                        await ctx.reply(f'You **lost** to the Bot since you did **rock** and it did **paper**\n')
                        await ctx.send("Doing next round now")
                        rpscpu_go = False 
                        dorpscpu = True
                        rpscpu_currentround +=1
                        print(rpscpu_currentround)
                        rpscpu_finished = False
                        rpscpu_firsttogo = False

                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        await ctx.message.author.remove_roles(Players_role)
                        Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")
                        await ctx.message.author.add_roles(Eliminated_role)

                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        for user in members:
                            if user.name == "ChatBot":
                                await user.remove_roles(Waiting_role)

                            else:
                                for role in ctx.guild.roles: # if a Winner or Eliminated, then stay that role, otherwise make everyone a Player again
                                    if role.name == "Winners":
                                        await user.remove_roles(Waiting_role)
                                    elif role.name == "Eliminated": 
                                        await user.remove_roles(Waiting_role)
                                    else:
                                        await user.remove_roles(Waiting_role)

                        rpscpu_restart = ctx.bot.get_command('rps')
                        await rpscpu_restart(ctx)

                    elif rpscpu_rockcpu == True: # Bot did rock, so Player tied to Bot
                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")
                        members = channel.members
                        Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        
                        for user in members:
                            await user.add_roles(Waiting_role)

                        await ctx.reply(f'You **tied** with the Bot since you did **rock** and it did **rock** too. You have neither won nor lost this round!\n')
                        await ctx.send("Doing next round now")
                        rpscpu_go = False 
                        dorpscpu = True
                        rpscpu_currentround +=1
                        print(rpscpu_currentround)
                        rpscpu_finished = False
                        rpscpu_firsttogo = False

                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        await ctx.message.author.remove_roles(Players_role)
                        await ctx.message.author.add_roles(Players_role)

                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        for user in members:
                            if user.name == "ChatBot":
                                await user.remove_roles(Waiting_role)

                            else:
                                for role in ctx.guild.roles: # if a Winner or Eliminated, then stay that role, otherwise make everyone a Player again
                                    if role.name == "Winners":
                                        await user.remove_roles(Waiting_role)
                                    elif role.name == "Eliminated": 
                                        await user.remove_roles(Waiting_role)
                                    else:
                                        await user.remove_roles(Waiting_role)
                        
                        rpscpu_restart = ctx.bot.get_command('rps')
                        await rpscpu_restart(ctx)

                    else:
                        print("The Bot didn't make a decision correctly")

            else:
                # Player did !rock but the Game hasn't started
                await ctx.author.send("Hold your horses, **Rock, Paper, Scissors - CPU** hasn't started yet, so **!rock** won't do anything. If you would like to play, do **!rps** to start a game first")           

############################################################################

# # # Command: !paper ; Player does !paper after he sees "Go" to try to beat rock. EX: !paper
    @commands.hybrid_command(name='paper', description = 'Do this command when "Go" appears to beat rock. (If done before "Go" appears, you lose)')
    async def paper(self, ctx:commands.Context):
        global rpscpu_firsttogo
        global rpscpu_finished
        global rpscpu_gotime
        global rpscpu_setround
        global rpscpu_currentround
        global rpscpu_go
        global dorpscpu
        global rpscpu_rockcpu
        global rpscpu_papercpu
        global rpscpu_scissorscpu

        # Makes sure !paper can only be run in the right channel 
        if ctx.channel.name != "rock-paper-scissors-cpu": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!paper** which is specific to the Channel: <#1172306707049889812> Please go there and try it")
        
        elif ctx.channel.name == "rock-paper-scissors-cpu": # the command was done in the correct Channel: rock-paper-scissors-cpu
            
            if rpscpu_firsttogo: # the game has been started
                user = ctx.author

                if rpscpu_finished == False: # the Bot has not said "Go" yet
                    Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")

                    for role in ctx.guild.roles:
                        if role.name == "Eliminated": # if an eliminated player does !rock, then they are told that they are already eliminated
                            await ctx.reply(f'You were already eliminated')

                        elif role.name != "Eliminated": # if a non-eliminated player does !rock, then they are eliminated for doing it too early
                            await ctx.reply(f'You went too early ; now you are eliminated')
                            await user.add_roles(Eliminated_role)
                            Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                            await user.remove_roles(Players_role)
                            return
                
                channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")

                if rpscpu_finished == True: # the Bot has said "Go"
                    rpscpu_papercpu = True
                    print(f"rpscpu_scissorscpu is: {rpscpu_scissorscpu}")
                    print(f"rpscpu_papercpu is: {rpscpu_papercpu}")
                    print(f"rpscpu_rockcpu is: {rpscpu_rockcpu}")

                    if rpscpu_rockcpu == True: # Bot did rock, so Player beats Bot
                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")
                        members = channel.members
                        Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        
                        for user in members:
                            await user.add_roles(Waiting_role)

                        await ctx.reply(f'You **beat** the Bot since you did **paper** and it did **rock**. Hooray, you have won this round!!\n')
                        await ctx.send("Doing next round now")
                        rpscpu_go = False 
                        dorpscpu = True
                        rpscpu_currentround +=1
                        print(rpscpu_currentround)
                        rpscpu_finished = False
                        rpscpu_firsttogo = False

                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        await ctx.message.author.remove_roles(Players_role)
                        Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                        await ctx.message.author.add_roles(Winners_role)

                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        for user in members:
                            if user.name == "ChatBot":
                                await user.remove_roles(Waiting_role)

                            else:
                                for role in ctx.guild.roles: # if a Winner or Eliminated, then stay that role, otherwise make everyone a Player again
                                    if role.name == "Winners":
                                        await user.remove_roles(Waiting_role)
                                    elif role.name == "Eliminated": 
                                        await user.remove_roles(Waiting_role)
                                    else:
                                        await user.remove_roles(Waiting_role)
                        
                        rpscpu_restart = ctx.bot.get_command('rps')
                        await rpscpu_restart(ctx)

                    elif rpscpu_scissorscpu == True: # Bot did scissors, so Player lost to Bot
                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")
                        members = channel.members
                        Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        
                        for user in members:
                            await user.add_roles(Waiting_role)

                        await ctx.reply(f'You **lost** to the Bot since you did **paper** and it did **scissors**\n')
                        await ctx.send("Doing next round now")
                        rpscpu_go = False 
                        dorpscpu = True
                        rpscpu_currentround +=1
                        print(rpscpu_currentround)
                        rpscpu_finished = False
                        rpscpu_firsttogo = False

                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        await ctx.message.author.remove_roles(Players_role)
                        Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")
                        await ctx.message.author.add_roles(Eliminated_role)

                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        for user in members:
                            if user.name == "ChatBot":
                                await user.remove_roles(Waiting_role)

                            else:
                                for role in ctx.guild.roles: # if a Winner or Eliminated, then stay that role, otherwise make everyone a Player again
                                    if role.name == "Winners":
                                        await user.remove_roles(Waiting_role)
                                    elif role.name == "Eliminated": 
                                        await user.remove_roles(Waiting_role)
                                    else:
                                        await user.remove_roles(Waiting_role)

                        rpscpu_restart = ctx.bot.get_command('rps')
                        await rpscpu_restart(ctx)

                    elif rpscpu_papercpu == True: # Bot did paper, so Player tied to Bot
                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")
                        members = channel.members
                        Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        
                        for user in members:
                            await user.add_roles(Waiting_role)

                        await ctx.reply(f'You **tied** with the Bot since you did **paper** and it did **paper** too. You have neither won nor lost this round!\n')
                        await ctx.send("Doing next round now")
                        rpscpu_go = False 
                        dorpscpu = True
                        rpscpu_currentround +=1
                        print(rpscpu_currentround)
                        rpscpu_finished = False
                        rpscpu_firsttogo = False

                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        await ctx.message.author.remove_roles(Players_role)
                        await ctx.message.author.add_roles(Players_role)

                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        for user in members:
                            if user.name == "ChatBot":
                                await user.remove_roles(Waiting_role)

                            else:
                                for role in ctx.guild.roles: # if a Winner or Eliminated, then stay that role, otherwise make everyone a Player again
                                    if role.name == "Winners":
                                        await user.remove_roles(Waiting_role)
                                    elif role.name == "Eliminated": 
                                        await user.remove_roles(Waiting_role)
                                    else:
                                        await user.remove_roles(Waiting_role)
                        
                        rpscpu_restart = ctx.bot.get_command('rps')
                        await rpscpu_restart(ctx)

                    else:
                        print("The Bot didn't make a decision correctly")

            else:
                # Player did !paper but the Game hasn't started
                await ctx.author.send("Hold your horses, **Rock, Paper, Scissors - CPU** hasn't started yet, so **!paper** won't do anything. If you would like to play, do **!rps** to start a game first")           

############################################################################

# # # Command: !scissors ; Player does !scissors after he sees "Go" to try to beat paper. EX: !scissors
    @commands.hybrid_command(name='scissors', description = 'Do this command when "Go" appears to beat paper. (If done before "Go" appears, you lose)')
    async def scissors(self, ctx:commands.Context):
        global rpscpu_firsttogo
        global rpscpu_finished
        global rpscpu_gotime
        global rpscpu_setround
        global rpscpu_currentround
        global rpscpu_go
        global dorpscpu
        global rpscpu_rockcpu
        global rpscpu_papercpu
        global rpscpu_scissorscpu

        # Makes sure !scissors can only be run in the right channel 
        if ctx.channel.name != "rock-paper-scissors-cpu": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!scissors** which is specific to the Channel: <#1172306707049889812> Please go there and try it")
        
        elif ctx.channel.name == "rock-paper-scissors-cpu": # the command was done in the correct Channel: rock-paper-scissors-cpu
            
            if rpscpu_firsttogo: # the game has been started
                user = ctx.author

                if rpscpu_finished == False: # the Bot has not said "Go" yet
                    Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")

                    for role in ctx.guild.roles:
                        if role.name == "Eliminated": # if an eliminated player does !rock, then they are told that they are already eliminated
                            await ctx.reply(f'You were already eliminated')

                        elif role.name != "Eliminated": # if a non-eliminated player does !rock, then they are eliminated for doing it too early
                            await ctx.reply(f'You went too early ; now you are eliminated')
                            await user.add_roles(Eliminated_role)
                            Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                            await user.remove_roles(Players_role)
                            return
                
                channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")

                if rpscpu_finished == True: # the Bot has said "Go"
                    rpscpu_scissorscpu = True
                    print(f"rpscpu_scissorscpu is: {rpscpu_scissorscpu}")
                    print(f"rpscpu_papercpu is: {rpscpu_papercpu}")
                    print(f"rpscpu_rockcpu is: {rpscpu_rockcpu}")

                    if rpscpu_papercpu == True: # Bot did paper, so Player beats Bot
                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")
                        members = channel.members
                        Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        
                        for user in members:
                            await user.add_roles(Waiting_role)

                        await ctx.reply(f'You **beat** the Bot since you did **scissors** and it did **paper**. Hooray, you have won this round!!\n')
                        await ctx.send("Doing next round now")
                        rpscpu_go = False 
                        dorpscpu = True
                        rpscpu_currentround +=1
                        print(rpscpu_currentround)
                        rpscpu_finished = False
                        rpscpu_firsttogo = False

                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        await ctx.message.author.remove_roles(Players_role)
                        Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                        await ctx.message.author.add_roles(Winners_role)

                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        for user in members:
                            if user.name == "ChatBot":
                                await user.remove_roles(Waiting_role)

                            else:
                                for role in ctx.guild.roles: # if a Winner or Eliminated, then stay that role, otherwise make everyone a Player again
                                    if role.name == "Winners":
                                        await user.remove_roles(Waiting_role)
                                    elif role.name == "Eliminated": 
                                        await user.remove_roles(Waiting_role)
                                    else:
                                        await user.remove_roles(Waiting_role)
                        
                        rpscpu_restart = ctx.bot.get_command('rps')
                        await rpscpu_restart(ctx)

                    elif rpscpu_rockcpu == True: # Bot did rock, so Player lost to Bot
                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")
                        members = channel.members
                        Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        
                        for user in members:
                            await user.add_roles(Waiting_role)

                        await ctx.reply(f'You **lost** to the Bot since you did **scissors** and it did **rock**\n')
                        await ctx.send("Doing next round now")
                        rpscpu_go = False 
                        dorpscpu = True
                        rpscpu_currentround +=1
                        print(rpscpu_currentround)
                        rpscpu_finished = False
                        rpscpu_firsttogo = False

                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        await ctx.message.author.remove_roles(Players_role)
                        Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")
                        await ctx.message.author.add_roles(Eliminated_role)

                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        for user in members:
                            if user.name == "ChatBot":
                                await user.remove_roles(Waiting_role)

                            else:
                                for role in ctx.guild.roles: # if a Winner or Eliminated, then stay that role, otherwise make everyone a Player again
                                    if role.name == "Winners":
                                        await user.remove_roles(Waiting_role)
                                    elif role.name == "Eliminated": 
                                        await user.remove_roles(Waiting_role)
                                    else:
                                        await user.remove_roles(Waiting_role)

                        rpscpu_restart = ctx.bot.get_command('rps')
                        await rpscpu_restart(ctx)

                    elif rpscpu_scissorscpu == True: # Bot did scissors, so Player tied to Bot
                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        channel = discord.utils.get(ctx.guild.channels, name = "rock-paper-scissors-cpu")
                        members = channel.members
                        Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        
                        for user in members:
                            await user.add_roles(Waiting_role)

                        await ctx.reply(f'You **tied** with the Bot since you did **scissors** and it did **scissors** too. You have neither won nor lost this round!\n')
                        await ctx.send("Doing next round now")
                        rpscpu_go = False 
                        dorpscpu = True
                        rpscpu_currentround +=1
                        print(rpscpu_currentround)
                        rpscpu_finished = False
                        rpscpu_firsttogo = False

                        Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                        await ctx.message.author.remove_roles(Players_role)
                        await ctx.message.author.add_roles(Players_role)

                        for user in channel.members:#1234
                            fresh_member = await self.bot.fetch_user(user.id)
                            guild_member = channel.guild.get_member(fresh_member.id)
                            fresh_roles = guild_member.roles

                        for user in members:
                            if user.name == "ChatBot":
                                await user.remove_roles(Waiting_role)

                            else:
                                for role in ctx.guild.roles: # if a Winner or Eliminated, then stay that role, otherwise make everyone a Player again
                                    if role.name == "Winners":
                                        await user.remove_roles(Waiting_role)
                                    elif role.name == "Eliminated": 
                                        await user.remove_roles(Waiting_role)
                                    else:
                                        await user.remove_roles(Waiting_role)
                        
                        rpscpu_restart = ctx.bot.get_command('rps')
                        await rpscpu_restart(ctx)

                    else:
                        print("The Bot didn't make a decision correctly")

            else:
                # Player did !rock but the Game hasn't started
                await ctx.author.send("Hold your horses, **Rock, Paper, Scissors - CPU** hasn't started yet, so **!rock** won't do anything. If you would like to play, do **!rps** to start a game first")           

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(Rock_Paper_Scissors_CPU(bot)) # name of the Class, look above