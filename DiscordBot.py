# # Setup section ############################################################################

# Import discord.py which allows access to Discord's API
from typing import Any
import discord

import random
import asyncio
import time
import datetime
import os
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

# These are needed in order for the Bot to work properly
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) # makes "!" be the character that Users use to run a Command

###############################################################################################################################################################################################################

# # Views & Buttons section ############################################################################

# Create test View Class
class test(discord.ui.View):
  # View has a timeout of 180 seconds (3 minutes)
  def __init__(self) -> None:
      super().__init__(timeout=1) # specify the timeout here

# You can add up to 25 buttons to the same view, but make sure its custom_id and function name are always different

  # First button - Just an Emoji, default color
  @discord.ui.button(custom_id = "emoji_button", emoji= '\U0001F606')
  async def say_hello(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f'Hello!')

  # Second button - Label 'greet', green, no emoji
  @discord.ui.button(label='greet', custom_id = "greet_button", style = discord.ButtonStyle.blurple)
  async def greet_user(self, interaction: discord.Interaction, button: discord.ui.Button):
    user = interaction.user.id
    await interaction.response.send_message(f'Hello, <@{user}>, how are you doing today?')

  # Third button - Label 'say goodbye', red, has emoji
  @discord.ui.button(label='say goodbye', custom_id = "good_bye_button", emoji = '\U0001F601', style = discord.ButtonStyle.red)
  async def say_goodbye_to_user(self, interaction: discord.Interaction, button: discord.ui.Button):
    user = interaction.user.id
    await interaction.response.send_message(f'Good bye, <@{user}>, hope to see you soon!')

# Create greet_view View Class
class greet_view(discord.ui.View):
  def __init__(self):
      super().__init__(timeout=None) # specify the timeout here

  # First button - Just an Emoji, default color
  @discord.ui.button(custom_id = "emoji_button", emoji= '\U0001F606')
  async def say_hello(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f'Hello!')

  # Second button - Label 'greet', green, no emoji
  @discord.ui.button(label='greet', custom_id = "greet_button", style = discord.ButtonStyle.blurple)
  async def greet_user(self, interaction: discord.Interaction, button: discord.ui.Button):
    user = interaction.user.id
    await interaction.response.send_message(f'Hello, <@{user}>, how are you doing today?')

  # Third button - Label 'say goodbye', red, has emoji
  @discord.ui.button(label='say goodbye', custom_id = "good_bye_button", emoji = '\U0001F601', style = discord.ButtonStyle.red)
  async def say_goodbye_to_user(self, interaction: discord.Interaction, button: discord.ui.Button):
    user = interaction.user.id
    await interaction.response.send_message(f'Good bye, <@{user}>, hope to see you soon!')

###############################################################################################################################################################################################################

# # Event Listeners section ############################################################################

##
# Event Listener - For when the Bot has first been turned On
##

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

    guild_count = 0 # creates a Counter to keep track of how many Guilds/Servers the Bot is connected to

    # Loops through all the Guilds/Servers that the Bot is associated with and Prints the Server's ID and Name
    for guild in bot.guilds:
        print(f"The server id is '{guild.id}' and the server name is '{guild.name}'")

        # Increments the Guild Counter
        guild_count = guild_count + 1

    print(f"'{bot.user}' is in " + str(guild_count) + " server(s)") # prints how many Guilds/Servers the Bot is in
    
##
# Event Listener - For when any new User sends a message to the Server
##

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

    await bot.process_commands(message) # This lets extra @bot.command to work/trigger - very important to have in the first event!!!!!

##
# Event Listener - For when a new User joins the Server
##

@bot.event
async def on_member_join(member):
    # When a new User joins the server, the Bot will send them a DM
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to the ChatBot Discord server! My name is {bot.user}. Please let me know if you need anything! Do !help if you want to know how to do something')

    # When a new User joins the Server, mention them specifically with a message in the Channel they are in
    await member.guild.system_channel.send(f'{member.mention}, welcome to my server')

##
# Event Listener - When a User leaves the Server, mention them specifically with a message in the Channel they are in
##

@bot.event
async def on_member_remove(member):
    await member.guild.system_channel.send(f'Goodbye {member.mention}')

##
# Event Listener - Changes the Bot's Presence to be Listening to a specific User when that User starts Typing, and then changes the Bot's Presence back to nothing (not Listening)
##

@bot.event
async def on_typing(channel, user, when):
    print(user.name + " is typing in", channel.name + " at", when)
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name=user.name))
    await asyncio.sleep(1) # this delay is so that Users can actually see the changed display of the Presence, instead of it changing back to normal instantly, that the code below does
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.custom))

###############################################################################################################################################################################################################

# # Commands section ############################################################################

##
# # # Buttons section
##

# View trigger: When a User does !botbutton1 in the " " Channel, it makes the Bot show: View 1 Buttons with Text added. EX: !botbutton1
@bot.command(help='Get some interactive buttons', description='The Bot will show you some interactive buttons')
async def botbutton1(ctx):
    await ctx.channel.send("Hi! What you would like me to do?",view=test())
    return

# View trigger: User does !botbutton2 in the " " Channel, it makes the Bot show: View 2 Buttons with Text added. EX: !botbutton2
@bot.command(help='Get some other interactive buttons', description='The Bot will show you some other interactive buttons')
async def botbutton2(ctx):
    await ctx.channel.send("Hi! What you would like me to do?",view=greet_view())
    return

##
# # # Ready Set Go game section
##

readysetgo_running = False
readysetgo_finished = False
readysetgo_gotime = 0
readysetgo_elapsedtime = 0
readysetgo_firsttogo = 0
readysetgo_setround = 0
readysetgo_currentround = 0

@bot.command(help='Play Ready Set Go (go to ready-set-go Channel first)', description='Has to be run in the Channel: ready-set-go')
async def readysetgo(ctx:commands.Context):
    global readysetgo_running # start the game
    global readysetgo_finished
    global readysetgo_gotime
    global readysetgo_elapsedtime
    global readysetgo_setround
    global readysetgo_currentround

    # Makes sure !readysetgo can only be run in the right channel
    if ctx.channel.name != "ready-set-go": # has to be ctx.channel.name (not ctx.channel)
        await ctx.reply(f"It looks like you have tried to do the command: **!readysetgo** which is specific to the Channel: <#1172292919420538961> Please go there and try it")    
    
    elif ctx.channel.name == "ready-set-go": # the command was done in the correct Channel: ready-set-go
        
        # Player did !readysetgo but the Game has already started

        if readysetgo_running == True:
            await ctx.reply("The game has already started, so **!readysetgo** won't do anything")
        
        else: # readysetgo has not been started already, so let it get started and run its logic
            readysetgo_running = True

            user = ctx.author
            channel = discord.utils.get(ctx.guild.channels, name="ready-set-go")
            members = channel.members
            for user in members:
                Players_role = discord.utils.get(ctx.guild.roles, name="Players")
                await user.add_roles(Players_role)
                  
            if readysetgo_currentround > int(readysetgo_setround):
                for role in ctx.guild.roles:
                    if role.name == "Winners":
                        print("Chichekn") 

                    elif role.name == "Eliminated":
                        print("Dinner") 

                Winners_role = discord.utils.get(ctx.guild.roles, name="Winners")
                Eliminated_role = discord.utils.get(ctx.guild.roles, name="Eliminated")
                
                await ctx.send(f'Winner(s):  \n Loser(s): ')
                await user.remove_roles(Eliminated_role)
                await user.remove_roles(Winners_role)
                exit

                await ctx.send(f'The game has concluded. Thank you for playing!')
                

            if readysetgo_currentround == 0:
                for user in members:
                    Eliminated_role = discord.utils.get(ctx.guild.roles, name="Eliminated")
                    await user.remove_roles(Eliminated_role)

                def check(msg):
                    msg = msg.content
                    if [int(s) for s in msg.split() if s.isdigit()]:
                        return msg

                try:
                    await ctx.reply("How many rounds would you like to play Ready, Set, Go?\n\n Please enter a number:")
                    msg = await bot.wait_for("message", check=check, timeout=10)
                    readysetgo_setround = msg.content
                    print(readysetgo_currentround)
                    readysetgo_currentround += 1
                    await ctx.send(f'We are going to do {readysetgo_setround} round(s)')
                    
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

                Go = False

                while Go == False:
                    send_rhyme = await ctx.channel.send(f'_ _ \n{random.choice(rhymes)}') # use _ _ to do a new line at the beginning of a message
                    send_rhyme # have to assign it as a variable in order to do .content.split() (I think, at least)
                    rhyme_sent = send_rhyme.content.split()[2] # I did '2' instead of '0' because '0' only output the '_' instead of the actual word
                    rhyme_sent_comparison = rhyme_sent[:2] # I did '2' to get only the first two characters of the string (since I want to compare them to "Go")
                    
                    await asyncio.sleep(.5) # delay the next message sendout
                    
                    # Bot sent a message that said "Go"
                    if rhyme_sent_comparison == "Go":
                        readysetgo_finished = True
                        Go = True # stops the loop, which stops the Bot from spamming

# Player does !dogo to say when he thinks he sees "Go" get sent by the Bot. EX: dogo!
@bot.command(help='Do this command when "Go" appears to win. (If done before it appears, you lose)', description='Has to be run in the Channel: ready-set-go')
async def dogo(ctx:commands.Context):
    global readysetgo_running
    global readysetgo_finished
    global readysetgo_gotime
    global readysetgo_elapsedtime
    global readysetgo_firsttogo
    global readysetgo_setround
    global readysetgo_currentround

    # Makes sure !dogo can only be run in the right channel 
    if ctx.channel.name != "ready-set-go": # has to be ctx.channel.name (not ctx.channel)
        await ctx.reply(f"It looks like you have tried to do the command: **!dogo** which is specific to the Channel: <#1172292919420538961> Please go there and try it")
    
    elif ctx.channel.name == "ready-set-go": # the command was done in the correct Channel: ready-set-go
        
        if readysetgo_running:
            user = ctx.author

            if readysetgo_finished == False:
                Eliminated_role = discord.utils.get(ctx.guild.roles, name="Eliminated")

                for role in ctx.guild.roles:
                    if role.name == "Eliminated":
                        await ctx.reply(f'You were already eliminated')

                    elif role.name != "Eliminated":
                        await ctx.reply(f'You went too early ; now you are eliminated')
                        await user.add_roles(Eliminated_role)
                        Players_role = discord.utils.get(ctx.guild.roles, name="Players")
                        await user.remove_roles(Players_role)

            if readysetgo_finished == True:
                channel = discord.utils.get(ctx.guild.channels, name="ready-set-go")
                members = channel.members
                Waiting_role = discord.utils.get(ctx.guild.roles, name="Waiting")
                Players_role = discord.utils.get(ctx.guild.roles, name="Players")
                
                for user in members:
                    await user.add_roles(Waiting_role)

                await ctx.reply(f'You were the fastest to say !dogo after "Go" appeared. Hooray, you have won this round!!')
                readysetgo_currentround +=1
                print(readysetgo_currentround)
                readysetgo_finished = False
                readysetgo_running = False

                Winners_role = discord.utils.get(ctx.guild.roles, name="Winners")
                await user.add_roles(Winners_role)

                for user in members:
                    await user.add_roles(Players_role)
                    await user.remove_roles(Waiting_role)
                
                readysetgo_restart = bot.get_command('readysetgo')
                await readysetgo_restart(ctx)
                
        else:
            # Player did !dogo but the Game hasn't started
            await ctx.reply("Hold your horses, the game hasn't started yet, so **!dogo** won't do anything. If you would like to play, do **!readysetgo** to start a game first")           

##
# # # Moderator section
##

# Allows the Moderator Role to mute a specified User by doing !mute User EX: !mute cool-man-stu EX: !mute @CoolManStu
@bot.command(help='MOD: Mute a specified user', description='The user will be muted. You can unmute them with !unmute')
@commands.has_role('Moderator')
async def mute(ctx, member : discord.Member = commands.parameter(default= None, description="- Type in a user")):
    await member.edit(mute=True)
    await member.send("You have been muted by the Moderator")

# Allows the Moderator Role to unmute a specified User by doing !unmute User EX: !unmute cool-man-stu EX: !unmute @CoolManStu
@bot.command(help='MOD: Unmute a specified user', description='The user will be unmuted. You can mute them with !mute')
@commands.has_role('Moderator')
async def unmute(ctx, member : discord.Member = commands.parameter(default= None, description="- Type in a user")):
    await member.edit(mute=False)
    await member.send("You have been unmuted by the Moderator")

# Allows the Moderator Role to delete messages in a Channel by doing !clear #OfMessagesToDelete EX: !clear 3
@bot.command(name="clear", help='MOD: Delete a specified number of messages from the current channel', description='The Bot will delete the number of messages you tell it to')
@commands.has_role('Moderator')
async def clear(ctx, number:int = commands.parameter(default= 1, description="- Type in a number")):
    channel = ctx.channel
    if number > 1000:
        number = 101
    await channel.purge(limit=number+1)
    await ctx.send(f"Deleted the last {number} message(s) in this channels")

# Allows the Moderator Role to Kick Users in a Server by doing !kickuser, has to mention the user. EX: !kickuser @CoolManStu
@bot.command(help='MOD: Kick a specified user from the server', description='MOD: The Bot will kick the user you tell it to')
@commands.has_role('Moderator')
async def kickuser(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

# Allows the Moderator Role to Ban Users in a Server by doing !banuser, has to mention the user. EX: !banuser @CoolManStu
@bot.command()
@commands.has_role('Moderator')
async def banuser(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

# Allows the Moderator Role to Un-Ban Users in a Server by doing !unbanuser, has to mention the user. EX: !unbanuser @CoolManStu
@bot.command()
@commands.has_role('Moderator')
async def unbanuser(ctx, *, member):
    obj = await commands.UserConverter().convert(ctx, member)
    if obj is None:
        id_ = await commands.IDConverter().convert(str(member))
        if id_ is not None:
            try:
                obj = await bot.fetch_user(int(id_.group(1)))
            except discord.NotFound:
                obj = None
        if obj is None:
            await ctx.send('User not found')
            return 
    await ctx.guild.unban(obj)
    await ctx.send(f'Unbanned {obj}')

##
# # # User section
##

# When a User does !dm in the Server, the Bot will DM him
@bot.command(help='Get a DM from the Bot', description='The Bot will DM you a set message')
async def dm(ctx):
  await ctx.message.author.send(f'hi my name is {bot.user} and I am a bot!')

# When a User does !ping in the Channel, the Bot will reply to them in the same Channel: "pong!" with the latency outputted
@bot.command(help='Check your latency', description='The Bot will reply to you with your latency')
async def ping(ctx):
    await ctx.reply(f"pong! {round(bot.latency * 1000)}ms")

# When a User does !eightball + a Question (any text), the Bot will respond with a message in the same Channel. 
# It would contain the Question asked along with a random quote chosen from 'responses'
@bot.command(aliases=['8ball'], help='Ask the 8 Ball a Yes or No question', description='Do "!eightball Ask a Yes or No Question here" \nEX: !8ball Am I going to win the lottery')
async def eightball(ctx, *, question = commands.parameter(default= None, description="- Type in a Yes or No question to ask")):
    responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
                 "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", 
                 "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"
                ] # a list of possible answers the Bot gives to the question the User asked the 8ball
    response_to_none = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
                           "Yes", "Signs point to yes"
                        ] # a list of possible answers the Bot gives to the User when they didn't ask a question
    
    # User only did !eightball and did not ask a question, so the Bot offers them a helpful message
    if question == None:
        await ctx.send(f':8ball: **Question**: Do I need to try "**!help eightball**" to understand how to use the command properly?:8ball:\n:8ball: **Answer**: {random.choice(response_to_none)}:8ball:')
    
    # User asked a Question after doing !eightball
    else:
        await ctx.send(f':8ball: **Question**: {question}:8ball:\n:8ball: **Answer**: {random.choice(responses)}:8ball:')

# User does !embed and gets to create and post their own Embed (link with additional info) EX: !embed
@bot.command(help='Create an embedded link (with optional additional info)', description='The Bot will guide you in how to create an embedded link')
async def embed(ctx, member:discord.Member = None):
    if member == None:
        member = ctx.author

    name = member.display_name # the name of the User who did this command
    pfp = member.display_avatar # the avatar of the User who did this command

    embed = discord.Embed(title="This is my embed", description="It is a very cool embed", color=discord.Color.random())
    embed.set_author(name=f"{name}", url="https://www.youtube.com/watch?v=urLZoyLUDdE&list=PLW9I0hYEya07AHzGNHh470BODgNae8RPh&index=4", icon_url=f"{pfp}")
    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    embed.add_field(name="This is 1 field", value="Description of field 1")
    embed.add_field(name="This is 2 field", value="This field is inline True", inline=True)
    embed.add_field(name="This is 2 field", value="This field is inline True", inline=True)
    embed.set_footer(text=f"{name} Made this Embed")

    await ctx.send(embed=embed) # Bot sends a message

# User does !generate and then in the same Channel, the Bot @s them in a message that asks them a predefined Question and provides predefined Answers.
# Then the Bot waits for anyone to respond with !predefinedAnswerChoice and then the Bot sends a message to that same Channel
@bot.command(help='Create a question with answer choices (and responses to them)', description='The Bot will guide you in how to create a question with answers for people to choose from')
async def generate(ctx):
    options = ["a", "b", "c", "d"]
    await ctx.send(
        f"{ctx.author.mention}\n"
        f'\n **Question**: What does 1 + 1 equal? \n\n(**Important**: Type a "." in front of your answer choice. EX: !C )\n```'
        " A - 2\n B - Z\n C - Window\n D - 42```"
    )
    def check(m):
        return (
            m.content.startswith(".")
            and m.content.lower()[1:] in options
            and m.channel.id == ctx.channel.id
        )
    while True:
        msg = await bot.wait_for("message", check=check)
        if msg.content[1:] == 'A':
            await ctx.send(f"A SUCCESS")
        elif msg.content[1:] == 'B':
            await ctx.send(f"B SUCCESS")
        elif msg.content[1:] == 'C':
            await ctx.send(f"C SUCCESS")
        elif msg.content[1:] == 'D':
            await ctx.send(f"D SUCCESS")
        else:
            await ctx.send(f"FAILURE")

#@bot.command(description='Bot sends a message every hour', period='Period of the day')
#async def hourlymessage():
#    if period.name == 1:


# Holidays - Bot changes Status and Sends a Custom Holiday message throughout the Server
# Happy Birthday - Bot Sends a Custom Birthday message to the user throughout the Server
# Random interesting Fact
# Checklist - A user could type something like !checklist create <checklistname> then !checklist <checklistname> add “Implement a verification system” or whatever they want to add. Likewise they could delete, check off, and edit entries


# Rolls two six-sided dice and shows each Outcome and then adds them together and the Bot sends the Total Result to the Channel EX: !roll2
@bot.command()
async def roll2(ctx):
    roll1 = 0
    roll2 = 0
    total = 0
    for a in range(1):
        roll1 += random.randint(1, 6)
        await ctx.send(f'First Roll is {roll1}')
    for b in range(1):   
        roll2 += random.randint(1, 6)
        await ctx.send(f'Second Roll is {roll2}')
    for c in range(1):
        total += roll1 + roll2
        await ctx.send(f'{roll1} + {roll2} = **{total}**')

# Rolls two six-sided dice and the Bot sends the Total Result to the Channel EX: !ezroll
@bot.command()
async def ezroll(ctx):
    total = 0
    for i in range(2):
        total += random.randint(1, 6)
    await ctx.send(total)

# Rolls a #-sided die where the User choose the # and the Bot sends the Outcome to the Channel EX: !rolldie ....... # from list shown
@bot.command()
async def rolldie(ctx):
    restart = True
    e = True

    while restart and e:
        e = False
        try:
            message = await ctx.send("Choose a number from below. The number you choose will be how high of a die you roll (that number of sides on the die):\n**4**, **6**, **8**, **10**, **12**, **20** ")
    
            def check(m):
                return m.author == ctx.author
    
            message = await bot.wait_for("message", check = check, timeout = 10.0)
            m = message.content

            if m != "4" and m != "6" and m != "8" and m != "10" and m != "12" and m != "20":
                await ctx.send("Sorry, invalid choice.\n")
                e = True
                restart = True
                continue
            
            elif e == False:
                coming = await ctx.send("Here it comes...")
                await asyncio.sleep(1)
                await coming.delete()
                await ctx.send(f"**{random.randint(1, int(m))}**")
                restart = False
                break

        except asyncio.TimeoutError:
            await message.delete()
            await ctx.send("Procces has been canceled because you didn't respond in **10** seconds.")
            break

# Change the Bot's Status to Do Not Disturb and a random message for its Activity. EX: !botdnd
@bot.command()
async def botdnd(ctx):
    possible_activity = ["your Mom", "your Dad", "your Bro", "your Sis", "your Cuz", "your Gpa", "your Gma"]
    await ctx.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(random.choice(possible_activity)))

# User changes their Status to Do Not Disturb and Inputs their Activity. EX: !dnd
#@bot.command()
#async def dnd(ctx):
#    activity = 
#    await ctx.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(activity))

# When a User wants to get the Date and Current Time sent to them as a DM from the Bot. EX: !now
@bot.command()
async def now(ctx):
    currentDate = datetime.datetime.now()
    await ctx.author.send(currentDate.strftime(r"%B %d, %Y - %I:%M %p"))

# Allows a User to create a RemindMe Scheduler (in either Seconds, Minutes, Hours, or Days) which will send a DM to that User when the time expires. EX: !remindme 10s To take out the trash
@bot.command()
async def remindme(ctx, time, *, task):
    def convert(time):
        pos = ['s', 'm', 'h', 'd']

        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2
        
        return val * time_dict[unit]
    
    converted_time = convert(time)

    if converted_time == -1:
        await ctx.send("You didn't answer the time correctly")
        return
    
    if converted_time == -2:
        await ctx.send("The time must be an integer")
        return

    await ctx.author.send(f"Scheduled a reminder for: **{task}** and it will go off in **{time}**")

    await asyncio.sleep(converted_time)
    await ctx.author.send(f"Here is your reminder for: **{task}**")

###############################################################################################################################################################################################################

# Executes the Bot with the specified Token. Token has been removed and used just as an example
bot.run(os.environ.get('DISCORD_TOKEN'))