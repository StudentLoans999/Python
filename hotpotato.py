# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands
import asyncio
import random
from discord.ext import tasks

hotpotato_running = False
potato_holder = None  # variable to store the current holder of the potato
player_points = {}  # dictionary to store player points
last_caller = None  # variable to store the user who most recently called for the potato
loser = None

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create RPG Class
class Hot_Potato(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

# # # Event Listener: Bot on_ready - For when ER has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('HP has loaded')

 # # # Event Listener: Bot on_message - For when a User does !hotpotato or !throw or !call outside the right channel, have that message deleted (so the channel doesn't get filled up)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # ignore messages from bot
        
        if message.content == "!hotpotato" or message.content == "!throw" or message.content == "!call" and message.channel.name != "hot-potato":
            await message.delete()

#
# # Command section ############################################################################
#

# # # Command: !hotpotato ; Player does !hotpotato when he wants to play Hot Potato in the hot-potato channel. EX: !hotpotato
    @commands.hybrid_command(name='hotpotato', description = 'Play Hot Potato (go to hot-potato Channel first)')
    async def hotpotato(self, ctx):
        global hotpotato_running # start the game
        global potato_holder
        global loser

        # Makes sure !hotpotato can only be run in the right channel
        if ctx.channel.name != "hot-potato": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!hotpotato** which is specific to the Channel: <#1182767410781110323> Please go there and try it")    
        
        elif ctx.channel.name == "hot-potato": # the command was done in the correct Channel: hot-potato

            if hotpotato_running == True: # player did !hotpotato but the Game has already started
                await ctx.author.send("A **Hot Potato** game has already started, so **!hotpotato** won't do anything. Please go to the Channel: <#1182767410781110323>")
            
            else: # hotpotato has not been started already, so let it get started and run its logic

                hotpotato_running = True # start the game

                channel = discord.utils.get(ctx.guild.channels, name = "hot-potato") # makes sure it only looks for users in the Channel: hot-potato
                members = channel.members

                members_online = [member for member in channel.members if member.status == discord.Status.online and member.name != "Heart-to-Heart Bot"] # online users (excluding bot)

# # Start game section ############################################################################

                potato_holder = random.choice(members_online) # gives the potato to a random player

                if potato_holder.id not in player_points: # add the potato holder to player_points if not present
                    player_points[potato_holder.id] = 0  

                await ctx.send(f"""_ _ \nA **Hot Potato** game has been started. 
                                        \nI have thrown the hot potato to **{potato_holder.mention}**. 
                                        \nIf you have the potato, do **!throw** to throw the potato to someone else.
                                        \nYou will earn **10 points** for each second you hold the potato.
                                        \nDon't do **!throw**, if you don't have the potato or else you'll be docked **100 points**!
                                        \nIf you don't have the potato, do **!call** to ask to receive the potato.
                                        \nWhoever does **!call** last (right before the potato holder does **!throw**), will receive the potato from the potato holder. 
                                        \nDon't do **!call**, if you do have the potato or else you'll be docked **100 points**!
                                        \nWhoever is left holding the potato when it explodes is the loser. The survivors' points will be displayed afterward""")
                                
                @tasks.loop(seconds=1)  # run the task every second
                async def potato_holder_getpoints():

                    if potato_holder and potato_holder.id in player_points: # gives the potato holder points for each second spent holding the potato

                        player_points[potato_holder.id] += 10
                        #print(f'**{potato_holder.name}** now has **{player_points[potato_holder.id]} points**')
                    
                    else:
                        print()

                @potato_holder_getpoints.before_loop # wait for the bot to be ready before starting the add points loop
                async def before_potato_holder_getpoints():
                    await ctx.bot.wait_until_ready()  

                async def display_scoreboard(ctx, loser): # shows the exploded player, the winner, and everyone's points (except the exploded player's)
                    global potato_holder, hotpotato_running, player_points

                    if player_points: # at least one person earned points

                        scoreboard = "_ _ \n**Scoreboard:**\n"

                        player_points_copy = dict(player_points) # create a copy of player_points for iteration

                        sorted_players = sorted(player_points_copy.items(), key=lambda x: x[1], reverse=True) # sorts the list of the player's points in descending order

                        for player_id, points in player_points_copy.items(): # lists each player with their points

                            player = ctx.guild.get_member(player_id)

                            if player:

                                if str(player) == loser: # the player who held the potato when it exploded
                                    scoreboard += f"_ _ \n**{player.display_name}**: **Exploded**!\n\n"

                                else: # non-loser
                                    scoreboard += f"_ _ \n**{player.display_name}**: **{points}** points\n\n"

                        # List out the winner from the list of players
                        if sorted_players:

                            winner_id, winner_points = sorted_players[0] # first player in the index (highest score, since sorted_players is in descending order up above)
                            winner = ctx.guild.get_member(winner_id)

                            if winner: # there is a winner
                                
                                if winner_points != 0: # not the exploded player (who has 0 points) nor anyone who didn't hold the potato at all
                                    scoreboard += f"_ _ \nSo the **Winner** is: **{winner.display_name}** with **{winner_points}** points!\n\n"

                        await ctx.send(scoreboard) # send out the scoreboard

                    else: # no one earned points
                        await ctx.send("No points recorded yet")

                    # Reset global variables (end of match)
                    potato_holder = None
                    hotpotato_running = False
                    player_points.clear()  # clear player points after displaying scoreboard

                # Generate a random timer between 5 and 30 seconds
                bomb_timer = random.uniform(5, 30)
                await ctx.send("Now starting a timer for the potato explosion; sometime between **5-30** seconds")
                potato_holder_getpoints.start() # start the earn points loop that runs every second

                await asyncio.sleep(bomb_timer)# potato explodes when random timer goes off
                potato_holder_getpoints.stop() # stop earning points loop

                if potato_holder: # potato explodes, making the person holding it the loser and setting their points to 0, and then doing scoreboard logic

                    loser = potato_holder.name
                    await ctx.send(f'_ _ \nBOOM!!!!! \n\n**{loser}** was holding the potato and lost the game')
                    
                    loser_id = ctx.guild.get_member_named(loser).id
                    player_points[loser_id] = 0
                    await display_scoreboard(ctx, loser)

############################################################################

# # # Command: !call ; Player does !call when he wants to get the Hot Potato in the hot-potato channel. EX: !call
    @commands.hybrid_command(name='call', description = 'Call for the Hot Potato to possibly receive it')
    async def call(self, ctx):
        global hotpotato_running, potato_holder, last_caller

        # Makes sure !call can only be run in the right channel 
        if ctx.channel.name != "hot-potato": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!call** which is specific to the Channel: <#1182767410781110323> Please go there and try it")

        elif ctx.channel.name == "hot-potato": # the command was done in the correct Channel: hot-potato

            if not hotpotato_running: # if the game is not running
                await ctx.send("Hold your horses, Hot Potato hasn't started yet, so **!call** won't do anything. If you would like to play, do **!hotpotato** to start a game first")

                return

        if ctx.author == potato_holder: # the person calling is the current potato_holder

            await ctx.send(f"**{potato_holder.mention}** you already have the potato! You're now docked **100 points** for not paying attention")
            player_points[potato_holder.id] -= 100

            return

        if potato_holder and ctx.author.id != potato_holder.id: # called for the potato and isn't holding potato
        
            last_caller = ctx.author # update the last caller
            await ctx.send(f"**{ctx.author}** has called for the potato")
            print(last_caller)

            # Check if the current potato holder exists and is not the one who called
            if potato_holder.id in player_points and potato_holder.id != last_caller.id:
                await ctx.send(f"The potato will be passed to **{last_caller.mention}** after the next throw.")
            else:
                await ctx.send(f"There is no potato holder or the current holder called. The potato will be thrown randomly after the next call.")

############################################################################

# # # Command: !throw ; Player does !throw when he wants to throw the Hot Potato in the hot-potato channel. EX: !throw
    @commands.hybrid_command(name='throw', description = 'Throw the Hot Potato to the person who last did !call')
    async def throw(self, ctx):
        global hotpotato_running, potato_holder, last_caller

        # Makes sure !throw can only be run in the right channel 
        if ctx.channel.name != "hot-potato": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!throw** which is specific to the Channel: <#1182767410781110323> Please go there and try it")

        elif ctx.channel.name == "hot-potato": # the command was done in the correct Channel: hot-potato

            if not hotpotato_running: # if the game is not running

                await ctx.send("Hold your horses, Hot Potato hasn't started yet, so **!throw** won't do anything. If you would like to play, do **!hotpotato** to start a game first")

                return

            if last_caller is not None: # someone called for the potato

                if ctx.author.id != potato_holder.id: # check if the person who did !throw is not the potato holder
                    
                    if ctx.author != potato_holder: # if player is not the current potato_holder

                        await ctx.send(f"**{ctx.author.mention}** you don't have the potato to throw! You're now docked **100 points** for not paying attention")
                        player_points[ctx.author.id] -= 100 # decrease the player's points
                        return
                    
                elif ctx.author.id == potato_holder.id: # player is holding the potato

                    potato_holder = last_caller # throw the potato to the person who last called for it

                    if potato_holder.id not in player_points: # if player never held potato, add them to the dictionary and set their starting points to 0 
                        player_points[potato_holder.id] = 0

                await ctx.send(f'**{potato_holder.mention}** caught the potato! They now have the potato')

                last_caller = None  # reset last_caller after throwing the potato

            else: # no one called for the potato

                if ctx.author == potato_holder: # throw the potato if currently holding the potato

                    channel = discord.utils.get(ctx.guild.channels, name = "hot-potato") # makes sure it only looks for users in the Channel: hot-potato
                    members = channel.members
                    members_online = [member for member in channel.members if member.status == discord.Status.online and member.name != "Heart-to-Heart Bot"] # online users (excluding bot)

                    potato_holder = random.choice(members_online) # gives the potato to a random player
                    await ctx.send(f"No one has called for the potato yet, so will throw the potato to a random player. **{potato_holder.mention}** now has the potato!")

                    if potato_holder.id not in player_points: # if player never held potato, add them to the dictionary and set their starting points to 0 
                        player_points[potato_holder.id] = 0

                    return
            
                else: # doesn't have the potato, so can't throw it

                    await ctx.send(f"**{ctx.author.mention}** you don't have the potato to throw! You're now docked **100 points** for not paying attention")
                    
                    if ctx.author.id not in player_points: # if player never held potato, add them to the dictionary and set their starting points to 0 
                        player_points[ctx.author.id] = 0

                    player_points[ctx.author.id] -= 100 # decreases the player's points

                    return

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(Hot_Potato(bot)) # name of the Class, look above