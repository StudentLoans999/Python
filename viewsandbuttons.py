# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands

###############################################################################################################################################################################################################

#
# # Buttons section ############################################################################
#

# # # Create faq Class ; (Not shown in the !help command block)
class faq(discord.ui.View):
  
    # The FAQ View has a timeout of 3 minutes
    def __init__(self, *, timeout = 180): # specify the timeout here (in seconds)
        super().__init__(timeout=timeout) 

    # You can add up to 25 buttons to the same view, but make sure its custom_id and function name are always different

# # # Button: FAQ1 ; Introduction 
    @discord.ui.button(label = 'Start here', custom_id = "FAQ1")
    async def FAQ1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"""I bet you are wondering what all of this is and what you can do with it all. 
                                                \n Well, this server is a place of **community**. We offer channels dedicated to **social minigames**,
                                                 but if you just want a place to chat around, that is done in <#1171905233467752530>    
                                                ...All run by me and the one who stared it all, David Richey, aka doubleoel
                                                ...""")

# # # Button: FAQ2 ; The General Channel 
    @discord.ui.button(label = 'The General Channel', custom_id = "FAQ2") # , emoji = '\U0001F606'
    async def FAQ2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"""<#1171905233467752530> This channel
                                                \n 
                                                ...""")
      
# # # Button: FAQ3 ; Mini Game Channels 
    @discord.ui.button(label = 'Mini Game Channels', custom_id = "FAQ3")
    async def FAQ3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"""I bet you are wondering what all of this is and what you can do with it all. 
                                                \n Well, this server is a place of **community**. We offer channels dedicated to **social minigames**, but if you just want a place to chat around, that is done in <#1171905233467752530>    
                                                ...All run by me and the one who stared it all, David Richey, aka doubleoel
                                                ...""")

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create Buttons Class 
class Buttons(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
# # # Event Listener: Bot on_ready - For when the Buttons have been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('Buttons have loaded')

# # # Event Listener: Bot on_message - For when a User does "!faq", have that message deleted (so the channel doesn't get filled up) 
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "!faq":
            await message.delete()

###############################################################################################################################################################################################################

#
# # Command section ############################################################################
#

# # # Command: !faq (View trigger) ; When a User does !faq in the " " Channel, it makes the Bot show: FAQ View with Buttons. EX: !faq 
    @commands.command(help = 'Start here if you have any questions', description = 'The Bot will provide some info through some interactive buttons')
    async def faq(self, ctx):
        await ctx.message.author.send("Hi! What you would like some information on?", view = faq())

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(Buttons(bot)) # name of the Class, defined at the top