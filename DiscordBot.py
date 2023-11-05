# Import discord.py which allows access to Discord's API
import discord

# Import random
import random

# Import the os module
import os

# Import load_dotenv function from dotenv module
from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script
load_dotenv()

# Grab the API Token from the .env file
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Gets the Client object from discord.py. Client is synonymous with Bot
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Event Listener for when the bot has been turned On
@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

    # Creates a Counter to keep track of how many Guilds/Servers the Bot is connected to
    guild_count = 0

    # Loops through all the Guilds/Servers that the Bot is associated with and Prints the Server's ID and Name
    for guild in bot.guilds:
        print(f"The server id is '{guild.id}' and the name is '{guild.name}'")

        # Increments the Guild Counter
        guild_count = guild_count + 1

    # Prints how many Guilds/Servers the Bot is in
    print(f"'{bot.user}' is in " + str(guild_count) + " server(s)")

# Event Listener for when a new message is sent to a channel
@bot.event
async def on_message(message):

    # We do not want the bot to reply to itself and potentially cause a recursive case where the bot sends a message over and over to itself
    if message.author.id == bot.user.id:
            return
    
    # Checks if a user said something specific in the Server and then Sends back a message to the Server
    if message.content == "hello":
        await message.channel.send("hey!")

    # Checks if a user said something in the Server that StartsWith something and then Sends back a message to the Server
    if message.content.startswith("q"):
        await message.channel.send("HELLO!")

    # Prints the User, their Message, and which Channel they posted in
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f"'{username}' said '{user_message}' in the channel '{channel}'")

    # This lets extra @bot.command to work/trigger
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to the Airport Discord server!')

# When a User says !dm in the Server, the Bot will DM him
@bot.command()
async def dm(ctx):
  await ctx.message.author.send(f'hi my name is {bot.user} and i am a bot!')

# When a User says !cost, the Bot will randomly output to the Channel one of the listed values
@bot.command(name='cost')
async def training_program_costs(ctx):
    costs = [
        '$100',
        '$999',
        '$333',
        '$666',
    ]

    response = random.choice(costs)
    await ctx.send(response)

@bot.command(name='99', help='Responds with a random Brooklyn 99 quote')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

# Executes the Bot with the specified Token. Token has been removed and used just as an example
#bot.run("DISCORD_TOKEN")
#print(DISCORD_TOKEN)
#print(os.environ.get('DISCORD_TOKEN'))
bot.run(os.environ.get('DISCORD_TOKEN'))