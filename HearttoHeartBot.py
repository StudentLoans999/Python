#
# # Imports and Setup section ############################################################################
#

# Import discord.py which allows access to Discord's API
from typing import Any
import discord

#import sys
#print(sys.path)

import random
import asyncio
import time
import datetime
import os # needed for Cogs
from discord.flags import Intents

# Import load_dotenv function from dotenv module
from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script
load_dotenv()

# Grab the API Token from the .env file
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Gets the Client object from discord.py. Client is synonymous with Bot
from discord.ext import commands, tasks

# Gets Class from discord.py
from discord import app_commands

import tracemalloc
tracemalloc.start()

# These are needed in order for the Bot to work properly
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents = intents, help_command=None) # makes "!" be the character that Users use to run a Command

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Event Listener: Bot on_ready - For when the Bot has first been turned On ############################################################################
@bot.event # has to be done before the ##Cogs section## below in order for this syntax to work
async def on_ready():

    guild_count = 0 # creates a Counter to keep track of how many Guilds/Servers the Bot is connected to

    # Loops through all the Guilds/Servers that the Bot is associated with and Prints the Server's ID and Name
    for guild in bot.guilds:
        print(f"The server id is '{guild.id}' and the server name is '{guild.name}'")

        # Increments the Guild Counter
        guild_count = guild_count + 1

    print(f"'{bot.user}' is now online and in " + str(guild_count) + " server(s)") # prints how many Guilds/Servers the Bot is in

# # # Event Listener: Bot on_message - For when a User sends a message to the Server ############################################################################
@bot.event
async def on_message(message):

    # We do not want the Bot to reply to itself and potentially cause a recursive case where the Bot sends a message over and over to itself
    if message.author.id == bot.user.id:
            return
    
    # Checks if any User said a [greeting] in any Channel and then the Bot sends back a message to that same Channel, naming the person who said the [greeting]
    greetings = ["hello", "hi", "hey", "hiya", "wassup", "sup", "yo", "salutations", "howdy", "good morning", "good afternoon", "good evening"]
    if any(word in message.content.lower() == word for word in greetings): # do it this way so that it doesn't react to words like "tHELLO". Used to be: any(word in message.content.lower() for word in greetings):
        await message.channel.send("Hello there, " + str(message.author))
        print("Bot's Reply to [greetings] has been executed")

    # Prints the User, their Message, and which Channel they posted in
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f"'{username}' said '{user_message}' in the channel '{channel}'")

    await bot.process_commands(message) # This lets extra @commands.command to work/trigger - very important to have in the first event!!!!!

# # # Event Listener - For when a new User joins the Server, the Bot will send them a DM, and also a message in the Channel they entered ############################################################################
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Heart-to-Heart server! My name is {bot.user}. Please let me know if you need anything! Do **!help** if you want to know how to do something')
    channel = await bot.fetch_channel(1173673669579510003) 
    await channel.send(f'{member.mention}, welcome to my server') # When a new User joins the Server, mention them specifically with a message in the Channel: welcome

# # # Event Listener - When a User leaves the Server, mention them specifically with a message in the Channel they are in ############################################################################
@bot.event
async def on_member_remove(member):
    channel = await bot.fetch_channel(1173673669579510003)
    await channel.send(f'Goodbye {member.mention}')

# # # Event Listener - Changes the Bot's Presence to be Listening to a specific User when that User starts Typing, and then changes the Bot's Presence back to nothing (not Listening) ############################################################################
@bot.event
async def on_typing(channel, user, when):

    if isinstance(channel, discord.DMChannel): # handle DM channels differently, as they don't have a 'name' attribute
        print(user.name + " is typing in a DM" + " at", when)
        await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = user.name))
        await asyncio.sleep(1) # this delay is so that Users can actually see the changed display of the Presence, instead of it changing back to "normal" instantly
        await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.custom)) # changes Presence back to "normal"

    else:# non-DM channel, so it does have a 'name' attribute
        print(user.name + " is typing in", channel.name + " at", when) # prints the user's name and the channel they're typing in, and at what time
        await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = user.name))
        await asyncio.sleep(1) # this delay is so that Users can actually see the changed display of the Presence, instead of it changing back to "normal" instantly
        await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.custom)) # changes Presence back to "normal"

###############################################################################################################################################################################################################

#
# # Cogs section ############################################################################
#

# # # Command: !reload ; 
@bot.command(help = 'MOD: Adds in a new Cog', description = 'Adds in more functionality (Commands and Event Listeners)')
@commands.has_role('Moderator')
async def reload(ctx, extension = commands.parameter(default = None, description = '- Put in the name of the Class you want loaded')):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Bot has unloaded a Cog: {extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Bot has loaded in a Cog: {extension}')

# # # When the Bot turns On, it checks for all the .py files in the cogs folder, then loads them as a cog
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        async def main():
            await bot.load_extension(f'cogs.{filename[:-3]}') # strips the .py ending of the filename
        if __name__ == '__main__':
            asyncio.get_event_loop().run_until_complete(main())

###############################################################################################################################################################################################################

# Executes the Bot with the specified Token. Token has been removed and used just as an example
bot.run(os.environ.get('DISCORD_TOKEN'))