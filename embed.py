# # Cog Setup section

import discord
from discord.ext import commands

# Create Embed Class
class Embed(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # Event Listener: on_ready - For when the Embeds have been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('Embeds have loaded')

    # Event Listener: on_message - For when a User does "!embed", have that message deleted (so the channel doesn't get filled up)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "!embed":
            await message.delete()

    # You can add up to 25 fields to the same embed. Can only have up to 3 fields side-by-side. Can do 1 field per row. Can do 2 fields containing all the values (like a table)

    # Command: !embed ; When a User does !embed, he gets to create and post their own Embed (link with additional info) EX: !embed
    @commands.command(help='Create an embedded link (with optional additional info)', description='The Bot will guide you in how to create an embedded link')
    async def embedtest(self, ctx, member:discord.Member = None):
        if member == None:
            member = ctx.author

        name = member.display_name # the name of the User who did this command
        pfp = member.display_avatar # the avatar of the User who did this command

        embed = discord.Embed(title="This is my embed", description="It is a very cool embed", color=discord.Color.random())
        embed.set_author(name=f"{name}", url="https://www.youtube.com/watch?v=urLZoyLUDdE&list=PLW9I0hYEya07AHzGNHh470BODgNae8RPh&index=4", icon_url=f"{pfp}")
        embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
        embed.add_field(name="This is 1 field", value="Description of field 1")
        embed.add_field(name="This is 2 field", value="This field is inline True", inline = True)
        embed.add_field(name="This is 3 field", value="This field is inline False", inline = False)
        embed.add_field(name="This is 4 field", value="This field is inline False", inline = False)
        embed.set_image(url="https://media.istockphoto.com/id/1281804798/photo/very-closeup-view-of-amazing-domestic-pet-in-mirror-round-fashion-sunglasses-is-isolated-on.webp?s=1024x1024&w=is&k=20&c=UtXosVVZG_ly8mymCjA4vGPnT0vzDZajOvoV5yUT1ng=")
        embed.set_footer(text=f"{name} made this Embed")

        await ctx.send(embed=embed) # Bot sends a message

    # Command: !embed ; When a User does !embed, he gets to create and post their own Embed (link with additional info) EX: !embed
    @commands.command(help='Create an embedded link (with optional additional info)', description='The Bot will guide you in how to create an embedded link')
    async def embed(self, ctx, member:discord.Member = None):
        if member == None:
            member = ctx.author

        

        name = member.display_name # the name of the User who did this command
        pfp = member.display_avatar # the avatar of the User who did this command

        embed = discord.Embed(title="This is my embed", description="It is a very cool embed", color=discord.Color.random())
        embed.set_author(name=f"{name}", url="https://www.youtube.com/watch?v=urLZoyLUDdE&list=PLW9I0hYEya07AHzGNHh470BODgNae8RPh&index=4", icon_url=f"{pfp}")
        embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
        embed.add_field(name="This is 1 field", value="Description of field 1")
        embed.add_field(name="This is 2 field", value="This field is inline True", inline = True)
        embed.add_field(name="This is 3 field", value="This field is inline True", inline = True)
        embed.set_image(url="https://media.istockphoto.com/id/1281804798/photo/very-closeup-view-of-amazing-domestic-pet-in-mirror-round-fashion-sunglasses-is-isolated-on.webp?s=1024x1024&w=is&k=20&c=UtXosVVZG_ly8mymCjA4vGPnT0vzDZajOvoV5yUT1ng=")
        embed.set_footer(text=f"{name} made this Embed")

        await ctx.send(embed=embed) # Bot sends a message

async def setup(bot):
    await bot.add_cog(Embed(bot)) # name of the Class, defined at the top