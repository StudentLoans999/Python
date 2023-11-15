# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands

import asyncio
import random
import datetime

readysetgo_running = False
readysetgo_finished = False
readysetgo_gotime = 0
readysetgo_elapsedtime = 0
readysetgo_firsttogo = 0
readysetgo_setround = 0
readysetgo_currentround = 0
go = False

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create ReadySetGo Class
class ReadySetGo(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

# # # Event Listener: Bot on_ready - For when ReadySetGo has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('ReadySetGo has loaded')

# # # Event Listener: Bot on_message - For when a User does "!readysetgo", have that message deleted (so the channel doesn't get filled up)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "!readysetgo" and message.channel.name != "ready-set-go":
            await message.delete()
        elif message.content == "!dogo" and message.channel.name != "ready-set-go":
            await message.delete()

###############################################################################################################################################################################################################

#
# # Command section ############################################################################
#

# # # Command: !readysetgo ; When a User does !readysetgo in the ready-set-go channel, then the game: Ready Set Go starts EX: !readysetgo
    @commands.command(help = 'Play Ready Set Go (go to ready-set-go Channel first)', description = 'Has to be run in the Channel: ready-set-go')
    async def readysetgo(self, ctx:commands.Context):
        global readysetgo_running # start the game
        global readysetgo_finished
        global readysetgo_gotime
        global readysetgo_elapsedtime
        global readysetgo_setround
        global readysetgo_currentround
        global go

        # Makes sure !readysetgo can only be run in the right channel
        if ctx.channel.name != "ready-set-go": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!readysetgo** which is specific to the Channel: <#1172292919420538961> Please go there and try it")    
        
        elif ctx.channel.name == "ready-set-go": # the command was done in the correct Channel: ready-set-go
            
            # Player did !readysetgo but the Game has already started

            if readysetgo_running == True:
                await ctx.author.send("The game has already started, so **!readysetgo** won't do anything")
            
            else: # readysetgo has not been started already, so let it get started and run its logic
                readysetgo_running = True

                user = ctx.author
                channel = discord.utils.get(ctx.guild.channels, name = "ready-set-go")
                members = channel.members

                for user in members:
                    Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                    await user.add_roles(Players_role)
                    
                if readysetgo_currentround > int(readysetgo_setround):
                    Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                    Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")

                    if Winners_role is not None:              

                        if channel is not None and isinstance(channel, discord.TextChannel):
                            # Get a list of members with the target role in the specified channel
                            members_with_role = [member for member in channel.members if Winners_role in member.roles]

                            if members_with_role:
                                user_list = "\n".join([member.name for member in members_with_role]) # prints the list of users with the Winners role in the Channel: ready-set-go
                                print(f'Users with the role {Winners_role} in the channel {channel}:\n{user_list} are a Winner!!!')
                                await ctx.send(f'_ _ \nPlayers who have won a round in this match are: \n**{user_list}**\n')
                            else:
                                print(f'No users have the role {Winners_role} in the channel {channel}.')
                                await ctx.send(f'_ _ \nThere are no winners in this match')
                        else:
                            print(f'The channel {channel} does not exist or is not a text channel in this server.')
                    else:
                            print(f'The role {Winners_role} does not exist in this server.')
                    
                    if Eliminated_role is not None:              

                        if channel is not None and isinstance(channel, discord.TextChannel):
                            
                            members_with_role = [member for member in channel.members if Eliminated_role in member.roles] # gets a list of users with the Eliminated role in the Channel: ready-set-go

                            if members_with_role:
                                user_list = "\n".join([member.name for member in members_with_role]) # prints the list of users with the Eliminated role in the Channel: ready-set-go
                                print(f'Users with the role {Eliminated_role} in the channel {channel}:\n{user_list} are a Loser :(')
                                await ctx.send(f'_ _ \nPlayers who have been eliminated in this match are: \n**{user_list}**\n')
                            else:
                                print(f'No users have the role {Eliminated_role} in the channel {channel}.')
                                await ctx.send(f'_ _ \nNo one has been eliminated in this match')
                        else:
                            print(f'The channel {channel} does not exist or is not a text channel in this server.')
                    else:
                            print(f'The role {Eliminated_role} does not exist in this server.')

                    await user.remove_roles(Eliminated_role)
                    await user.remove_roles(Winners_role)
                    await ctx.send(f'_ _ \nThe game has concluded. Thank you for playing!')
                    readysetgo_running = False
                    readysetgo_setround = 0
                    return
                
                if readysetgo_currentround == 0:
                    for user in members:
                        Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")
                        await user.remove_roles(Eliminated_role)
                        Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                        await user.remove_roles(Winners_role)

                    def check(msg):
                        msg = msg.content
                        if [int(s) for s in msg.split() if s.isdigit()]:
                            return msg

                    try:
                        await ctx.reply("How many rounds would you like to play Ready, Set, Go?\n\n Please enter a number:")
                        msg = await ctx.bot.wait_for("message", check = check, timeout = 10)
                        readysetgo_setround = msg.content
                        print(readysetgo_currentround)
                        readysetgo_currentround += 1
                        await ctx.send(f"""We are going to do {readysetgo_setround} round(s).
                                        \nThe rules of this game are to say "!dogo" as soon as "go" appears. But, do not say "!dogo" before that, or else you'll be eliminated for the entire match. 
                                        \nWhen "go" appears but no one responds within 10 seconds, everyone will be eliminated.
                                        \n This is a game of focus and reflexes. Good luck and have fun!""")
                        
                    except asyncio.TimeoutError:
                        print(readysetgo_currentround)
                        await ctx.reply("\nSorry, you didn't reply in time! Do !readysetgo to try again")
                        readysetgo_running = False
                        return

                if (readysetgo_currentround > 0) and (readysetgo_currentround <= int(readysetgo_setround)):
                    await ctx.send(f'_ _ \n**Round {readysetgo_currentround} of {readysetgo_setround}**\n')
        
                    rhymes = ["Go", "Bo", "Ho", "Jo", "Lo", "Mo", "No", "Oh", "Po", "Wo", "So", "Yo", "Ago", "Azo", "Bio", "Bow", "Bro", "C.E.O.", "C.F.O.", "Doe", "Duo", "Eau", "Ego", 
                                "Emo", "Foe", "Flo", "Fro", "Geo", "Hoe", "Joe", "Low", "Mho", "Mow", "Poe", "Pro", "Quo", "Rho", "Rio", "Roe", "Row", "Sew", "Toe", "Tow", "U.F.O.", 
                                "Uno", "Aloe", "Ammo", "Beau", "Blow", "Camo", "Coco", "Crow", "Dado", "Dodo", "Ebro", "Ergo", "Faux", "Flow", "Glow", "Grow", "Gyro", "Know", "Hero", 
                                "Hobo", "Jojo", "Judo", "Juno", "Kayo", "Karo", "Keto", "Kilo", "Logo", "Ludo", "Oleo", "Pogo", "Mayo", "Milo", "Mojo", "Otto", "Peso", "Pico", "Reno", 
                                "Show", "Slow", "Snow", "Solo", "Stow", "Trio", "Typo"
                                ] # a list of messages the Bot spams out, with "Go" in it
                    await ctx.channel.send('_ _ \nReady')
                    await asyncio.sleep(1)
                    await ctx.channel.send('_ _ \nSet')
                    await asyncio.sleep(1)

                    go = False

                    while go == False:
                        send_rhyme = await ctx.channel.send(f'_ _ \n{random.choice(rhymes)}') # use _ _ to do a new line at the beginning of a message
                        send_rhyme # have to assign it as a variable in order to do .content.split() (I think, at least)
                        rhyme_sent = send_rhyme.content.split()[2] # I did '2' instead of '0' because '0' only outputs the '_' instead of the actual word
                        rhyme_sent_comparison = rhyme_sent[:2] # I did '2' to get only the first two characters of the string (since I want to compare them to "Go")
                        
                        await asyncio.sleep(.5) # delay the next message sendout
                        
                        # Bot sent a message that said "Go"
                        if rhyme_sent_comparison == "Go":
                            readysetgo_finished = True
                            go = True # stops the loop, which stops the Bot from spamming
                    
                    if go == True: # first check if every user in the channel is eliminated, if not, then ; wait 10 seconds, if no input given, then everyone gets eliminated
                        try:
                            Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")
                            
                            if Eliminated_role is not None:              

                                if channel is not None and isinstance(channel, discord.TextChannel):
                                    
                                    for member in channel.members:
                                        if Eliminated_role not in member.roles:

                                            print(f'There are players who are not eliminated, so someone should be able to do !dogo, so go ahead and start the timer')
                                            await asyncio.sleep(10)
                                            raise asyncio.TimeoutError
                                            #return
                                            #TimeoutError
                                            #raise Exception, asyncio.TimeoutError
                                            #await ctx.send("_ _ \nThis round is now over because no one responded in time 2")
                                            #channel = discord.utils.get(ctx.guild.channels, name = "ready-set-go")
                                            #members = channel.members
                                            #Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                                            #Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                                            
                                            #for user in members:
                                            #    await user.add_roles(Waiting_role)

                                            #readysetgo_currentround +=1
                                            #print(readysetgo_currentround)
                                            #readysetgo_finished = False
                                            #readysetgo_running = False

                                            #for user in members:
                                            #    await user.add_roles(Players_role)
                                            #    await user.remove_roles(Waiting_role)
                                            
                                            #readysetgo_restart = ctx.bot.get_command('readysetgo')
                                            #await readysetgo_restart(ctx)

                                            #return
                                    
                                    #print(f'All players have been eliminated')
                                    #message = await self.bot.wait_for("message", check = check, timeout = 10.0)
                                    #m = message.content

                                    # All users are eliminated
                                    #await ctx.send("All players have been eliminated, so this match is over")
                                    #Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                                    #Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                                    
                                    #for user in members:
                                    #    await user.add_roles(Waiting_role)

                                    #readysetgo_currentround = readysetgo_setround + 1
                                    #print(readysetgo_currentround)
                                    #readysetgo_finished = False
                                    #readysetgo_running = False

                                    #Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                                    #await ctx.message.author.add_roles(Winners_role)

                                    #for user in members:
                                    #    await user.add_roles(Players_role)
                                    #    await user.remove_roles(Waiting_role)
                                    
                                    #readysetgo_restart = ctx.bot.get_command('readysetgo')
                                    #await readysetgo_restart(ctx)

                        except asyncio.TimeoutError:
                            
                            await ctx.send("This match is now over because no one responded in time.")
                            channel = discord.utils.get(ctx.guild.channels, name = "ready-set-go")
                            members = channel.members
                            # So make all users, except for winners, eliminated
                            
                            # Now all users are eliminated, so go to scoreboard logic
                            await ctx.send("All players have been eliminated, so this match is over")
                            Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                            Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                            
                            for user in members:
                                await user.add_roles(Waiting_role)

                            readysetgo_currentround = readysetgo_setround + 1
                            print(readysetgo_currentround)
                            readysetgo_finished = False
                            readysetgo_running = False

                            Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                            await ctx.message.author.add_roles(Winners_role)

                            for user in members:
                                await user.add_roles(Players_role)
                                await user.remove_roles(Waiting_role)
                            
                            readysetgo_restart = ctx.bot.get_command('readysetgo')
                            await readysetgo_restart(ctx)
                        
                        else:
                            print(f'All players have been eliminated')
                            #message = await self.bot.wait_for("message", check = check, timeout = 10.0)
                            #m = message.content

                            # All users are eliminated
                            await ctx.send("All players have been eliminated, so this match is over")
                            Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                            Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                            
                            for user in members:
                                await user.add_roles(Waiting_role)

                            readysetgo_currentround = readysetgo_setround + 1
                            print(readysetgo_currentround)
                            readysetgo_finished = False
                            readysetgo_running = False

                            Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                            await ctx.message.author.add_roles(Winners_role)

                            for user in members:
                                await user.add_roles(Players_role)
                                await user.remove_roles(Waiting_role)
                            
                            readysetgo_restart = ctx.bot.get_command('readysetgo')
                            await readysetgo_restart(ctx)


# # # Command: !dogo ; Player does !dogo to say when he thinks he sees "Go" get sent by the Bot. EX: dogo!
    @commands.command(help = 'Do this command when "Go" appears to win. (If done before it appears, you lose)', description = 'Has to be run in the Channel: ready-set-go')
    async def dogo(self, ctx:commands.Context):
        global readysetgo_running
        global readysetgo_finished
        global readysetgo_gotime
        global readysetgo_elapsedtime
        global readysetgo_firsttogo
        global readysetgo_setround
        global readysetgo_currentround
        global go

        # Makes sure !dogo can only be run in the right channel 
        if ctx.channel.name != "ready-set-go": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!dogo** which is specific to the Channel: <#1172292919420538961> Please go there and try it")
        
        elif ctx.channel.name == "ready-set-go": # the command was done in the correct Channel: ready-set-go
            
            if readysetgo_running:
                user = ctx.author

                if readysetgo_finished == False:
                    Eliminated_role = discord.utils.get(ctx.guild.roles, name = "Eliminated")

                    for role in ctx.guild.roles:
                        if role.name == "Eliminated":
                            await ctx.reply(f'You were already eliminated')

                        elif role.name != "Eliminated":
                            await ctx.reply(f'You went too early ; now you are eliminated')
                            await user.add_roles(Eliminated_role)
                            Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                            await user.remove_roles(Players_role)
                            return

                if readysetgo_finished == True:
                    channel = discord.utils.get(ctx.guild.channels, name = "ready-set-go")
                    members = channel.members
                    Waiting_role = discord.utils.get(ctx.guild.roles, name = "Waiting")
                    Players_role = discord.utils.get(ctx.guild.roles, name = "Players")
                    
                    for user in members:
                        await user.add_roles(Waiting_role)

                    await ctx.reply(f'You were the fastest to say !dogo after "Go" appeared. Hooray, you have won this round!!\n')
                    readysetgo_currentround +=1
                    print(readysetgo_currentround)
                    readysetgo_finished = False
                    readysetgo_running = False

                    Winners_role = discord.utils.get(ctx.guild.roles, name = "Winners")
                    await ctx.message.author.add_roles(Winners_role)

                    for user in members:
                        await user.add_roles(Players_role)
                        await user.remove_roles(Waiting_role)
                    
                    readysetgo_restart = ctx.bot.get_command('readysetgo')
                    await readysetgo_restart(ctx)
                    
            else:
                # Player did !dogo but the Game hasn't started
                await ctx.author.send("Hold your horses, Ready Set Go hasn't started yet, so **!dogo** won't do anything. If you would like to play, do **!readysetgo** to start a game first")           

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(ReadySetGo(bot)) # name of the Class, look above