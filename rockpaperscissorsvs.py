# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands
import asyncio

rpsvs = 0

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create Rock_Paper_Scissors_VS Class
class Rock_Paper_Scissors_VS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gamesRPS = {} # initializing an empty dictionary, which will be used later on to establish a connection between Player 1 (ID) and Player 2 (ID)

# # # Event Listener: Bot on_ready - For when Rock_Paper_Scissors_VS has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('Rock_Paper_Scissors_VS has loaded')

# # # Event Listener: Bot on_message - For when a User does !rps anywhere, have that message deleted (so the channel doesn't get filled up)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "!rpsvs":
            await message.delete()

#
# # Command section ############################################################################
#

# # # Command: !rpsvs ; Player does !rpsvs when he wants to play Rock, Paper, Scissors against someone else. Can be done anywhere. EX: !rpsvs
    @commands.hybrid_command(name='rpsvs', description ='Do this command in any channel to play a private game of RPS against someone else')
    async def rpsvs(self, ctx): 
        global rpsvs

        if ctx.author.id in self.gamesRPS: # user is already in a game
            await ctx.author.send('_ _ \nYou are already playing a game of **Rock, Paper, Scissors - VS**')
        elif rpsvs == 0: # self.gamesRPS should be empty at the start, so this should run fine the first time around ; the game has not been started already and this is the first time a user did !rpsvs
            
            rpsvs = 1
            original_channel = ctx.channel # store the original channel where the user initatiated !rpsvs
            await original_channel.send(f"_ _ \n{ctx.author.mention} wants to start a Rock, Paper, Scissors - VS game! \nWhoever wants to challenge me, do: **!rpsvs** in the server: **Heart-to-Heart**")

            try: # waits for the second player to join

                rpsvs = 2
                player2_message = await self.bot.wait_for('message', timeout=10, check=lambda m: m.author != ctx.author and m.content.lower().startswith('!rpsvs')) # player 2 has to join by doing !rpsvs
                player2 = player2_message.author

                # Associate the two players' IDs with each other, making it easy to find who is playing against whom
                self.gamesRPS[ctx.author.id] = player2.id # sets Player 1 to associate with Player 2. EX: if ctx.author.id is cool_man_stu and player2.id is jabroni_jim then self.gamesRPS now looks like this: { cool_man_stu: jabroni_jim }
                self.gamesRPS[player2.id] = ctx.author.id # sets Player 2 to associate with Player 1. EX: now after adding this line, the dictionary self.gamesRPS looks like this: { cool_man_stu: jabroni_jim,  jabroni_jim: cool_man_stu}

                await self.start_rpsvs_game(ctx.author, player2, original_channel) # pushes these three arguments into the method and then runs that method

            except asyncio.TimeoutError: # a second user did not do !rpsvs within the time limit so didn't join the match in time
                await ctx.author.send('_ _ \nNo one challenged you within 10 seconds. Please do **!rpsvs** in the server: **Heart-to-Heart** to try again')
                rpsvs = 0

        elif ctx.author.id not in self.gamesRPS: # player 1 is spamming !rpsvs before player 2 joins. Or, a different user is trying to start a match when one is being played by two other users 
            sent_message = await ctx.author.send('_ _ \nYou already did **!rpsvs** so just wait for someone to join; or a match has already started so just wait for that to finish')
            await sent_message.delete(delay=3)

############################################################################

    async def start_rpsvs_game(self, player1, player2, channel): # takes in the three arguments created earlier, as parameters
        global rpsvs

        await channel.send(f"""_ _ \nThe **Rock, Paper, Scissors - VS** game has now been started. \n\n{player1.mention} is **Player 1** and {player2.mention} is **Player 2**.
                           \nClassic rules. Good luck to you both!""")

        await player1.send(f"_ _ \nYou're playing Rock, Paper, Scissors - VS against {player2.mention}! \n\nMake your move by doing: **rock** or **paper** or **scissors**")
        await player2.send(f"_ _ \nYou're playing Rock, Paper, Scissors - VS against {player1.mention}! \n\nThey're doing their move right now; I'll message you when it's your turn")

        try: # give player 1 the list of possible moves to do (rock, paper, scissors) 
            move1_message = await self.bot.wait_for('message', timeout=20, check=lambda m: m.author == player1 and m.content.lower() in ('rock', 'paper', 'scissors'))
            move1 = move1_message.content.lower()  # set Player 1's message to be move1

        except asyncio.TimeoutError: # player 1 did not input their move in time
            await player1.send("_ _ \nYou took too long to make a move. The game is now canceled")
            await player2.send(f"_ _ \n{player1.mention} took too long to make a move. The game is now canceled")
            await channel.send(f"_ _ \nThe Rock, Paper, Scissors - VS game between {player1.mention} and {player2.mention} has finished")
            del self.gamesRPS[player1.id] # clear the self.gamesRPS dictionary, to allow a new game to be started
            del self.gamesRPS[player2.id] # clear the self.gamesRPS dictionary, to allow a new game to be started
            rpsvs = 0 # reset this variable
            return # stop the game

        await player2.send(f"_ _ \n{player1.mention} chose a move! \nIt's your turn to make a move, by doing: **rock** or **paper** or **scissors**") # this is after player 1 chose a move 
        await player1.send(f"_ _ \n{player2.mention} is doing their move right now; I'll message you the results when they finished thier turn")

        try: # give player 2 the list of possible moves to do (rock, paper, scissors) 
            move2_message = await self.bot.wait_for('message', timeout=20, check=lambda m: m.author == player2 and m.content.lower() in ('rock', 'paper', 'scissors'))
            move2 = move2_message.content.lower() # set Player 2's message to be move2

        except asyncio.TimeoutError: # player 2 did not input their move in time
            await player2.send("_ _ \nYou took too long to make a move. The game is now canceled")
            await player1.send(f"_ _ \n{player2.mention} took too long to make a move. The game is now canceled")
            await channel.send(f"_ _ \nThe Rock, Paper, Scissors - VS game between {player1.mention} and {player2.mention} has finished")
            del self.gamesRPS[player1.id] # clear the self.gamesRPS dictionary, to allow a new game to be started
            del self.gamesRPS[player2.id] # clear the self.gamesRPS dictionary, to allow a new game to be started
            rpsvs = 0 # reset this variable
            return # stop the game

        result = self.determine_winner(move1, move2, player1, player2) # pushes these four arguments into the method and then runs that method

        # Announce the winner, sends a DM to both Players
        if result is None: # draw, done in the section below

            await player1.send(f"_ _ \nThe game is a draw! Both players chose **{move1}**. \n The game is now finished")
            await player2.send(f"_ _ \nThe game is a draw! Both players chose **{move2}**. \n The game is now finished")
            await channel.send(f"_ _ \nThe Rock, Paper, Scissors - VS game between {player1.mention} and {player2.mention} has finished")

        else: # not a draw

            await player1.send(f"_ _ \n{result.mention} wins! \n\n{player1.mention} did **{move1}** and {player2.mention} did **{move2}**! \n\n The game is now finished")
            await player2.send(f"_ _ \n{result.mention} wins! \n\n{player1.mention} did **{move1}** and {player2.mention} did **{move2}**! \n\n The game is now finished")
            await channel.send(f"_ _ \nThe Rock, Paper, Scissors - VS game between {player1.mention} and {player2.mention} has finished")

        del self.gamesRPS[player1.id] # removes Player 1 from the dictionary, in order to empty it
        del self.gamesRPS[player2.id] # removes Player 2 from the dictionary, in order to empty it. (It should be empty now)
        rpsvs = 0 # reset this variable
        return # stop the game

############################################################################

    def determine_winner(self, move1, move2, player1, player2): # takes in the four arguments created earlier, as parameters, and assigns the return value into the result variable
        
        if move1 == move2 and move1 in ('rock', 'paper', 'scissors'): # players did the same move, resulting in a draw
            return None

        elif (move1 == 'rock' and move2 == 'scissors') or (move1 == 'paper' and move2 == 'rock') or (move1 == 'scissors' and move2 == 'paper'): # player 1 beat player 2
            return player1

        else: # player 2 beat player 1
            return player2

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(Rock_Paper_Scissors_VS(bot)) # name of the Class, look above