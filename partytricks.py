# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands
import random
import asyncio

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create partytricks Class
class Partytricks(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

# # # Event Listener: Bot on_ready - For when Partytricks has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('Partytricks has loaded')

###############################################################################################################################################################################################################

#
# # Command section ############################################################################
#

# # # Command: !eightball question (any text) ; The Bot will respond with a message in the same Channel EX: !eightball question here
    # It would contain the question asked along with a random quote chosen from 'responses'
    @commands.command(aliases = ['8ball'], help = 'Ask the 8 Ball a Yes or No question', description = 'The Bot will give you an answer \nExample: !8ball Am I going to win the lottery')
    async def eightball(self, ctx, *, question = commands.parameter(default = None, description = "- Put in a Yes or No question to ask")):
        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
                    "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", 
                    "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"
                    ] # a list of possible answers the Bot gives to the question the User asked the 8ball
        response_to_none = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
                            "Yes", "Signs point to yes"
                            ] # a list of possible answers the Bot gives to the User when they didn't ask a question
        
        # User only did !eightball and did not ask a question, so the Bot offers them a helpful message
        if question == None:
            await ctx.send(f':8ball: **Question**: Do I need to try **!help eightball** to understand how to use the command properly?:8ball:\n:8ball: **Answer**: {random.choice(response_to_none)}:8ball:')
              
        else: # user asked a Question after doing !eightbhelpall
            await ctx.send(f':8ball: **Question**: {question}:8ball:\n:8ball: **Answer**: {random.choice(responses)}:8ball:')

# # # Command: !roll2 ; Rolls two six-sided dice and shows each Outcome and then adds them together and the Bot sends the Total Result to the Channel EX: !roll2
    @commands.command(help = 'Rolls two six-sided dice one-by-one, showing you the outcomes, and totaling the results', description = 'The Bot will show you it generating two numbers between 1-6, adding them together, and the total')
    async def roll2(self, ctx):
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

# # # Command: !ezroll ; Rolls two six-sided dice and the Bot sends the Total Result to the Channel EX: !ezroll
    @commands.command(help = 'Rolls two imaginary six-sided dice and then tells you the final outcome', description = 'The Bot will generate two numbers between 1-6, adds them together, and sends you the total')
    async def ezroll(self, ctx):
        total = 0
        for i in range(2):
            total += random.randint(1, 6)
        await ctx.send(total)

# # # Command: !rolldie # ; Rolls a #-sided die where the User choose the # and the Bot sends the Outcome to the Channel EX: !rolldie ....... # from list shown
    @commands.command(help = 'Rolls a die that has as many sides as you told it to have from the list and then tells you the result', description = 'The Bot will generate a number between 1 amd the one you selected and then tells you the outcome')
    async def rolldie(self, ctx):
        restart = True
        e = True

        while restart and e:
            e = False
            try:
                message = await ctx.send("Choose a number from below. The number you choose will be how high of a die you roll (that number of sides on the die):\n**4**, **6**, **8**, **10**, **12**, **20** ")
        
                def check(m):
                    return m.author == ctx.author
        
                message = await self.bot.wait_for("message", check = check, timeout = 10.0)
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

# # # Command: !rollcustomdie # ; Rolls a #-sided die where the User inputs the # and the Bot sends the Outcome to the Channel EX: !rollcustomdie #
    @commands.command(help = 'Rolls a die that has as many sides as you told it to have and then tells you the result', description = 'The Bot will generate a number between 1 amd the one you said and then tells you the outcome')
    async def rollcustomdie(self, ctx):
        restart = True
        e = True

        while restart and e:
            e = False
            try:
                message = await ctx.send("Type in a number. The number you choose will be how high of a die you roll (that number of sides on the die)")

                def check(m):
                    return m.author == ctx.author

                message = await self.bot.wait_for("message", check = check, timeout = 10.0)
                m = message.content

                if not [int(s) for s in m.split() if s.isdigit()]:
                    await ctx.send("Sorry, invalid choice.\n")
                    e = True
                    restart = True
                    continue
                
                if e == False:
                    coming = await ctx.send("Here it comes...")
                    await asyncio.sleep(1)
                    await coming.delete()
                    await ctx.send(f"**{random.randint(1, int(m))}**")
                    restart = False
                    break

            except asyncio.TimeoutError:
                await message.delete()
                await ctx.send("Procces has been canceled because you didn't respond in **10** seconds")
                break


# # # Command: !botdnd ; Change the Bot's Status to Do Not Disturb and a random message for its Activity EX: !botdnd
    @commands.command(help = 'Change the Status of the Bot to Do Not Disturb and gives it an Activity to do ;p', description = 'The Bot will go to Do Not Disturb since it will be busy doing something...')
    async def botdnd(self, ctx):
        possible_activity = ["your Mom", "your Dad", "your Bro", "your Sis", "your Cuz", "your Gpa", "your Gma"]
        await ctx.bot.change_presence(status = discord.Status.dnd, activity = discord.Game(random.choice(possible_activity)))

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(Partytricks(bot)) # name of the Class, look above