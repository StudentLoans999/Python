# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands
import asyncio
import random

HIDDEN_CARD_PLACEHOLDER = '||:black_square_button:||'  # Use a placeholder for hidden cards
flip_number = 0 # this is used to help delete a message (the final board that appears when Player 1 flips a card) ; used in the send_spoiler_board method

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create Memory_Match Class

class Memory_Match(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gamesMM = {} # initializing an empty dictionary, which will be used later on to establish the game board (random card arrangement), the flipped cards, the two players, and whose turn it is

    # # # Event Listener: Bot on_ready - For when Memory_Match has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('Memory_Match has loaded')

# # # Event Listener: Bot on_message - For when a User does !memorymatch outside the right channel or !flip anywhere, have that message deleted (so the channel doesn't get filled up)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # ignore messages from bot
    
        if isinstance(message.channel, discord.TextChannel): # delete this line if it causes errors later
            if message.channel.name != "memory-match": 
                if message.content == "!memorymatch":
                    await message.delete()

                elif message.content.startswith("!flip"): 
                    await message.delete()

#
# # Command section ############################################################################
#

# # # Command: !memorymatch ; When a User does !memorymatch in the memory-match channel, the the game: Memory Match starts EX: !memorymatch
    @commands.hybrid_command(name='memorymatch', description='Play Memory Match game (go to memory-match Channel first)')
    async def memorymatch(self, ctx):

        # Makes sure !memorymatch can only be run in the right channel
        if ctx.channel.name != "memory-match": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!memorymatch** which is specific to the Channel: <#1179215839166201917> Please go there and try it")
            return
        
        elif ctx.channel.name == "memory-match": # the command was done in the correct Channel: memory-match

            channel_id = ctx.channel.id

            if channel_id not in self.gamesMM: # checks if a game is not already running

                # First time running !memorymatch in this channel
                await ctx.send(f"{ctx.author.mention} wants to start a Memory Match game! \nWhoever wants to join, do: **!memorymatch**")
                self.gamesMM[channel_id] = {'players': [ctx.author.id], 'flipped_cards': [], 'turn': 0, 'board': self.create_board()} # initialize everything in the dictionary ; assigns the user who started the game as Player 1

                try:
                    # Wait for the second player to join
                    player2_message = await self.bot.wait_for('message', timeout=10, check=lambda m: m.author != ctx.author and m.content.lower().startswith('!memorymatch'))
                    player2 = player2_message.author # assigns the user who does !memorymatch the second time as Player 2

                except asyncio.TimeoutError: # if no one does !memorymatch after it Player 1 did it 

                    await ctx.reply(f'No one wanted to play with you within 10 seconds. \nPlease do **!memorymatch** to try again')
                    del self.gamesMM[channel_id]
                    return

            elif self.gamesMM[channel_id]['players'][0] == ctx.author.id: # a game is already running and the same user who started it, is now trying to start a new game

                await ctx.reply('You have already started a Memory Match game, please wait for someone else to join you in the next 10 seconds')

            elif len(self.gamesMM[channel_id]['players']) == 1: # if one player in the game

                player1 = self.gamesMM[channel_id]['players'][0] # retrieves the ID of the first player in the list and assigns it to Player 1
                player2 = ctx.author.id # assigns the user who does !memorymatch the second time as Player 2
                del self.gamesMM[channel_id]  # remove the game from the "waiting for players" state (so game is ready to start)
                await self.start_memory_match_game(player1, player2, ctx.channel, channel_id) # starts the game with the two players set

            else: # unexpected state, should not happen 
                await ctx.send('A Memory Match game is already in progress.')


############################################################################

    # Starts the game by initializing the dictionary, listing out the rules, and sending out the game board
    async def start_memory_match_game(self, player1, player2, channel, channel_id):
        player1 = self.bot.get_user(player1)
        player2 = self.bot.get_user(player2)
        self.gamesMM[channel_id] = {'players': [player1.id, player2.id], 'flipped_cards': [], 'turn': 0, 'board': self.create_board()}
        await channel.send(f"""\nThe **memorymatch** game has now been started. \n\n{player1.mention} is **Player 1** and {player2.mention} is **Player 2**.
                           \nYou two will work together using your memory to try to match cards bv flipping them one-at-a-time with {player1.mention} flipping the first card and then {player2.mention} looking for the match to flip.
                           \nGood luck to you both!
                           \n {player1.mention} do **\"!flip #\"** since it is your turn first""")
        await self.send_board(channel_id)

############################################################################

    # # # Command: !flip # ; When a User does !flip # in the memory-match channel, it will flip that corresponding card position. Range is 0-23. EX: !flip 4
    @commands.hybrid_command(name='flip', description="Do this command to flip a card, the number you input corresponds to the card's position (1-24)")
    async def flip(self, ctx, card_index: int):
        global flip_number

        # Makes sure !flip can only be run in the right channel
        if ctx.channel.name != "memory-match":
            await ctx.author.send(
                f"It looks like you have tried to do the command: **!flip #** which is specific to the Channel: <#1179215839166201917> Please go there and try it")
            return

        elif ctx.channel.name == "memory-match": # in the right channel
            channel_id = ctx.channel.id

            if channel_id in self.gamesMM: # checks if a game is already running

                game = self.gamesMM[channel_id]
                players = game['players']
                current_turn = game['turn'] # initialize variables

                if ctx.author.id in players: # checks if the command issuer is one of the players
                    
                    player_index = players.index(ctx.author.id)

                    if player_index == current_turn: # checks if the person who did !flip is their turn

                        if channel_id in self.gamesMM and len(self.gamesMM[channel_id]['players']) == 2: # if two players in the game

                            if self.gamesMM[channel_id]['players'][self.gamesMM[channel_id]['turn']] == ctx.author.id: # if the ID of the player whose turn it currently is (as stored in the game data) is equal to the ID of the user who invoked !flip

                                card_index -= 1 # this adjusts the card_index to start from 0 (more user-friendly)

                                flip_message = None  # initialize flip_message variable

                                if 0 <= card_index < len(self.gamesMM[channel_id]['board']): # makes sure the player flipped a card within the position range

                                    if card_index not in self.gamesMM[channel_id]['flipped_cards']: # checks that the player flipped a card that was not just flipped by the other player right before

                                        self.gamesMM[channel_id]['flipped_cards'].append(card_index) # adds the card that the player just flipped to the list of flipped cards 
                                        await self.send_board(channel_id) # sends the updated game board (with the newly flipped card)

                                        if len(self.gamesMM[channel_id]['flipped_cards']) == 2: # the second time !flip was done (aka the second card to flip) ; retrieves the list of flipped cards (should be 2)

                                            flip_number = 2 # used in the send_spoiler_board method
                                            flip_message = await ctx.send('Flipping card...') # sends a message but then assigns it to a variable which will be called below and used to delete this message

                                            # Simulating the second flip
                                            await asyncio.sleep(1)
                                            self.gamesMM[channel_id]['board'][self.gamesMM[channel_id]['flipped_cards'][0]]['hidden'] = True # makes the first flipped card hidden (see check_match method below)
                                            self.gamesMM[channel_id]['board'][self.gamesMM[channel_id]['flipped_cards'][1]]['hidden'] = False # makes the second flipped card visible (see check_match method below)

                                            # Hides the second card for Player 1 after a short delay so that the second card will be briefly visible before being hidden again
                                            if player_index == 0:

                                                second_card_index = self.gamesMM[channel_id]['flipped_cards'][1]
                                                await self.delayed_hide(ctx, second_card_index) 

                                            await self.check_match(ctx) # goes into the method which does flipped cards results state (win conditions)
                                            await self.send_board(channel_id)  # Send the board only after the flip

                                            # Delete the flip message "Flipping card..." as well as deleting the neweset board message
                                            await asyncio.sleep(1)
                                            await flip_message.delete()
                                            await self.delete_last_board_message(channel_id)

                                        elif len(self.gamesMM[channel_id]['flipped_cards']) == 1: # the first time !flip was done (aka the first card to flip) ; retrieves the list of flipped cards (should only be 1)
                                            
                                            flip_number = 1 # used in the send_spoiler_board method
                                            flip_message = await ctx.send('Flipping card...') # sends a message but then assigns it to a variable which will be called below and used to delete this message

                                            # Simulating the first flip
                                            self.gamesMM[channel_id]['board'][self.gamesMM[channel_id]['flipped_cards'][0]]['hidden'] = False # makes the first flipped card visible (see check_match method below)

                                            # Mention the current player and the next player
                                            next_player_id = self.gamesMM[channel_id]["players"][1 - self.gamesMM[channel_id]["turn"]] # 1 - self.gamesMM[channel_id]["turn"]: This expression calculates the index of the next player in the list
                                            #If the current turn is 0 (indicating the first player's turn), then 1 - 0 evaluates to 1, and if the current turn is 1, then 1 - 1 evaluates to 0. This effectively toggles between 0 and 1.
                                            next_player = self.bot.get_user(next_player_id)

                                            if isinstance(next_player, discord.User): # checks whether the next_player variable is an instance of the discord.User class
                                                await ctx.send(f'{ctx.author.mention}, it\'s now {next_player.mention}\'s turn.') # tells the other player that it's now their turn
                                            else:
                                                await ctx.send("An error occurred in fetching the next player")

                                            await self.send_board(channel_id)  # Send the board only after the flip

                                            # Delete the flip message "Flipping card..." as well as deleting the neweset board message
                                            await asyncio.sleep(1)
                                            await flip_message.delete()
                                            await self.delete_last_board_message(channel_id)

                                    else:
                                        await ctx.send('**This card has already been flipped. What a waste of a turn!**')
                                else:
                                    await ctx.send('There is no card to flip at that position. Next time, please flip a card within range: **1-24**')
                            else:
                                await ctx.send(f'It\'s not your turn. It\'s **{ctx.author.mention}** turn')
                        else:
                            await ctx.send('No game in progress. Start a new game with **!memorymatch**')

                        await ctx.send(f"_ _ \n{ctx.author.mention} flipped card at position: **{card_index + 1}**") # lets the other player know what card position you flipped
                        await self.send_spoiler_board(channel_id) # send the spoiler board after a card is flipped

                        # Update turn for the next player
                        game['turn'] = (current_turn + 1) % len(players) # increments the turn counter for the game. It uses the modulo operator (%) to ensure that the turn counter wraps around to 0 when it reaches the total number of players (2)
                        # this way, the turns cycle through the list of players. 2 % 2 = 0 (so turn 0) and 1 % 2 = 1 (so turn 1)
                        next_player_id = players[game['turn']]
                        next_player = self.bot.get_user(next_player_id) # the player who is next in line to take their turn

                        if isinstance(next_player, discord.User): # checks whether the next_player variable is an instance of the discord.User class
                            await ctx.send(f"_ _ \n{next_player.mention}, it's now your turn\n") # tells the other player that it's now their turn
                        else:
                            await ctx.send("An error occurred in fetching the next player")

                        # Delete the board message after a certain period (e.g., 5 seconds)
                        await asyncio.sleep(1)

                        # Get the last board message
                        last_board_message = self.gamesMM[channel_id].get('last_board_message')

                        # Delete the last board message if it exists
                        if last_board_message:
                            await last_board_message.delete()

                    else:
                        await ctx.reply(f"{ctx.author.mention}, it's not your turn to flip a card")
                else:
                    await ctx.send("You are not part of the Memory Match game.")
            else:
                await ctx.send("No Memory Match game is currently in progress in this channel")

############################################################################

    # Deletes the last game board message to keep things tidy and to make the game harder 
    async def delete_last_board_message(self, channel_id):
        # Get the last board message ID
        last_board_message_id = self.gamesMM[channel_id].get('last_board_message_id')

        # Delete the last board message if it exists
        if last_board_message_id:
            try:
                # Get the last board message
                last_board_message = await self.bot.get_channel(channel_id).fetch_message(last_board_message_id)

                # Delete the last board message
                await last_board_message.delete()
            except discord.errors.NotFound:
                print()

############################################################################

    # Create a game board containing Emoji card pairs and stores each card with its hidden state
    def create_board(self):
        cards = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🐯', '🦁', '🐮']  # the list of 12 cards
        card_pairs = cards * 2  # doubles the cards (so 24 in this case)
        random.shuffle(card_pairs)  # shuffles all the pairs
        hidden_cards = [{'emoji': card, 'hidden': True} for card in card_pairs] # creates a list of dictionaries, where each dictionary represents a card on the game board
        # each dictionary has two key-value pairs: 'emoji', which stores the emoji of the card, and 'hidden', which initially is set to True to indicate that the card is hidden
        return hidden_cards # returns the list of hidden cards, which represents the initial state of the game board

############################################################################

    # Deletes the last game board message to keep things tidy and to make the game harder. Adds cards to game board, either emoji or the placeholder (hidden) and then displays the original game board
    async def send_board(self, channel_id):
        # Get the last board message
        last_board_message = self.gamesMM[channel_id].get('last_board_message')

        # Delete the last board message if it exists
        if last_board_message:
            try:
                await last_board_message.delete()
            except discord.errors.NotFound:
                print()
        
        board = self.gamesMM[channel_id]['board'] # retrieves the current state of the game board from the game data stored in the self.gamesMM dictionary
        board_str = '' # initializes an empty string (which will be used to create the representation of the game board)
        for i, card_info in enumerate(board): # iterates over each card in the game board ; 'i' represents the index of the card in the board
            if i % 4 == 0 and i != 0: # checks if the current card is the first card in a new row of the game board (every 4 cards)
                board_str += '\n' # adds a new line (so starts a new row in the game board)

            emoji_name = card_info['emoji'] if not card_info['hidden'] else HIDDEN_CARD_PLACEHOLDER # determines the emoji to be displayed based on whether the card is hidden or not
            # if the card is not hidden (hidden is False), it uses the actual emoji from the card information; otherwise, it uses the HIDDEN_CARD_PLACEHOLDER to represent a hidden card
            # this is to avoid player cheating by clicking on cards in the game board and revealing the emoji underneath (this way all they see when cliking is the placeholder, which I set as a white square at the top of this code)
            board_str += f'{emoji_name} ' # adds the current card representation (either emoji or placeholder) to the game board

        try:
            board_message = await self.bot.get_channel(channel_id).send(board_str) # send the constructed board string (the original board)

            self.gamesMM[channel_id]['last_board_message'] = board_message # update the last_board_message in the game data ; stores a reference to the last board message, so the code can later delete that message when a new board is about to be sent

        except discord.errors.NotFound:
            print()

############################################################################

    # Similar to send_board() except it first gets the updated game board state and then sends that updated game board (shows the cards that are flipped, the emojis), and deletes that game boad message for the first flip (to make the game harder)
    async def send_spoiler_board(self, channel_id):
        board = self.gamesMM[channel_id]['board']
        spoiler_board_str = ''
        for i, card_info in enumerate(board):
            if i % 4 == 0 and i != 0:
                spoiler_board_str += '\n'

            emoji_name = card_info['emoji'] if not card_info['hidden'] else HIDDEN_CARD_PLACEHOLDER
            spoiler_board_str += f'{emoji_name} '

        # Send the constructed spoiler board string
        await self.bot.get_channel(channel_id).send(spoiler_board_str)
        if flip_number == 1:
            await self.bot.get_channel(channel_id).purge(limit=1)

############################################################################

    # The results to show after both cards are flipped (win conditions)
    async def check_match(self, ctx):
        flipped_cards = self.gamesMM[ctx.channel.id]['flipped_cards'] # retrieves the flipped cards information from the game data stored in the self.gamesMM dictionary
        board = self.gamesMM[ctx.channel.id]['board'] # retrieves the game board information from the game data stored in the self.gamesMM dictionary

        if board[flipped_cards[0]]['emoji'] == board[flipped_cards[1]]['emoji']: # checks if the emojis of the two flipped cards are the same

            board[flipped_cards[0]]['hidden'] = False # reveal the emoji for the first flipped card
            board[flipped_cards[1]]['hidden'] = False # reveal the emoji for the second flipped card
            await ctx.send('\n**Match found!**')
            self.gamesMM[ctx.channel.id]['flipped_cards'] = [] # resets/clears the list of flipped cards

            # Check if all pairs are found
            if all(not card_info['hidden'] for card_info in board): # checks if all cards on the game board have been successfully matched and revealed
                await ctx.send(f'\n**Congratulations, together you found all pairs and have won! Game over!**')
                del self.gamesMM[ctx.channel.id] # deletes the game data from the dictionary self.gamesMM since the game is concluded and to allow a new game to start fresh
                return # stops the game
            
        else: # not a match
            await ctx.send('\nNo match. Try again!')

            self.bot.loop.create_task(self.delayed_hide(ctx, self.gamesMM[ctx.channel.id]['flipped_cards'][1])) #  hide the second flipped card after a delay
            self.gamesMM[ctx.channel.id]['flipped_cards'] = [] # resets/clears the list of flipped cards
            self.gamesMM[ctx.channel.id]['turn'] = 1 - self.gamesMM[ctx.channel.id]['turn']

        await self.send_board(ctx.channel.id) # sends the updated board with hidden and matched cards

############################################################################

    # Hide the flipped card after the delay
    async def delayed_hide(self, ctx, card_index):
        await asyncio.sleep(1)
        self.gamesMM[ctx.channel.id]['board'][card_index]['hidden'] = True # makes the flipped card hidden
        await self.send_board(ctx.channel.id) # sends the updated game board (with the newly hidden card)

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(Memory_Match(bot)) # name of the Class, look above