# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands
import asyncio
import random

turbotype = 0

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create Turbo_Type Class
class Turbo_Type(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gamesTT = {} # initializing an empty dictionary, which will be used later on to establish a connection between Player 1 (ID) and Player 2 (ID)

    async def cleanup_command_message(self, ctx): # deletes !turbotype message
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass  # ignore errors if the message is not found

# # # Event Listener: Bot on_ready - For when Turbo_Type has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('Turbo_Type has loaded')

# # # Event Listener: Bot on_message - For when a User does !turbotype anywhere, have that message deleted (so the channel doesn't get filled up)
#    @commands.Cog.listener()
#    async def on_message(self, message):
#        if message.content == "!turbotype":
#            await message.delete()

#
# # Command section ############################################################################
#

# # # Command: !turbotype ; Player does !turbotype when he wants to play Turbo Type against someone else. Can be done anywhere. EX: !turbotype
    @commands.before_invoke(cleanup_command_message) # move the command usage of the player to the DMs
    @commands.hybrid_command(name='turbotype', description ='Do this command in any channel to play a private game of Turbo Type against someone else')
    async def turbotype(self, ctx): 
        global turbotype

        if ctx.author.id in self.gamesTT: # user is already in a game
            await ctx.author.send('_ _ \nYou are already playing a game of **Turbo Type**')
            
        elif turbotype == 0: # self.gamesTT should be empty at the start, so this should run fine the first time around ; the game has not been started already and this is the first time a user did !turbotype
            
            turbotype = 1
            original_channel = ctx.channel # store the original channel where the user initatiated !turbotype
            await original_channel.send(f"_ _ \n{ctx.author.mention} wants to start a Turbo Type game! \nWhoever wants to challenge me, do: **!turbotype** in the server: **Heart-to-Heart**")

            try: # waits for the second player to join

                turbotype = 2
                player2_message = await self.bot.wait_for('message', timeout=10, check=lambda m: m.author != ctx.author and (m.content.lower().startswith('!turbotype') or m.content.lower().startswith('/turbotype '))) # player 2 has to join by doing !turbotype or the slash command
                player2 = player2_message.author

                # Associate the two players' IDs with each other, making it easy to find who is playing against whom
                self.gamesTT[ctx.author.id] = player2.id # sets Player 1 to associate with Player 2. EX: if ctx.author.id is cool_man_stu and player2.id is jabroni_jim then self.gamesTT now looks like this: { cool_man_stu: jabroni_jim }
                self.gamesTT[player2.id] = ctx.author.id # sets Player 2 to associate with Player 1. EX: now after adding this line, the dictionary self.gamesTT looks like this: { cool_man_stu: jabroni_jim,  jabroni_jim: cool_man_stu}

                await self.start_turbotype_game(ctx.author, player2, original_channel) # pushes these three arguments into the method and then runs that method

            except asyncio.TimeoutError: # a second user did not do !turbotype within the time limit so didn't join the match in time
                await ctx.author.send('_ _ \nNo one challenged you within 10 seconds. Please do **!turbotype** in the server: **Heart-to-Heart** to try again')
                turbotype = 0

        elif ctx.author.id not in self.gamesTT: # player 1 is spamming !turbotype before player 2 joins. Or, a different user is trying to start a match when one is being played by two other users 
            sent_message = await ctx.author.send('_ _ \nYou already did **!turbotype** so just wait for someone to join; or a match has already started so just wait for that to finish')
            await sent_message.delete(delay=3)

############################################################################

    async def start_turbotype_game(self, player1, player2, channel): # takes in the three arguments created earlier, as parameters
        global turbotype

        await channel.send(f"""_ _ \nThe **Turbo Type** game has now been started. \n\n{player1.mention} is **Player 1** and {player2.mention} is **Player 2**.
                           \nWhen I say "**go**", be the first player to type in and send the word that follows to win.
                           \nReply to me in your **DMs** the word. Good luck to you both!""")

        await player1.send(f"_ _ \nYou're playing Turbo Type against {player2.mention}! \n\nReady, set, go")
        await player2.send(f"_ _ \nYou're playing Turbo Type against {player1.mention}! \n\nReady, set, go")

        possible_word = ["abecedarian", "aberrant", "abhorrence", "abscissa", "absquatulate", "abysmal", "accommodate", "achievement", "acquiesce", "acquisitiveness", "aficionado", "amanuensis", "anathema", "aneurysm", "antediluvian", "apartheid", "aphaeresis", 
                 "apocryphal", "appropriateness", "asterisk", "baccalaureate", "bicuspid", "boutonniere", "borborygmus", "bouillon", "brouhaha", "cacophony", "calisthenics", "callus", "candelabra", "cannoli", "cantankerous", "cappuccino", "caricature", "catachresis", 
                 "cataclysm", "catastrophe", "catharsis", "celerity", "chamomile", "chandelier", "claustrophobia", "clientele", "colloquial", "connoisseur", "conscientious", "convivial", "delineate", "diaphanous", "dirigible", "eclectic", "egregious", "ephemeral", "equanimity", 
                 "espionage", "euonymus", "execrable", "extraneous", "fallacious", "filibuster", "flibbertigibbet", "gazetteer", "garrulous", "gourmand", "gratuitous", "guerdon", "hacienda", "hegemony", "horologium", "hypocritical", "iconoclast", "idiosyncratic", "ignominy", "implacable", 
                 "impuissance", "inchoate", "incontrovertible", "indefatigable", "inexorable", "infallible", "inoculate", "intransigence", "inveigh", "iontophoresis", "irrepressible", "jacquard", "jodhpurs", "jurisprudence", "kanone", "knickknack", "kuchen", "largesse", "lederhosen", "loathsome", 
                 "logarithm", "logorrhea", "maelstrom", "masseuse", "mayonnaise", "millennium", "milieu ", "milquetoast", "mischievous", "mulligatawny", "myrrh", "nadir", "nouveau", "nugatory", "onomatopoeia", "ophthalmologist", "panache", "paraphrasable", "pastiche", "peccadillo", "peripatetic", 
                 "phenomenon", "phlebitis", "picnicking", "pirouette", "poignancy", "posthumous", "preemptory", "psephology", "pseudonym", "ptyalism", "quandary ", "querulous", "questionnaire", "quiescent ", "quixotic ", "rampageous", "rapacious", "raucously", "rendezvous", "restaurateur", 
                 "resuscitate", "rinceau", "sacrilegious", "spontaneity", "streusel", "stupefying", "stymie", "surreptitiously", "susceptible", "synecdoche", "synonymous", "tableau", "tarantula", "terpsichorean", "troubadour", "turpitude", "tutelage", "tyrannical", "ubiquitous", "unconscious", 
                 "undecipherable", "unwarranted", "unwieldiness", "vaccinate", "variegated", "vehement", "vengeance", "veterinarian", "vicissitude", "vigilante", "virtuoso", "whippoorwill", "withhold", "writhe", "zephyr", "zooxanthella", "zucchini"]
        word = random.choice(possible_word)

        word_chars = list(word) # split the word into individual characters

        # Send each character separately with on separate lines so that the players can't just copy and paste the word
        for char in word_chars:
            await player1.send(f"_ _ \n**{char}\u200B**")
            await player2.send(f"_ _ \n**{char}\u200B**")

        await player1.send(f"\nSend the word above first!") # to let the players know that the word has finished beiong spelled out
        await player2.send(f"\nSend the word above first!")

        def check(msg): # check if the message is from either player 1 or player 2
            return msg.author == player1 or msg.author == player2  
  
        try:

            msg = await self.bot.wait_for("message", check=check, timeout=45)

            if msg.author == player1 and msg.content == word: # player 1 sent the right word

                await player1.send(f"_ _ \n**{player1.mention}** typed **{word}** correctly and has **won** the game! \nPlease do **!turbotype** in the server: **Heart-to-Heart** to play again")
                await player2.send(f"_ _ \n**{player1.mention}** typed **{word}** correctly and has **won** the game! \nPlease do **!turbotype** in the server: **Heart-to-Heart** to play again")

            elif msg.author == player1 and msg.content != word: # player 1 sent the wrong word

                await player1.send(f"_ _ \n**{player1.mention}** typed **{word}** incorrectly and has **lost** the game! \nPlease do **!turbotype** in the server: **Heart-to-Heart** to play again")
                await player2.send(f"_ _ \n**{player1.mention}** typed **{word}** incorrectly and has **lost** the game! \nPlease do **!turbotype** in the server: **Heart-to-Heart** to play again")

            elif msg.author == player2 and msg.content == word: # player 2 sent the right word

                await player1.send(f"_ _ \n**{player2.mention}** typed **{word}** correctly and has **won** the game! \nPlease do **!turbotype** in the server: **Heart-to-Heart** to play again")
                await player2.send(f"_ _ \n**{player2.mention}** typed **{word}** correctly and has **won** the game! \nPlease do **!turbotype** in the server: **Heart-to-Heart** to play again")

            elif msg.author == player2 and msg.content != word: # player 2 sent the wrong word

                await player1.send(f"_ _ \n**{player2.mention}** typed **{word}** incorrectly and has **lost** the game! \nPlease do **!turbotype** in the server: **Heart-to-Heart** to play again")
                await player2.send(f"_ _ \n**{player2.mention}** typed **{word}** incorrectly and has **lost** the game! \nPlease do **!turbotype** in the server: **Heart-to-Heart** to play again")

        except asyncio.TimeoutError: # Neither player sent a word in time

            await player1.send(f"_ _ \nNo one guessed **{word}** in time. The game is over. \nPlease do **!turbotype** in the server: **Heart-to-Heart** to try again")
            await player2.send(f"_ _ \nNo one guessed **{word}** in time. The game is over. \nPlease do **!turbotype** in the server: **Heart-to-Heart** to try again")

        turbotype = 0  # reset this variable
        del self.gamesTT[player1.id] # removes Player 1 from the dictionary, in order to empty it
        del self.gamesTT[player2.id] # removes Player 2 from the dictionary, in order to empty it. (It should be empty now)
        return # stop the game

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(Turbo_Type(bot)) # name of the Class, look above