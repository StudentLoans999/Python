# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands
import asyncio
from discord.ui import select, View

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create RPG Class
class ER(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gamesER = {} # initializing a dictionary to store the game session (state)

    async def cleanup_command_message(self, ctx): # deletes !er message
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass  # ignore errors if the message is not found

# # # Event Listener: Bot on_ready - For when ER has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('ER has loaded')
    
#
# # Command section ############################################################################
#

# # # Command: !er ; Player does !er when he wants to play ER. Can be done anywhere. EX: !er
    @commands.before_invoke(cleanup_command_message) # move the command usage of the player to the DMs
    @commands.hybrid_command(name='escaperoom', description = 'Do this command in any channel to play a private Escape Room game')
    async def escaperoom(self, ctx):

        if ctx.author.id in self.gamesER: # user is already in a game
            await ctx.author.send('_ _ \nAn **Escape Room** game is already in progress for you')
            return

        self.gamesER[ctx.author.id] = True # add the user to the games dictionary

# # Start game section ############################################################################

        await ctx.author.send(f"""_ _ \nWelcome to the **RPG** game. Let's get started with you setting up your character by choosing your name and stats.
                                \nThen the game will begin with you entering Zone and battling around Level enemies for experience and gold.
                                \nBattle tougher enemies by advancing to the next zone. These higher level enemies give you more experience and gold when defeated compared to enemies from lower zones.
                                \nTry to make it to the highest zone as you can before being defeated!
                                \nSo, let's get started.""")
        
        sent_DM_message = await ctx.send(f"{ctx.author.mention} Check your DMs since that's where you'll play the game") # let the player know to continue the game in their DMs

        try: # delete !er that player did outside of the DMs and also delete the bot's message saying to check DMs

            await asyncio.gather(
                sent_DM_message.delete(delay=5),
                ctx.message.delete()
            )

        except discord.NotFound:
            pass  # ignore NotFound error if the message was already deleted

############################################################################

    # Bot gives player an input (asking for their name)
    async def get_hero_name(self, ctx):
        try:
            response = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author and m.content.lower() != '!er' and m.content.lower() != 'timeout')
            return response.content # the player input their name ^
        
        except Exception as e:
            return False # the player did not input their name ^

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(ER(bot)) # name of the Class, look above