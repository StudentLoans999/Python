# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands
import datetime
import asyncio
from discord.ui import View, Select, button
from typing import List
from collections import deque

###############################################################################################################################################################################################################

#
# # Custom help section ############################################################################
#

class PaginatorView(discord.ui.View):
    def __init__(
            self,
            embeds: List[discord.Embed]
    ) -> None:
        super().__init__(timeout=30)

        self._embeds = embeds
        self._queue = deque(embeds)
        self._initial = embeds[0]
        self._len = len(embeds)
        self._current_page = 1
        self._queue[0].set_footer(text=f"Pages of {self._current_page}/{self._len}")

    async def update_buttons(self, interaction: discord.Interaction) -> None:
        for i in self._queue:
            i.set_footer(text=f"Pages of {self._current_page}/{self._len}")

        if self._current_page == self._len:
            self.children[1].disabled = True
        else:
            self.children[1].disabled = False

        if self._current_page == 1:
            self.children[0].disabled = True
        else:
            self.children[0].disabled = False

        await interaction.message.edit(view=self)

    @discord.ui.button(label='C:\IT\DiscordBot\left_arrow.png')
    async def previous(self, interaction: discord.Interaction, _):
        self._queue.rotate(-1)
        embed = self._queue[0]
        self._current_page -= 1
        await self.update_buttons(interaction)
        await interaction.response.edit_message(embed=embed)        

    @discord.ui.button(label='C:\IT\DiscordBot\right_arrow.png')
    async def next(self, interaction: discord.Interaction, _):
        self._queue.rotate(1)
        embed = self._queue[0]
        self._current_page += 1
        await self.update_buttons(interaction)
        await interaction.response.edit_message(embed=embed)

    @property
    def initial(self) -> discord.Embed:
        return self._initial

############################################################################

class HelpSelect(Select):
    def __init__(self, cog: commands.Cog):
        super().__init__(
            placeholder="Choose a category",
            options=[
                discord.SelectOption(
                    label=cog_name, description=cog.__doc__
                ) for cog_name, cog in cog.cogs.items() if cog.__cog_commands__ and cog_name not in ['Moderator']
            ]
        )
        
        self.cog = cog

    async def callback(self, interaction: discord.Interaction) -> None:
        cog = self.cog.get_cog(self.values[0])
        assert cog

        commands_mixer = []
        for i in cog.walk_commands():
            commands_mixer.append(i)

        for i in cog.walk_app_commands():
            commands_mixer.append(i)

        embed = discord.Embed(
            title=f"{cog.__cog_name__} Commands",
            description='\n'.join(
                f"**{command.name}**: '{command.description}'"
                for command in commands_mixer
            )
        )
        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )        

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
        elif message.content == '!help':
            await message.delete()

###############################################################################################################################################################################################################

#
# # Command section ############################################################################
#

# # # Command: !help ; the Bot will give info on commands EX: !help
    @commands.hybrid_command(name='help', description = 'Shows list of commands')
    async def help(self, ctx: commands.Context):
        embed = discord.Embed(
            title="List of Commands",
            description="Choose a category of commands you want to view"
        )
        view = View().add_item(HelpSelect(self.bot))
        await ctx.send(embed=embed, view=view)

############################################################################

# # # Command: !dm ; When a User does !dm in the Server, the Bot will DM him EX: !dm
    @commands.hybrid_command(name='dm', description = 'Get a DM from the Bot')
    async def dm(self, ctx):
        await ctx.message.author.send(f'Hi, my name is **{ctx.bot.user}** and I am the bot for the server: Heart-to-Heart!')

############################################################################

# # # Command: !ping ; When a User does !ping in the Server, the Bot will DM him: "pong!" with the latency outputted EX: !ping
    @commands.hybrid_command(name='ping', description = 'Check your latency')
    async def ping(self, ctx):
        await ctx.message.author.send(f"pong! {round(self.bot.latency * 1000)}ms")

############################################################################

# # # Command: !dnd ; User changes their Status to Do Not Disturb and Inputs their Activity. EX: !dnd
    #@commands.hybrid_command(name='dnd', description = 'Change your Status to Do Not Disturb with your Activity')
    #async def dnd(self, ctx):
    #    activity = 
    #    await ctx.bot.change_presence(status = discord.Status.dnd, activity = discord.Game(activity))

############################################################################

# # # Command: !now ; When a User wants to get the Current Date and Time sent to them as a DM from the Bot EX: !now
    @commands.hybrid_command(name='now', description = 'Check the current Date and Time')
    async def now(self, ctx):
        currentDate = datetime.datetime.now()
        await ctx.author.send(currentDate.strftime(r"%B %d, %Y - %I:%M %p"))

############################################################################

# # # Command: !remindme #unit task name ; Allows a User to create a RemindMe Scheduler (in either Seconds, Minutes, Hours, or Days) which will send a DM to that User when the time expires EX: !remindme 10s To take out the trash
    @commands.hybrid_command(name='remindme', description = 'Set a Reminder from the Bot')
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

############################################################################

# # # Command: !qanda ; the Bot @s them in a message in the same Channel that asks them a predefined question and provides predefined answers
    # Then the Bot waits for anyone to respond with !predefinedAnswerChoice and then the Bot sends a message to that same Channel
    @commands.hybrid_command(name='qanda', description = 'Create a question with answer choices (and responses to them)')
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