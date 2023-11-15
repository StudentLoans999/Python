# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create Moderator Class
class Moderator(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

# # # Event Listener: on_ready - For when Moderator has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderator has loaded')

###############################################################################################################################################################################################################

#
# # Command section ############################################################################
#

# # # Command: !clear # ; Allows the Moderator Role to Delete messages in a Channel by doing !clear #OfMessagesToDelete EX: !clear 3
    @commands.command(name="clear", help='Delete a specified number of messages from the current channel', description='The Bot will delete the number of messages you tell it to. 100 is the limit \nExample: !clear 3')
    @commands.has_role('Moderator')
    async def clear(self, ctx, number:int = commands.parameter(default= 1, description="- Type in a number")):
        channel = ctx.channel
        if number > 100:
            number = 101
        await channel.purge(limit=number+1)
        await ctx.send(f"Deleted the last {number} message(s) in this channels")

# # # Command: !mute user ; Allows the Moderator Role to Mute a specified User by doing !mute User EX: !mute cool-man-stu     EX: !mute @CoolManStu
    @commands.command(help='Mute a specified user', description='The user will be muted \nExample: !mute @CoolManStu \nYou can unmute them with the Command: !unmute')
    @commands.has_role('Moderator')
    async def mute(self, ctx, member : discord.Member = commands.parameter(default= None, description="- Type in a user")):
        await member.edit(mute=True)
        await member.send("You have been muted by the Moderator")

# # # Command: !unmute user ; Allows the Moderator Role to Unmute a specified User by doing !unmute User EX: !unmute cool-man-stu     EX: !unmute @CoolManStu
    @commands.command(help='Unmute a specified user', description='The user will be unmuted \nExample: !unmute @CoolManStu \nYou can mute them with the Command: !mute')
    @commands.has_role('Moderator')
    async def unmute(self, ctx, member : discord.Member = commands.parameter(default= None, description="- Type in a user")):
        await member.edit(mute=False)
        await member.send("You have been unmuted by the Moderator")

# # # Command: !kickuser user ; Allows the Moderator Role to Kick Users in a Server by doing !kickuser User EX: !unmute cool-man-stu     EX: !kickuser @CoolManStu
    @commands.command(help='Kick a specified user from the server', description='The Bot will kick the user you tell it to \nExample: !kickuser @CoolManStu')
    @commands.has_role('Moderator')
    async def kickuser(self, ctx, member : discord.Member= commands.parameter(default= None, description="- Type in a user"), *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

# # # Command: !banuser user ; Allows the Moderator Role to Ban Users in a Server by doing !banuser User EX: !banuser cool-man-stu     EX: !banuser @CoolManStu
    @commands.command(help='Ban a specified user from the server', description='The Bot will ban the user you tell it to \nExample: !banuser @CoolManStu')
    @commands.has_role('Moderator')
    async def banuser(self, ctx, member : discord.Member = commands.parameter(default= None, description="- Type in a user"), *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

# # # Command: !unbanuser user ; Allows the Moderator Role to Un-Ban Users in a Server by doing !unbanuser User. EX: !unbanuser cool-man-stu     EX: !unbanuser @CoolManStu
    @commands.command(help='Unban a specified user from the server', description='The Bot will unban the user you tell it to \nExample: !unbanuser @CoolManStu')
    @commands.has_role('Moderator')
    async def unbanuser(self, ctx, *, member : discord.Member = commands.parameter(default= None, description="- Type in a user")):
        obj = await commands.UserConverter().convert(ctx, member)
        if obj is None:
            id_ = await commands.IDConverter().convert(str(member))
            if id_ is not None:
                try:
                    obj = await ctx.bot.fetch_user(int(id_.group(1))) #1234
                except discord.NotFound:
                    obj = None
            if obj is None:
                await ctx.send('User not found')
                return 
        await ctx.guild.unban(obj)
        await ctx.send(f'Unbanned {obj}')

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(Moderator(bot)) # name of the Class, look above