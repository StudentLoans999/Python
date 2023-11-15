# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands
import datetime
import asyncio

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create User Class
class User(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

# # # Event Listener: Bot on_ready - For when User has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('User has loaded')

# # # Event Listener: Bot on_message - For when a User does "!dm" or "!ping" or "!dnd", or "!now", or "!remindme" have that message deleted (so the channel doesn't get filled up)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "!dm":
            await message.delete()
        elif message.content == "!ping":
            await message.delete()
        elif message.content == "!dnd":
            await message.delete()
        elif message.content == "!now":
            await message.delete()
        elif message.content.startswith('!remindme'):
            await message.delete()

###############################################################################################################################################################################################################

#
# # Command section ############################################################################
#

# # # Command: !dm ; When a User does !dm in the Server, the Bot will DM him EX: !dm
    @commands.command(help = 'Get a DM from the Bot', description = 'The Bot will DM you a set message \nExample: !dm')
    async def dm(self, ctx):
        await ctx.message.author.send(f'Hi, my name is {ctx.bot.user} and I am the bot for this server!')

# # # Command: !ping ; When a User does !ping in the Server, the Bot will DM him: "pong!" with the latency outputted EX: !ping
    @commands.command(help = 'Check your latency', description = 'The Bot will DM you with your latency \nExample: !ping')
    async def ping(self, ctx):
        await ctx.message.author.send(f"pong! {round(self.bot.latency * 1000)}ms")

# # # Command: !dnd ; User changes their Status to Do Not Disturb and Inputs their Activity. EX: !dnd
    #@commands.command(help = 'Change your Status to Do Not Disturb', description = 'Your status changes to Do Not Disturb and you input your Activity \nExample: !dnd')
    #async def dnd(self, ctx):
    #    activity = 
    #    await ctx.bot.change_presence(status = discord.Status.dnd, activity = discord.Game(activity))

# # # Command: !now ; When a User wants to get the Current Date and Time sent to them as a DM from the Bot EX: !now
    @commands.command(help = 'Check the current Date and Time', description = 'The Bot will DM you with the current Date and Time \nExample: !now')
    async def now(self, ctx):
        currentDate = datetime.datetime.now()
        await ctx.author.send(currentDate.strftime(r"%B %d, %Y - %I:%M %p"))

# # # Command: !remindme #unit task name ; Allows a User to create a RemindMe Scheduler (in either Seconds, Minutes, Hours, or Days) which will send a DM to that User when the time expires EX: !remindme 10s To take out the trash
    @commands.command(help = 'Set a Reminder from the Bot', description = 'The Bot will DM you and guide you in setting a Task Reminder \nExample: !remindme 10s To take out the trash')
    async def remindme(self, ctx, time = commands.parameter(default = '5s', description = '- Put in a number and a unit of time'), *, task = commands.parameter(default = 'Take out the trash', description = '- Put in what you want to be reminded about')):
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

# # # Command: !qanda ; the Bot @s them in a message in the same Channel that asks them a predefined question and provides predefined answers
    # Then the Bot waits for anyone to respond with !predefinedAnswerChoice and then the Bot sends a message to that same Channel
    @commands.command(help = 'Create a question with answer choices (and responses to them)', description = 'The Bot will guide you in how to create a question with answers for people to choose from')
    async def qanda(self, ctx):
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
            msg = await self.bot.wait_for("message", check = check)
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

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(User(bot)) # name of the Class, look above