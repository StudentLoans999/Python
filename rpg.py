#RPG (Pokemon 1v1 adventure)

#Single Player - do it like Fallout where character is given but Player chooses what stats to level up, which all start at 1 and can go up to 10: luck (critical hits), health, agility (makes monster more likely to miss), stength (damage), mana (needed for magic).

#All done through DMs with the bot, not tied down to any channel. After player sets up their character, they do 1 v 1 battles against randomly generated enemies (random stats within ranges based on the zone).
#So Level 1 Player fights against Zone 1 enemies (level 1 with level 1 stats) until player decides to go to Zone 2 and then fights level 2 enemies.

#The game goes until the player dies (reset back to character creation and then zone 1). Game over message mentions their current level and stats (so they can share it with others), the zone they died in, and how many times they fleed.

#Each defeated monster gives the player a random narrow range of gold earned (based on monster's level).
#Player also gets XP based on level of monster killed.

#Player can visit an item shop in between fights, to buy mana and health potions using their gold.
#Player can also choose to advance a Zone in between fights, but they can never choose to go down a Zone 

#During the battle, the player has these options: physical attack, magic attack, Use item, flee.
#If the player flees, then they are sent back to Zone 1, yet each time the player flees, all the monster stats get buffed a level. So the first time the player flees and starts fighting enemies in Zone 1 they actually are like Zone 2 monster where they have level 2 stats. But same with xp and gold #gained. The point of this is to encourage the player to grind at a zone they're comfortable with but also the riskier they are by going to a higher zone, the more rewards, but if they can't handle it they have to start on the bottom and are punished for it.

# 
# # Imports and Cog Setup section ############################################################################
#

from typing import Any
import discord
from discord.ext import commands
import asyncio
from discord.ui import select, View
import random

hero_currentlevel = 1
hero_maxlevel = 44

hero_currenthealth = 100
hero_totalhealth = 100
hero_currentmana = 100
hero_totalmana = 100
hero_currentluck = 1
hero_currentstrength = 1
hero_currentagility = 1
hero_currentxp = 0
hero_currentgold = 0

hero_stat_points = 1
hero_stat_currenthealth = 1
hero_stat_totalhealth = 10
hero_stat_currentmana = 1
hero_stat_totalmana = 10        
hero_stat_currentluck = 1       
hero_stat_totalluck = 10
hero_stat_currentstrength = 1
hero_stat_totalstrength = 10
hero_stat_currentagility = 1
hero_stat_totalagility = 10

hero_currentzone = 1
hero_name = ""

hero_healthpotions = 1
hero_manapotions = 1

monster_currentlevel = 1
monster_currenthealth = 0
monster_totalhealth = 0
monster_currentluck = 1
monster_currentstrength = 1
monster_currentagility = 1 

monster_hero_flee_currentzone = 1
monster_maxlevel = 100
monster_name = ""
possible_monster_name = ["Brinecat, The Twin Mutant", "Abysstalon, The Venom Feline", "Brineling, The Primeval Mutant", "Vapormutant, The Venom Mutant", "Emberword, The Silver Critter", "Grossmutant, The Silver Man", "Grossbug, The Quiet Monster", "Germeyes, The Rotten Serpent",
"Brinebeast, The Evasive Tumor", "Soilface, The Nightmare Man", "Brineface, The Nightmare Gorilla", "Emberbug, The Evasive Cobra", "Curseword, The Twin Dog", "Cursefigure, The Nightmare Woman", "Soilword, The Big Bad Feline", "Emberface, The Needy Critter", "Ghosteyes, The Rotten Woman",
"Vaporface, The Silver Tumor", "Webmutant, The Venom Cobra", "Germface, The Raptor Mutant", "Vaporman, The Needy Mutant", "Webfigure, The Bruised Woman", "Brineface, The Quiet Dog", "Deadmutant, The Quiet Hound", "Cursetalon, The Quiet Gorilla", "Soilface, The Bruised Hound",
"Germword, The Venom Serpent", "Brineeyes, The Rotten Woman", "Webtalon, The Nightmare Monster", "Ghostfigure, The Silver Tumor", "Deadling, The Big Bad Monster", "Deadmutant, The Rotten Feline", "Brineword, The Venom Man", "Brineeyes, The Bruised Gorilla", "Germtalon, The Bruised Gorilla",
"Deadbeast, The Silver Gorilla", "Germtalon, The Nightmare Man", "Germtalon, The Evasive Cobra", "Deadfigure, The Silver Feline", "Soilface, The Primeval Monster", "Cursefigure, The Quiet Dog", "Grosswing, The Twin Monster", "Decayman, The Twin Tumor", "Abyssbug, The Raptor Gorilla",
"Cursecat, The Needy Gorilla", "Abyssman, The Silver Hound", "Abysstalon, The Needy Monster", "Ghostcat, The Raptor Hound", "Grosscat, The Rotten Dog", "Vaportalon, The Big Bad Serpent", "Emberman, The Raptor Mutant", "Soilling, The Primeval Monster", "Grossman, The Quiet Woman",
"Deadwing, The Raptor Woman", "Ghostbug, The Twin Woman", "Germword, The Bruised Hound", "Soilfigure, The Twin Serpent", "Deadeyes, The Rotten Dog", "Soilbug, The Primeval Hound", "Ghostling, The Needy Mutant", "Curseman, The Evasive Critter", "Soilling, The Twin Man", 
"Brinetalon, The Big Bad Mutant", "Germman, The Primeval Man", "Vaportalon, The Nightmare Cobra", "Deadling, The Twin Man", "Deadfigure, The Venom Dog", "Germbeast, The Twin Monster", "Brinebeast, The Quiet Woman", "Decayface, The Venom Serpent", "Vaportalon, The Venom Man", 
"Deadcat, The Evasive Tumor", "Grossbug, The Rotten Gorilla", "Decayman, The Quiet Serpent", "Soilbeast, The Silver Hound", "Grossfigure, The Quiet Mutant", "Decayeyes, The Primeval Monster", "Deadwing, The Needy Cobra", "Emberfigure, The Nightmare Man", "Decaywing, The Primeval Feline",
"Soilface, The Nightmare Feline", "Ghostmutant, The Big Bad Monster", "Brineface, The Evasive Critter", "Embertalon, The Venom Tumor", "Deadeyes, The Quiet Cobra", "Decaycat, The Needy Mutant", "Decayman, The Rotten Cobra", "Ghostfigure, The Primeval Hound", "Brinemutant, The Rotten Woman",
"Abyssman, The Evasive Man", "Decaytalon, The Bruised Gorilla", "Decaymutant, The Needy Man", "Webman, The Quiet Feline", "Grossfigure, The Needy Woman", "Webeyes, The Evasive Feline", "Deadeyes, The Primeval Critter", "Emberbug, The Nightmare Man", "Soilling, The Raptor Tumor",
"Grossfigure, The Venom Dog", "Ghostling, The Raptor Monster", "Abyssling, The Evasive Dog", "Vaporfigure, The Primeval Woman", "Vaporfigure, The Needy Critter", "Vaporcat, The Rotten Feline", "Soilbeast, The Silver Gorilla", "Emberbug, The Bruised Gorilla", "Webtalon, The Silver Serpent",
"Germbug, The Twin Dog", "Germword, The Nightmare Gorilla", "Abyssfigure, The Quiet Feline", "Cursetalon, The Rotten Tumor", "Brinefigure, The Twin Feline", "Emberling, The Bruised Tumor", "Cursewing, The Raptor Critter", "Emberbeast, The Quiet Hound", "Curseling, The Big Bad Cobra",
"Ghostbeast, The Bruised Cobra", "Abyssfigure, The Evasive Cobra", "Brinewing, The Silver Feline", "Decayling, The Primeval Monster", "Cursefigure, The Needy Serpent", "Webword, The Nightmare Critter", "Embertalon, The Raptor Woman", "Embereyes, The Big Bad Monster", 
"Abyssling, The Big Bad Man", "Ghostling, The Nightmare Serpent", "Curseface, The Nightmare Dog", "Emberling, The Bruised Serpent", "Vaporwing, The Raptor Cobra", "Cursetalon, The Venom Hound", "Embercat, The Rotten Woman", "Ghostbug, The Primeval Monster", "Abyssling, The Silver Serpent",
"Germbug, The Silver Dog", "Grossfigure, The Silver Dog", "Embertalon, The Quiet Monster", "Curseman, The Raptor Man", "Brinecat, The Evasive Critter", "Cursefigure, The Silver Critter", "Brinetalon, The Twin Woman", "Cursebeast, The Nightmare Critter", "Cursemutant, The Evasive Mutant",
"Ghostwing, The Nightmare Woman", "Webbug, The Raptor Gorilla", "Cursefigure, The Venom Mutant", "Deadword, The Evasive Tumor", "Vaporeyes, The Silver Monster", "Brineeyes, The Raptor Mutant", "Vaporwing, The Needy Gorilla", "Vaporling, The Silver Cobra", "Deadface, The Needy Monster",
"Ghostmutant, The Twin Mutant", "Deadbug, The Raptor Dog", "Germling, The Bruised Gorilla", "Decayfigure, The Big Bad Critter", "Deadman, The Needy Woman", "Emberwing, The Quiet Man", "Grossbeast, The Twin Tumor", "Webword, The Bruised Feline", "Vaporbeast, The Big Bad Mutant",
"Ghosteyes, The Needy Tumor", "Germcat, The Nightmare Woman", "Germling, The Primeval Critter", "Germbug, The Rotten Mutant", "Decaybeast, The Raptor Serpent", "Deadfigure, The Raptor Gorilla", "Brineman, The Primeval Feline", "Webface, The Needy Hound", "Vaporface, The Rotten Woman",
"Webbeast, The Venom Man", "Decaymutant, The Primeval Critter", "Ghostwing, The Rotten Mutant", "Embercat, The Big Bad Feline", "Brineling, The Raptor Hound", "Curseeyes, The Rotten Hound", "Vaporeyes, The Raptor Man", "Soilbeast, The Nightmare Critter", "Grossfigure, The Primeval Gorilla",
"Deadfigure, The Quiet Critter", "Vaporfigure, The Bruised Woman", "Webling, The Twin Feline", "Soilword, The Raptor Feline", "Brinebeast, The Twin Cobra", "Ghostcat, The Silver Woman", "Vaporling, The Big Bad Man", "Ghostbeast, The Twin Mutant", "Deadeyes, The Silver Feline", 
"Vaporbug, The Rotten Mutant", "Decaybeast, The Rotten Cobra", "Grossling, The Twin Critter", "Decayface, The Quiet Tumor", "Ghostman, The Quiet Tumor", "Emberword, The Bruised Hound", "Grossfigure, The Primeval Tumor", "Ghostman, The Venom Critter", "Brineling, The Evasive Tumor",
"Germmutant, The Big Bad Mutant", "Emberbug, The Nightmare Hound", "Vapormutant, The Silver Tumor", "Abysstalon, The Raptor Dog", "Webeyes, The Big Bad Dog", "Soilbug, The Rotten Hound", "Vaporman, The Quiet Man", "Soilling, The Evasive Critter", "Grosseyes, The Evasive Woman", 
"Soileyes, The Quiet Gorilla", "Ghostman, The Quiet Gorilla", "Grosseyes, The Primeval Man", "Grosswing, The Quiet Serpent", "Brineface, The Bruised Dog", "Brineword, The Quiet Feline", "Germmutant, The Needy Woman", "Grosswing, The Primeval Woman", "Germbeast, The Rotten Hound",
"Emberman, The Raptor Woman", "Brineman, The Twin Man", "Vaporword, The Silver Hound", "Goolops, The Young Pest", "Youngly, The Rainbow Mutant", "Gloomlops, The Flamed Mutant", "Doomboo, The Crying Doll", "Goopaw, The Young Fiend", "Acidgirl, The Icy Snake", "Muckga, The Night Worm",
"Smogfang, The Young Babbler", "Poogirl, The Icy Pest", "Mucktree, The Sunshine Spider", "Gooloo, The Cute Bat", "Moongirl, The Scared Monkey", "Smogboy, The Scared Cub", "Ewwga, The Cute Child", "Gooboo, The Scared Worm", "Ewwpaw, The Cursed Cub", "Dreamgirl, The Crying Spirit",
"Gloomboy, The Cursed Babbler", "Moontree, The Young Spider", "Mucklops, The Young Mutant", "Dreamlu, The Flamed Kitten", "Youngga, The Young Kitten", "Gloomtree, The Furry Glob", "Ashboo, The Rainbow Spider", "Moonlu, The Cute Pest", "Gloomfang, The Sunshine Spirit", "Gooling, The Crying Alien"
"Dreamlops, The Young Spirit", "Gloomfang, The Young Monster", "Doomfang, The Cute Cub", "Ashfang, The Icy Babbler", "Doomlops, The Cute Monster", "Dreamga, The Night Kitten", "Muckfang, The Scared Glob", "Goolops, The Cursed Spirit", "Pooly, The Young Monkey", "Muckboo, The Rainbow Blob",
"Mucklops, The Furry Spirit", "Mucklu, The Flamed Snake", "Moonlops, The Sunshine Doll", "Poolu, The Bright Worm", "Youngling, The Cursed Kitten", "Moonling, The Furry Cub", "Youngfang, The Baby Fiend", "Doompaw, The Baby Glob", "Ewwlops, The Crying Child", "Smogga, The Cursed Cub",
"Ewwloo, The Young Monkey", "Pooboo, The Scared Doll", "Moonboo, The Cursed Cub", "Mucktree, The Furry Monkey", "Dreamling, The Baby Alien", "Gloomlu, The Crying Blob", "Ashpaw, The Night Alien", "Gloomloo, The Baby Glob", "Dreampaw, The Sunshine Snake", "Dreamfang, The Flamed Kitten",
"Gloomboy, The Furry Cub", "Gloomgirl, The Scared Babbler", "Ewwpaw, The Scared Babbler", "Ewwgirl, The Scared Spider", "Moonfang, The Icy Monster", "Gootree, The Sunshine Babbler", "Moonloo, The Crying Worm", "Smogpaw, The Baby Spirit", "Ewwgirl, The Bright Child", "Ashfang, The Cute Child",
"Ewwga, The Rainbow Monkey", "Ewwboo, The Crying Babbler", "Youngfang, The Furry Fiend", "Muckfang, The Baby Pest", "Youngboy, The Cute Cub", "Ashling, The Night Alien", "Pooboo, The Night Monster", "Ashtree, The Cute Pest", "Ewwpaw, The Furry Snake", "Gloomfang, The Flamed Child",
"Youngga, The Crying Bat", "Pooly, The Young Fiend", "Ashga, The Crying Alien", "Youngpaw, The Sunshine Babbler", "Dreamtree, The Rainbow Child", "Gooloo, The Cute Pest", "Acidly, The Baby Fiend", "Youngly, The Young Monkey", "Gloomboo, The Furry Pest", "Smogfang, The Scared Spider"] 

###############################################################################################################################################################################################################

#
# # Event Listener section ############################################################################
#

# # # Create RPG Class
class RPG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gamesRPG = {} # initializing a dictionary to store the game session (state)
        self.hero_stat_points = {} # initialize hero_stat_points as a class attribute

    async def cleanup_command_message(self, ctx): # deletes !rpg message
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass  # ignore errors if the message is not found

# # # Event Listener: Bot on_ready - For when RPG has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('RPG has loaded')
    
#
# # Command section ############################################################################
#

# # # Command: !rpg ; Player does !rpg when he wants to play RPG. Can be done anywhere. EX: !rpg
    @commands.before_invoke(cleanup_command_message) # move the command usage of the player to the DMs
    @commands.hybrid_command(name='rpg', description = 'Do this command in any channel to play a private RPG game')
    async def rpg(self, ctx):

        if ctx.author.id in self.gamesRPG: # user is already in a game
            await ctx.author.send('_ _ \nA **RPG** game is already in progress for you')
            return

        self.gamesRPG[ctx.author.id] = True # add the user to the games dictionary

        # Initalize variables
        global hero_currentlevel

        global hero_currenthealth
        global hero_totalhealth
        global hero_currentmana
        global hero_totalmana
        global hero_currentluck
        global hero_currentstrength
        global hero_currentagility
        global hero_currentxp
        global hero_currentgold

        global hero_stat_points
        global hero_stat_currenthealth
        global hero_stat_totalhealth
        global hero_stat_currentmana
        global hero_stat_totalmana     
        global hero_stat_currentluck    
        global hero_stat_currentstrength
        global hero_stat_currentagility

        global hero_currentzone
        global hero_name

        global hero_healthpotions
        global hero_manapotions

        global monster_currentlevel
        global monster_currenthealth
        global monster_totalhealth
        global monster_currentluck
        global monster_currentstrength
        global monster_currentagility

        global monster_hero_flee_currentzone
        global monster_name
        global possible_monster_name

# # Start game & Give Name section ############################################################################

        await ctx.author.send(f"""_ _ \nWelcome to the **RPG** game. Let's get started with you setting up your character by choosing your name and stats.
                                \nThen the game will begin with you entering Zone {hero_currentzone} and battling around Level {monster_currentlevel} enemies for experience and gold.
                                \nBattle tougher enemies by advancing to the next zone. These higher level enemies give you more experience and gold when defeated compared to enemies from lower zones.
                                \nTry to make it to the highest zone as you can before being defeated!
                                \nSo, let's get started. What would you would like to be called?""")
        
        sent_DM_message = await ctx.send(f"{ctx.author.mention} Check your DMs since that's where you'll play the game") # let the player know to continue the game in their DMs

        try: # delete !rpg that player did outside of the DMs and also delete the bot's message saying to check DMs

            await asyncio.gather(
                sent_DM_message.delete(delay=5),
                ctx.message.delete()
            )

        except discord.NotFound:
            pass  # ignore NotFound error if the message was already deleted

        hero_name = await self.get_hero_name(ctx) # bot gives player an input (asking for their name) (see get_hero_name method below)

# # Set Hero Stats section ############################################################################

        if hero_name: # the player input their name

            await ctx.author.send(f"""\nNice to meet you, **{hero_name}**! 
                                  \nNow that we have gotten acquainted, let's see your current stats.
                                  \n **Health** : **{hero_currenthealth}**/**{hero_totalhealth}**
                                  \n **Mana**: **{hero_currentmana}**/**{hero_totalmana}**
                                  \n **Luck**: **{hero_currentluck}**
                                  \n **Strength**: **{hero_currentstrength}**
                                  \n **Agility**: **{hero_currentagility}**
                                  \nYou are **Level {hero_currentlevel}** and you have **{hero_stat_points}** point to increase a stat by a level.
                                  \nYou will earn a point each time you level up.
                                  \nBut for now, let's spend that point now to upgrade your character!""")
            
            class get_hero_stats(View): # update stats input (will be used when hero levels up)
                def __init__(self, rpg_cog):
                    super().__init__()

                    self.rpg_cog = rpg_cog  # store the rpg_cog as an attribute

                @discord.ui.select(
                    placeholder="Choose a stat to update",
                    options=[
                        discord.SelectOption(label="Health (Capacity)", value="1", description=f"Currently: {hero_stat_currenthealth}/{hero_stat_totalhealth}"),
                        discord.SelectOption(label="Mana (Capacity and Damage)", value="2", description=f"Currently: {hero_stat_currentmana}/{hero_stat_totalmana}"),
                        discord.SelectOption(label="Luck (More likely to do a Critical Hit)", value="3", description=f"Currently: {hero_stat_currentluck}"),
                        discord.SelectOption(label="Strength (Physical Attack Damage)", value="4", description=f"Currently: {hero_stat_currentstrength}"),
                        discord.SelectOption(label="Agility (Makes Monster miss their Physical Attack more)", value="5", description=f"Currently: {hero_stat_currentagility}")
                    ]
                )

                async def select_callback(self, interaction, select):
                    global hero_stat_points
                    global hero_stat_currenthealth
                    global hero_stat_currentmana
                    global hero_stat_currentluck
                    global hero_stat_currentstrength
                    global hero_stat_currentagility
                    global hero_currenthealth
                    global hero_totalhealth
                    global hero_currentmana
                    global hero_totalmana
                    global hero_currentluck
                    global hero_currentstrength
                    global hero_currentagility
                    global monster_currentlevel
                    global monster_currenthealth
                    global monster_totalhealth
                    global monster_currentluck
                    global monster_currentstrength
                    global monster_currentagility

                    select.disabled=True

                    if select.values[0] == "1": # chose to update Health stat, so increase hero's total health

                        hero_stat_currenthealth += 1
                        hero_totalhealth += 10
                        hero_currenthealth += 10
                        await interaction.response.send_message(f"You have increased your **Health** and it is now **{hero_currenthealth}**/**{hero_totalhealth}**", ephemeral=True)
                        
                    elif select.values[0] == "2": # chose to update Mana stat, so increase hero's total mana

                        hero_stat_currentmana += 1
                        hero_totalmana += 10
                        hero_currentmana += 10
                        await interaction.response.send_message(f"You have increased your **Mana** and it is now **{hero_currentmana}**/**{hero_totalmana}**", ephemeral=True)

                    elif select.values[0] == "3": # chose to update Luck stat, so increase hero's current luck

                        hero_stat_currentluck += 1
                        hero_currentluck += 1
                        await interaction.response.send_message(f"You have increased your **Luck** and it is now **{hero_currentluck}**", ephemeral=True)

                    elif select.values[0] == "4": # chose to update Strength stat, so increase hero's current strength

                        hero_stat_currentstrength += 1
                        hero_currentstrength += 1
                        await interaction.response.send_message(f"You have increased your **Strength** and it is now **{hero_currentstrength}**", ephemeral=True)

                    elif select.values[0] == "5": # chose to update Agility stat, so increase hero's current agility

                        hero_stat_currentagility += 1
                        hero_currentagility += 1
                        await interaction.response.send_message(f"You have increased your **Agility** and it is now **{hero_currentagility}**", ephemeral=True)
                        
                    hero_stat_points -= 1 # player spent their stat point
                    self.stop() # makes the player not be able to change their dropdown selection

                    await ctx.author.send(f"""\nOkay, so you have set your stat levels to be:
                                        \n **Health** (Capacity): **{hero_stat_currenthealth}** out of **{hero_stat_totalhealth}**
                                        \n **Mana** (Capacity and Damage): **{hero_stat_currentmana}** out of **{hero_stat_totalmana}**
                                        \n **Luck** (More likely to do a Critical Hit): **{hero_stat_currentluck}** out of **{hero_stat_totalluck}**
                                        \n **Strength** (Physical Attack Damage): **{hero_stat_currentstrength}** out of **{hero_stat_totalstrength}**
                                        \n **Agility** (Makes Monster miss their Physical Attack more): **{hero_stat_currentagility}** out of **{hero_stat_totalagility}**
                                        """)
                    
# # Zone 1 section ############################################################################

                    await ctx.author.send(f"_ _ \nNow you are ready to fight! \n\n So you enter **Zone {hero_currentzone}**")
                    
                    audio_zone = 'C:\IT\DiscordBot\Zone.mp3'
                    await ctx.author.send(file=discord.File(audio_zone)) # sends an audio file
                    
                    monster_currentlevel = random.randint(1, 3)
                    monster_name = random.choice(possible_monster_name)
                    await ctx.author.send(f"_ _ \nMonster found! \n\nYou will fight: **{monster_name}** **(Level {monster_currentlevel})**") # makes the monster's level a random between 1-3 and a random name from the long list of names
                    
                    audio_monsterspotted = 'C:\IT\DiscordBot\MonsterSpotted.mp3'
                    await ctx.author.send(file=discord.File(audio_monsterspotted)) # sends an audio file
                    
                    def generate_range(level, multiplier=10): # defines a function to generate a range for a given level with a specified multiplier ; gives a specified range for each of the monster's stats, based on the monster's level
                        return list(range(int(level * multiplier), int(level * multiplier) + 10)) # Gives a range of 10 numbers, starting from the level * multiplier and 10 higher numbers from that

                    monster_attributes = {} # define all the attributes for the monster level

                    for level in range(1, 101): # populate monster_attributes up to level 100 (monster's max level)

                        monster_attributes[level] = {
                            'health_range': generate_range(level),
                            'luck_range': generate_range(level, multiplier=0.1), # adjust multiplier for luck
                            'strength_range': generate_range(level, multiplier=0.1), # adjust multiplier for strength
                            'agility_range': generate_range(level, multiplier=0.1), # adjust multiplier for agility
                        }

                    if monster_currentlevel in monster_attributes: # assuming monster_currentlevel is set appropriately

                        attributes = monster_attributes[monster_currentlevel] # retrieves a set of attributes based on the monster's current level

                        # Set monster attributes - a random number in the attribute range for each stat
                        monster_totalhealth += random.choice(attributes['health_range'])
                        monster_currentluck += random.choice(attributes['luck_range'])
                        monster_currentstrength += random.choice(attributes['strength_range'])
                        monster_currentagility += random.choice(attributes['agility_range'])

                        monster_currenthealth = monster_totalhealth

                    await ctx.author.send(f"""_ _ \n**{monster_name}** **(Level {monster_currentlevel})** 
                                          \nStarting Health: **{monster_currenthealth}**/**{monster_totalhealth}**
                                          \nLuck: **{monster_currentluck}**
                                          \nStrength: **{monster_currentstrength}**
                                          \nAgility: **{monster_currentagility}**""")
                    
                    print(f"First: {hero_currenthealth}")

# # Zone 1 Battle section ############################################################################

                    #rpg_instance = RPG()

                    class get_hero_actions(View): # battle actions input (will be used when hero fights a monster)
                        def __init__(self, rpg_cog, monster_currentagility, hero_currentluck, monster_currenthealth, hero_currentmana, hero_currenthealth, monster_totalhealth, original_message=None):
                            super().__init__()

                            self.rpg_cog = rpg_cog  # store the rpg_cog as an attribute
                            self.monster_currentagility = monster_currentagility # used for hero's attack miss percentage
                            self.hero_currentluck = hero_currentluck # used for hero's attack critical hit likelihood percentage
                            self.monster_currenthealth = monster_currenthealth
                            self.monster_totalhealth = monster_totalhealth
                            self.hero_currentmana = hero_currentmana
                            self.hero_currenthealth = hero_currenthealth
                            self.original_message = original_message
                        
                        @discord.ui.select(
                            placeholder="Choose an action to do",
                            options=[
                                discord.SelectOption(label="Physical Attack", value="1", description=f"Strength (damage modifier): {hero_currentstrength} ; \n Luck (critical hit modifier): {hero_currentluck}"),
                                discord.SelectOption(label="Magic Attack", value="2", description=f"Capacity: {hero_currentmana}/{hero_totalmana}"),
                                discord.SelectOption(label="Flee", value="3", description=f"Sends you back to Zone 1, but all enemies get leveled up"),
                            ]
                        )

                        async def select_callback(self, interaction, select):

                            select.disabled=True

                            if select.values[0] == "1": # chose to physical attack (so deal damage based on hero's Strength with the possibility of a critical hit or a miss)
                                print(f"Here is where self.hero_currenthealth shows 110 instead of 100: {self.hero_currenthealth}")

                                if self.hero_attack_hits(): # check if the hero's attack hits based on monster's agility

                                    damage = self.calculate_hero_damage() # calculate damage
                                    self.monster_currenthealth = monster_currenthealth
                                    self.monster_currenthealth -= damage

                                    audio_possible_physical_attack = ['C:\IT\DiscordBot\Attack1.mp3', 'C:\IT\DiscordBot\Attack2.mp3', 'C:\IT\DiscordBot\Attack3.mp3', 'C:\IT\DiscordBot\Attack4.mp3', 'C:\IT\DiscordBot\Attack5.mp3']
                                    audio_physicalattack = random.choice(audio_possible_physical_attack)
                                    await ctx.author.send(file=discord.File(audio_physicalattack)) # sends an audio file

                                    await ctx.author.send(f"Attack! You dealt **{damage}** damage to **{monster_name}**")

                                    if self.monster_currenthealth <= 0: # monster died (ran out of health)
                                       await ctx.author.send(f"You defeated **{monster_name}**")
                                    
                                    else: # monster attack
                                        await self.monster_attack() 

                                else: # hero missed physical attack
                                    
                                    audio_missphysicalattack = 'C:\IT\DiscordBot\MissAttack.mp3'
                                    await ctx.author.send(file=discord.File(audio_missphysicalattack)) # sends an audio file
                                    await ctx.author.send("Your attack missed")
                                    await self.monster_attack() # monster attacks

                            elif select.values[0] == "2": # chose to magic attack (so deal set damage based on hero's Mana)

                                if hero_currentmana >= 25:
                                    
                                    audio_possible_magic_attack = ['C:\IT\DiscordBot\Magic1.mp3', 'C:\IT\DiscordBot\Magic2.mp3', 'C:\IT\DiscordBot\Magic3.mp3', 'C:\IT\DiscordBot\Magic4.mp3', 'C:\IT\DiscordBot\Magic5.mp3']
                                    audio_magicattack = random.choice(audio_possible_magic_attack)
                                    await ctx.author.send(file=discord.File(audio_magicattack)) # sends an audio file
                                    
                                    self.hero_currentmana -= 25

                                    magic_damage = random.randint(hero_stat_currentmana + 10, hero_stat_currentmana + 10 * 5)  # calculate damage based on hero's current strength
                                    self.monster_currenthealth -= magic_damage

                                    await ctx.author.send("Magic!")

                                    if self.monster_currenthealth <= 0: # monster died (ran out of health)
                                       await ctx.author.send(f"You defeated **{monster_name}**")
                                    
                                    else: # monster attack
                                        await self.monster_attack()

                                else:

                                    await ctx.author.send(f"You only have **{self.hero_currentmana}** mana and you need **25** to do a magic attack")
                                    get_hero_actions_view = get_hero_actions(self, monster_currentagility, hero_currentluck, monster_currenthealth, monster_totalhealth, hero_currentmana, hero_currenthealth)
                                    hero_actions = await ctx.author.send(f"_ _ \nYour current health is **{self.hero_currenthealth}**/**{hero_totalhealth}**", view=get_hero_actions_view)
                                    get_hero_actions_view.original_message = hero_actions

                            elif select.values[0] == "3": # chose to flee (so take player back to Zone 1 and make the monsters level up)
                                
                                audio_flee = 'C:\IT\DiscordBot\Flee.mp3'
                                await ctx.author.send(file=discord.File(audio_flee)) # sends an audio file
                                await interaction.response.send_message("You turn and run, all the way back to Zone 1! Unfortunately that gives all the monsters a level up boost, so be prepared for them to be more difficult to defeat", ephemeral=True)

                            self.stop() # makes the player not be able to change their dropdown selection
                        
# # Hero Attack section ############################################################################

                        # Calculates physical damage based on hero's strength
                        def calculate_hero_damage(self):

                            self.hero_is_critical_hit = False

                            hero_base_damage = random.randint(hero_currentstrength + 10, hero_currentstrength + 10 * 2)  # calculate damage based on hero's current strength

                            # Check for a critical hit based on player's luck
                            critical_hit_chance = min(1.0, self.hero_currentluck * 0.099) # adjust the multiplier (when luck reaches 10, 99% chance of critical hit)
                            hero_is_critical_hit = random.random() < critical_hit_chance # did a critical hit

                            # Apply critical hit damage multiplier
                            if hero_is_critical_hit:
                                print("Hero did Critical Hit")
                                hero_base_damage *= 1.5 # adjust the multiplier for critical hit damage

                            print(f"Hero did: {hero_base_damage} damage")
                            return hero_base_damage # damage dealt to monster

                        # Generates a hit or a miss hero did against monster, based on monster's agility
                        def hero_attack_hits(self):
                            # Calculate hit chance based on monster's agility
                            hit_chance = max(0, 100 - self.monster_currentagility * 1.1) # adjust the multiplier

                            # Generate a random number between 0 and 100
                            random_number = random.randint(0, 100)

                            # Check if the random number is less than the hit chance
                            return random_number < hit_chance # did a hit (not a miss)
             
# # Monster Attack section ############################################################################
           
                        # Monster's attack
                        async def monster_attack(self):

                            self.monster_is_critical_hit = False

                            monster_damage = self.calculate_monster_damage()  # Calculate damage based on monster's strength

                            audio_possible_monster_attack = ['C:\IT\DiscordBot\Monster1.mp3', 'C:\IT\DiscordBot\Monster2.mp3', 'C:\IT\DiscordBot\Monster3.mp3', 'C:\IT\DiscordBot\Monster4.mp3', 'C:\IT\DiscordBot\Monster5.mp3', 'C:\IT\DiscordBot\Monster6.mp3', 'C:\IT\DiscordBot\Monster7.mp3', 'C:\IT\DiscordBot\Monster8.mp3',
                                                            'C:\IT\DiscordBot\Monster9.mp3', 'C:\IT\DiscordBot\Monster10.mp3', 'C:\IT\DiscordBot\Monster11.mp3', 'C:\IT\DiscordBot\Monster12.mp3', 'C:\IT\DiscordBot\Monster13.mp3', 'C:\IT\DiscordBot\Monster14.mp3', 'C:\IT\DiscordBot\Monster15.mp3',
                                                            'C:\IT\DiscordBot\Monster16.mp3', 'C:\IT\DiscordBot\Monster17.mp3', 'C:\IT\DiscordBot\Monster18.mp3', 'C:\IT\DiscordBot\Monster19.mp3', 'C:\IT\DiscordBot\Monster20.mp3']
                            audio_monsterattack = random.choice(audio_possible_monster_attack)
                            await ctx.author.send(file=discord.File(audio_monsterattack)) # sends an audio file

                            await ctx.author.send(f"_ _ \n**{monster_name}** attacks! You received **{monster_damage}** damage")

                            if self.monster_is_critical_hit:
                                await ctx.author.send("Monster did Critical Hit!")

                            print(f"Hero's health before getting attacked: {hero_currenthealth}")
                            print(self.hero_currenthealth)
                            
                            self.hero_currenthealth = hero_currenthealth
                            print(self.hero_currenthealth)

                            self.hero_currenthealth -= monster_damage

                            print(self.hero_currenthealth)
                            print(f"Hero's health after getting attacked: {hero_currenthealth}")

                            if self.hero_currenthealth <= 0: # hero died (ran out of health)

                                await ctx.author.send("You have been defeated!")
                                # Handle defeat logic here if needed

                            else: # hero's turn

                                print(hero_currenthealth)
                                get_hero_actions_view = get_hero_actions(self.rpg_cog, self.monster_currentagility, self.hero_currentluck,
                                                                            self.monster_currenthealth, self.monster_totalhealth,
                                                                            self.hero_currentmana, self.hero_currenthealth,
                                                                            self.original_message)                                
                                updated_message = await ctx.author.send(f"_ _ \nYour current health is **{self.hero_currenthealth}**/**{hero_totalhealth}** \n\n **{monster_name}** current health is **{self.monster_currenthealth}**", view=get_hero_actions_view)
                                #get_hero_actions_view.original_message = hero_actions

                                # Edit the original message with the updated information
                                await self.original_message.edit(content=updated_message.content, view=get_hero_actions_view)

                            ## After sending the original message, initialize the get_hero_actions with the original message
                            #get_hero_actions_view = get_hero_actions(self, monster_currentagility, hero_currentluck, monster_currenthealth, hero_currentmana, hero_currenthealth)
                            #hero_actions = await ctx.author.send(f"_ _ \nYour current health is **{hero_currenthealth}**/**{hero_totalhealth}**", view=get_hero_actions_view)
                            #get_hero_actions_view.original_message = hero_actions

                        # Calculates physical damage based on monster's strength
                        def calculate_monster_damage(self):

                            monster_base_damage = random.randint(monster_currentstrength, monster_currentstrength * 2)  # calculate damage based on monster's current strength

                            # Check for a critical hit based on monster's luck
                            critical_hit_chance = min(1.0, monster_currentluck * 0.099) # adjust the multiplier (when luck reaches 10, 99% chance of critical hit)
                            self.monster_is_critical_hit  = random.random() < critical_hit_chance # did a critical hit

                            # Apply critical hit damage multiplier
                            if self.monster_is_critical_hit:
                                print(f"Monster did Critical Hit (prep) with damageL {monster_base_damage}")
                                monster_base_damage *= 1.5 # adjust the multiplier for critical hit damage
                                print(f"Monster did Critical Hit (modified) with damageL {monster_base_damage}")

                            print(f"Monster did: {monster_base_damage} damage")
                            return monster_base_damage # damage dealt to hero

                        # Generates a hit or a miss monster did against hero, based on hero's agility
                        def monster_attack_hits(self):
                            # Calculate hit chance based on hero's agility
                            hit_chance = max(0, 100 - hero_currentagility * 1.1) # adjust the multiplier

                            # Generate a random number between 0 and 100
                            random_number = random.randint(0, 100)

                            # Check if the random number is less than the hit chance
                            return random_number < hit_chance # did a hit (not a miss)

# # Second dropdown (Zone 1 First Battle Actions) section ############################################################################
                              
                    get_hero_actions_view  = get_hero_actions(self, monster_currentagility, hero_currentluck, monster_currenthealth, monster_totalhealth, hero_currentmana, hero_currenthealth)
                    hero_actions = await ctx.author.send(f"_ _ \nYour current health is **{hero_currenthealth}**/**{hero_totalhealth}**", view=get_hero_actions_view) # bot gives player dropdown (asking to choose an action)
                    get_hero_actions_view.original_message = hero_actions

# # First dropdown (Level 1 Stat) section ############################################################################

            get_hero_stats = get_hero_stats(self)
            hero_stats = await ctx.author.send("_ _ \nHere are your current stat levels", view=get_hero_stats) # bot gives player dropdown (asking to set their stats)
            

    













        else:
            await ctx.author.send("_ _ \nYou did not input you name. Please do **!rpg** in the server: **Heart-to-Heart** to try again") # the player did not input their name (see get_hero_name method below)
            del self.gamesRPG[ctx.author.id] # clear the self.gamesRPG dictionary, to allow a new game to be started (see get_hero_name method below)

############################################################################

        #if hero_healthpotions <= 0:
        #    await ctx.author.send("You look in your bag and find nothing")
        
        #else:
            
        #    audio_healthpotion = 'C:\IT\DiscordBot\HealthPotion.mp3'
        #    await ctx.author.send(file=discord.File(audio_healthpotion)) # sends an audio file
        #    await ctx.author.send(f"You look in your bag and find **{hero_healthpotions}** health potion(s) and use one.")
        #    hero_currenthealth += 25
        #    if hero_currenthealth > hero_totalhealth: # to make sure that the current health doesn't go over the total health
        #        hero_currenthealth = hero_totalhealth

        #    hero_healthpotions -= 1
            
############################################################################


        #if hero_manapotions <= 0:
        #    await ctx.author.send("You look in your bag and find nothing")
        
        #else:

        #    audio_manapotion = 'C:\IT\DiscordBot\ManaPotion.mp3'
        #    await ctx.author.send(file=discord.File(audio_manapotion)) # sends an audio file
        #    await ctx.author.send(f"You look in your bag and find **{hero_manapotions}** mana potion(s) and use one.")
        #    hero_currentmana += 25
        #    if hero_currentmana > hero_totalmana: # to make sure that the current mana doesn't go over the total mana
        #        hero_currentmana = hero_totalmana

        #    hero_manapotions -= 1

############################################################################

    # Bot gives player an input (asking for their name)
    async def get_hero_name(self, ctx):
        try:
            response = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author and m.content.lower() != '!rpg' and m.content.lower() != 'timeout')
            return response.content # the player input their name ^
        
        except Exception as e:
            return False # the player did not input their name ^

###############################################################################################################################################################################################################

async def setup(bot):
    await bot.add_cog(RPG(bot)) # name of the Class, look above