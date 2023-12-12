# 
# # Imports and Cog Setup section ############################################################################
#

import discord
from discord.ext import commands
import asyncio
import random

hangman_running = False
number_of_guesses_done = 0

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create Turbo_Type Class
class Hangman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gamesH = {} # initializing an empty dictionary, which will be used later on to establish a connection between Player 1 (ID) and Player 2 (ID)

# # # Event Listener: Bot on_ready - For when Hangman has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('Hangman has loaded')

 # # # Event Listener: Bot on_message - For when a User does !hangman or !guess - outside the right channel, have that message deleted (so the channel doesn't get filled up)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # ignore messages from bot
        
        if message.content == "!hangman" and message.channel.name != "hangman":
            await message.delete()

#
# # Command section ############################################################################
#

# # # Command: !hangman ; Player does !hangman when he wants to play Hangman in the hangman channel. EX: !hangman
    @commands.hybrid_command(name='hangman', description='Start a Hangman game (go to hangman Channel first)')
    async def hangman(self, ctx):
        global hangman_running
        global possible_word
        global word

       # Makes sure !hangman can only be run in the right channel
        if ctx.channel.name != "hangman": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!hangman** which is specific to the Channel: <#1179207576701915176> Please go there and try it")    
        
        elif ctx.channel.name == "hangman": # the command was done in the correct Channel: hangman

            if hangman_running == True: # player did !hangman but the Game has already started
                await ctx.author.send("A **Hangman** game has already started, so **!hangman** won't do anything. Please go to the Channel: <#1179207576701915176>")
            
            else: # hangman has not been started already, so let it get started and run its logic
                
                hangman_running = True # start the game

                channel = discord.utils.get(ctx.guild.channels, name = "hangman") # makes sure it only looks for users in the Channel: hangman
                members = channel.members

                members_online = [member for member in channel.members if member.status == discord.Status.online and member.name != "Heart-to-Heart Bot"] # online users (excluding bot)

                await ctx.send(f"""_ _ \nThe **Hangman** game has now been started.
                                        \nYou'll type in and send a letter that you think is in the hidden word or you can guess the whole word.
                                        \nThe game goes until the entire word is guessed or you run out of guesses.
                                        \nTake a guess by doing **!guess word** or guess just a letter by doing **!guess -**  
                                        \nGood luck to you all!""")
                
                possible_word = ["able", "about", "account", "acid", "across", "act", "addition", "adjustment", "advertisement", "after", "again", "against", "agreement", "air", "all", "almost", "among", "amount", "amusement", "and", "angle", "angry", "animal", "answer", "ant", "any", "apparatus", "apple", 
                                 "approval", "arch", "argument", "arm", "army", "art", "as", "at", "attack", "attempt", "attention", "attraction", "authority", "automatic", "awake", "baby", "back", "bad", "bag", "balance", "ball", "band", "base", "basin", "basket", "bath", "be", "beautiful", "because", "bed",
                                   "bee", "before", "behaviour", "belief", "bell", "bent", "berry", "between", "bird", "birth", "bit", "bite", "bitter", "black", "blade", "blood", "blow", "blue", "board", "boat", "body", "boiling", "bone", "book", "boot", "bottle", "box", "boy", "brain", "brake", "branch", 
                                   "brass", "bread", "breath", "brick", "bridge", "bright", "broken", "brother", "brown", "brush", "bucket", "building", "bulb", "burn", "burst", "business", "but", "butter", "button", "by", "cake", "camera", "canvas", "card", "care", "carriage", "cart", "cat", "cause", 
                                   "certain", "chain", "chalk", "chance", "change", "cheap", "cheese", "chemical", "chest", "chief", "chin", "church", "circle", "clean", "clear", "clock", "cloth", "cloud", "coal", "coat", "cold", "collar", "colour", "comb", "come", "comfort", "committee", "common", "company",
                                     "comparison", "competition", "complete", "complex", "condition", "connection", "conscious", "control", "cook", "copper", "copy", "cord", "cork", "cotton", "cough", "country", "cover", "cow", "crack", "credit", "crime", "cruel", "crush", "cry", "cup", "cup", "current", 
                                     "curtain", "curve", "cushion", "damage", "danger", "dark", "daughter", "day", "dead", "dear", "death", "debt", "decision", "deep", "degree", "delicate", "dependent", "design", "desire", "destruction", "detail", "development", "different", "digestion", "direction", "dirty",
                                       "discovery", "discussion", "disease", "disgust", "distance", "distribution", "division", "do", "dog", "door", "doubt", "down", "drain", "drawer", "dress", "drink", "driving", "drop", "dry", "dust", "ear", "early", "earth", "east", "edge", "education", "effect", "egg", 
                                       "elastic", "electric", "end", "engine", "enough", "equal", "error", "even", "event", "ever", "every", "example", "exchange", "existence", "expansion", "experience", "expert", "eye", "face", "fact", "fall", "false", "family", "far", "farm", "fat", "father", "fear", 
                                       "feather", "feeble", "feeling", "female", "fertile", "fiction", "field", "fight", "finger", "fire", "first", "fish", "fixed", "flag", "flame", "flat", "flight", "floor", "flower", "fly", "fold", "food", "foolish", "foot", "for", "force", "fork", "form", "forward", 
                                       "fowl", "frame", "free", "frequent", "friend", "from", "front", "fruit", "full", "future", "garden", "general", "get", "girl", "give", "glass", "glove", "go", "goat", "gold", "good", "government", "grain", "grass", "great", "green", "grey", "grip", "group", "growth", 
                                       "guide", "gun", "hair", "hammer", "hand", "hanging", "happy", "harbour", "hard", "harmony", "hat", "hate", "have", "he", "head", "healthy", "hear", "hearing", "heart", "heat", "help", "high", "history", "hole", "hollow", "hook", "hope", "horn", "horse", "hospital", 
                                       "hour", "house", "how", "humour", "I", "ice", "idea", "if", "ill", "important", "impulse", "in", "increase", "industry", "ink", "insect", "instrument", "insurance", "interest", "invention", "iron", "island", "jelly", "jewel", "join", "journey", "judge", "jump", "keep", 
                                       "kettle", "key", "kick", "kind", "kiss", "knee", "knife", "knot", "knowledge", "land", "language", "last", "late", "laugh", "law", "lead", "leaf", "learning", "leather", "left", "leg", "let", "letter", "level", "library", "lift", "light", "like", "limit", "line", 
                                       "linen", "lip", "liquid", "list", "little", "living", "lock", "long", "look", "loose", "loss", "loud", "love", "low", "machine", "make", "male", "man", "manager", "map", "mark", "market", "married", "mass", "match", "material", "may", "meal", "measure", "meat", "medical",
                                         "meeting", "memory", "metal", "middle", "military", "milk", "mind", "mine", "minute", "mist", "mixed", "money", "monkey", "month", "moon", "morning", "mother", "motion", "mountain", "mouth", "move", "much", "muscle", "music", "nail", "name", "narrow", "nation", 
                                         "natural", "near", "necessary", "neck", "need", "needle", "nerve", "net", "new", "news", "night", "no", "noise", "normal", "north", "nose", "not", "note", "now", "number", "nut", "observation", "of", "off", "offer", "office", "oil", "old", "on", "only", "open", 
                                         "operation", "opinion", "opposite", "or", "orange", "order", "organization", "ornament", "other", "out", "oven", "over", "owner", "page", "pain", "paint", "paper", "parallel", "parcel", "part", "past", "paste", "payment", "peace", "pen", "pencil", "person", "physical", 
                                         "picture", "pig", "pin", "pipe", "place", "plane", "plant", "plate", "play", "please", "pleasure", "plough", "pocket", "point", "poison", "polish", "political", "poor", "porter", "position", "possible", "pot", "potato", "powder", "power", "present", "price", "print", 
                                         "prison", "private", "probable", "process", "produce", "profit", "property", "prose", "protest", "public", "pull", "pump", "punishment", "purpose", "push", "put", "quality", "question", "quick", "quiet", "quite", "rail", "rain", "range", "rat", "rate", "ray", 
                                         "reaction", "reading", "ready", "reason", "receipt", "record", "red", "regret", "regular", "relation", "religion", "representative", "request", "respect", "responsible", "rest", "reward", "rhythm", "rice", "right", "ring", "river", "road", "rod", "roll", "roof", 
                                         "room", "root", "rough", "round", "rub", "rule", "run", "sad", "safe", "sail", "salt", "same", "sand", "say", "scale", "school", "science", "scissors", "screw", "sea", "seat", "second", "secret", "secretary", "see", "seed", "seem", "selection", "self", "send", "sense",
                                           "separate", "serious", "servant", "sex", "shade", "shake", "shame", "sharp", "sheep", "shelf", "ship", "shirt", "shock", "shoe", "short", "shut", "side", "sign", "silk", "silver", "simple", "sister", "size", "skin", "skirt", "sky", "sleep", "slip", "slope", "slow", 
                                           "small", "smash", "smell", "smile", "smoke", "smooth", "snake", "sneeze", "snow", "so", "soap", "society", "sock", "soft", "solid", "some", "son", "song", "sort", "sound", "soup", "south", "space", "spade", "special", "sponge", "spoon", "spring", "square", "stage", 
                                           "stamp", "star", "start", "statement", "station", "steam", "steel", "stem", "step", "stick", "sticky", "stiff", "still", "stitch", "stocking", "stomach", "stone", "stop", "store", "story", "straight", "strange", "street", "stretch", "strong", "structure", "substance",
                                             "such", "sudden", "sugar", "suggestion", "summer", "sun", "support", "surprise", "sweet", "swim", "system", "table", "tail", "take", "talk", "tall", "taste", "tax", "teaching", "tendency", "test", "than", "that", "the", "then", "theory", "there", "thick", "thin", 
                                             "thing", "this", "thought", "thread", "throat", "through", "through", "thumb", "thunder", "ticket", "tight", "till", "time", "tin", "tired", "to", "toe", "together", "tomorrow", "tongue", "tooth", "top", "touch", "town", "trade", "train", "transport", "tray", "tree",
                                               "trick", "trouble", "trousers", "true", "turn", "twist", "umbrella", "under", "unit", "up", "use", "value", "verse", "very", "vessel", "view", "violent", "voice", "waiting", "walk", "wall", "war", "warm", "wash", "waste", "watch", "water", "wave", "wax", "way", 
                                               "weather", "week", "weight", "well", "west", "wet", "wheel", "when", "where", "while", "whip", "whistle", "white", "who", "why", "wide", "will", "wind", "window", "wine", "wing", "winter", "wire", "wise", "woman", "wood", "wool", "word", "work", "worm", "wound", 
                                               "writing", "wrong", "year", "yellow", "yes", "yesterday", "you", "young"]
                word = random.choice(possible_word) # the word the player has to guess

                word_length = len(word)
                global max_guesses
                max_guesses = word_length + 1
                await ctx.channel.send(f"The word (delete this later): {word}")
                await ctx.channel.send(f"_ _ \nThe word to guess has **{word_length}** letters in it, so you have **{max_guesses} tries** to guess the word") # lets the player know the length of the word they have to guess and how many tries to get the whole word right

############################################################################
    
    # Global variables to store game state
    word_progress = ""
    players_guesses = []

# # # Command: !guess - ; Player does !guess - to guess a letter or the entire word in the hangman channel. EX: !guess k
    @commands.hybrid_command(name='guess', description='Guess a letter or the entire word. EX: !guess k')
    async def guess(self, ctx, guess: str):
        global hangman_running
        global possible_word
        global word
        global max_guesses
        global number_of_guesses_done
        global guesses_left
        global word_progress
        global players_guesses

        # Makes sure !guess can only be run in the right channel 
        if ctx.channel.name != "hangman": # has to be ctx.channel.name (not ctx.channel)
            await ctx.author.send(f"It looks like you have tried to do the command: **!guess -** which is specific to the Channel: <#1179207576701915176> Please go there and try it")

        elif ctx.channel.name == "hangman": # the command was done in the correct Channel: hangman
                
            if not hangman_running: # if the game is not running
                
                await ctx.send("Hold your horses, Hangman hasn't started yet, so **!guess -** won't do anything. If you would like to play, do **!hangman** to start a game first")

                return 

            players_guesses = list() # a list of everything the players guessed so far
            guess = guess.lower() # make the players' guess lowercase
            word_progress = "" # shows the progress of guessing the word right that the players did
            
            if number_of_guesses_done == 0: # first time doing !guess
                guesses_left = max_guesses # starts off as what was decided when first did !hangman (1 more than the word)
                guesses_left -= 1 # then lowers it by 1, since someone guessed

            else: # not the first time doing !guess
                guesses_left -= 1 # lowers how many guesses/tries the players have after a player has guessed
                                   
            # Builds the string word_progress which represents the progress of the players in guessing the word. It reveals the correctly guessed letters and hides the yet-to-be-guessed letters with underscores
            for c in word.lower(): # iterates over each character in the word

                if guess == c or c in players_guesses: # the players' guess is equal to a character in the word or if the players' guess has already been guessed
                    word_progress += c + " " # adds players' guess (character) to word_progress and then a space after it so that formatting doesn't get messed up

                else:
                    word_progress += "\_ " # the players' guess doesn't equal a character in the word so put a _ 
            
            players_guesses.append(guess) # adds players' guess to the list of guesses

            number_of_guesses_done += 1 # increase this so that you can lower the guesses_left

            if guesses_left < 0: # final word logic finished incorrectly (player did !guess or slash command instead of sending the final guess directly)
                
                # Reset game state
                    players_guesses = list() # resets the players' guesses
                    hangman_running = False
                    max_guesses = 0
                    guesses_left = 0
                    number_of_guesses_done = 0

                    return

            if guess == word: # players guessed the whole word correctly
                
                await ctx.send(f"_ _ \nYou guessed the word correctly so now you've won the game! \nPlease do **!hangman** to play again")
                players_guesses = list() # resets the players' guesses
                hangman_running = False # resets the game's state
                max_guesses = 0
                guesses_left = 0
                number_of_guesses_done = 0

                return

            else: # player guessed the whole word wrong
                
                if guesses_left > 0:
                    
                    await ctx.channel.send("Progress: %s" % word_progress) # show players' progress so far
                    # %s is a placeholder for a string in the format string. It tells Python to expect a string value at this position
                    # % is a formatting syntax that indicates the string should be formatted with the value following the %. In this case, the %s will be replaced with the actual string value
                    # The same as doing (f"Progress: {word_progress}"")

                    guesses_str = ",".join(players_guesses) # separates the player's guesses with a , 
                    await ctx.channel.send(f"Guesses so far: **{guesses_str}**") # show players' guesses so far

                    await ctx.channel.send(f"Number of tries left: **{guesses_left}**") # show how many guesses the players have left

            # Final guess logic
            if guesses_left == 0:

                await ctx.channel.send("_ _ \nYou have run out of tries. \nGuess the whole word now (don't do **!guess**, just send what you think the word is). \nYou have **20** seconds to guess")
                
                try:
                    
                    # Allow one final chance to guess the entire word
                    final_guess = await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20)
                    final_guess_content = final_guess.content.lower().strip()
                    
                    if final_guess_content == word: # player guessed the word correctly
                        await ctx.channel.send(f"_ _ \nYou guessed the word correctly in your final attempt and have won the game! \nPlease do **!hangman** to play again")

                    else: # player guessed the word wrong
                        await ctx.channel.send(f"Sorry, your final guess **{final_guess_content}** was incorrect so now you lost the game. The word was **{word}**. \nPlease do **!hangman** to play again")

                    # Reset game state
                    players_guesses = list() # resets the players' guesses
                    hangman_running = False
                    max_guesses = 0
                    guesses_left = 0
                    number_of_guesses_done = 0

                    return
                
                except asyncio.TimeoutError: # player took more than 20 seconds to guess
                    await ctx.channel.send(f"Sorry, you took too long to guess. The word was **{word}**. \nPlease do **!hangman** to play again")

                    # Reset game state
                    players_guesses = list() # resets the players' guesses
                    hangman_running = False
                    max_guesses = 0
                    guesses_left = 0
                    number_of_guesses_done = 0

                    return
                
            if guesses_left < 0:
                await ctx.channel.send("_ _ \nI told you not to do **!guess**")


###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(Hangman(bot))