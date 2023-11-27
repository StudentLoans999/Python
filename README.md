For this project, I created a bot for Discord for users to interact on the server with, by following this guide: 

https://builtin.com/software-engineering-perspectives/discord-bot-python

## Table of Contents
- [Summary](#Summary)
- [Action 1](#Action-1)
- [Action 2](#Action-2)
- [Action 3](#Action-3)
- [Action 4](#Action-4)
- [Action 5](#Action-5)
- [Action 6](#Action-6)
- [Helpful Information](#Helpful-Information)
- [Action 7](#Action-7)
  
***
## Summary
Action 1 - Installed Python, PIP, discord, and then discord.py to get access to Discord's API

Action 2 - Created a Discord application

Action 3 - Created a Discord Guild (server)

Action 4 - Added the Bot to the server

Action 5 - Gave the Bot functionality by using a Python file I wrote

Action 6 - Added custom features for the Bot (Direct Messaging, Event Listeners, and Input Commands) which are then used in the minigames I created

Helpful Information - Resources used and steps taken to optimize and/or fix the Bot

Action 7 - Created minigames and then explained how I went about making the specific one "Ready, Set, Go"

***

## Action 1 
Make sure to install Python (Version 3.11 only, any additional version doesn't work with importing Discord.py) first, in the Windows Store, and also from (https://www.python.org/downloads/windows/)

The rest of the steps listed below in this action were done in CMD:


Also, create a Python Virtual Environment `python -m venv C:\Users\david\Desktop\DiscordBot` and then activate it : (https://realpython.com/python-virtual-environments-a-primer/)
(https://blog.finxter.com/modulenotfounderror-no-module-named-discord-in-python/)
(https://docs.python.org/3/library/venv.html)
(https://stackoverflow.com/questions/11005457/how-do-i-remove-delete-a-virtualenv#:~:text=You%20can%20do%20that%20by,delete%20myspecialenv%20or%20manual%20removal.&text=if%20you%20are%20windows%20user,command%20prompt%20rmvirtualenv%20environment%20name.)

Install pip : (https://www.liquidweb.com/kb/install-pip-windows/)

Install discord `pip install discord` and `pip install discord.py`
![image](https://github.com/StudentLoans999/Python/assets/77641113/30d062c8-236b-4827-8a0a-6dc64441261b)

Then continue following the guide
***
## Action 2
Here I followed the guide directly but the discord UI has been updated so it is slightly different but the steps are the same
***
## Action 3
Here I followed the guide directly
***
## Action 4
Here I followed the guide directly
***
## Action 5
Here I followed the guide directly but the discord UI has been updated so it is slightly different but the steps are the same. In the video, there's a helpful comment someone posted that fixed an error I was getting where I had to add to my code `bot = discord.Client(intents=discord.Intents.default())` But that got changed later to
```
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
```

After following the video, I continued following the guide which pretty much overwrote a lot that was done in the video (I just created one python file instead of splitting it up into three files originally)
***
## Action 6
You can find the custom features implemented throughout the .py files and also in the minigames. 
***
## Helpful Information

https://realpython.com/how-to-make-a-discord-bot-python/#interacting-with-discord-apis

https://discordpy.readthedocs.io/en/stable/ext/commands/api.html

https://discordpy.readthedocs.io/en/latest/faq

Errors I encountered:

ChatGPT helps the most in making sure this and everything else in this Action are installed in the right place:

"WARNING: The script dotenv.exe is installed in 'C:\Users\david\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location."
  
  "import dotenv could not be resolved"

https://stackoverflow.com/questions/71959420/client-init-missing-1-required-keyword-only-argument-intents-or-tak - I did `bot = discord.Client(intents=discord.Intents.default())`


https://stackoverflow.com/questions/68329014/discord-py-bot-not-triggering-and-ignoring-commands - I did `await bot.process_commands(message)`


https://www.reddit.com/r/Discord_Bots/comments/b97qdz/improper_token_has_been_passed_error_using_python/ - I did this in [DiscordBot.py](DiscordBot.py)
```
import os
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# These comments below were for error testing, uncomment the Prints to make sure the token is set correctly
#bot.run("DISCORD_TOKEN")
#print(DISCORD_TOKEN)
#print(os.environ.get('DISCORD_TOKEN'))

bot.run(os.environ.get('DISCORD_TOKEN'))
```

I did this in [.env](.env) ; I kept both files in the same directory level, with the virtual environment
```
# .env
DISCORD_TOKEN = "INSERT TOKEN FROM https://discord.com/developers/application HERE"
```
***
## Action 7
After learning the basics of Discord Bot development, I decided to create some minigames (both classics and originals) to further my Python knowledge and experience.

There are a lot of minigames (and user commands), so I'm just going to focus on describing in-depth one particular one on this page: Ready, Set, Go. (The rest of the minigames are uploaded as well, so you can what they do, they just have an explanation like the one below.)

**Ready, Set, Go:**

The rules of this game are quite simple, a player starts off the game by doing the command !readysetgo and then will tell the Bot how many rounds to play. The Bot will then say "Ready", "Set" and then will say a bunch of random words in a random order that look similar to "Go". When the Bot does finally say "Go", the player who first does the command !dogo the fastest wins that round. If any player does the command !dogo before the Bot says "Go", then they get eliminated from the match. Throughout the game, everyone's role is shown in the Members area in Discord. The important roles are Winner and Eliminated. After all the rounds are concluded, the Bot will present a scoreboard listing all the winners and eliminated in the match.

Here is how I decided to logically process and formulate this minigame (my version of pseudocode):

+ Player does !readysetgo command 

  _Initial Setup section_
    + Has !readysetgo been done in the channel "ready-set-go"? 
      + **NO:** Tell player that the command only works in "ready-set-go" and offer a link to that channel
      + **YES:** Continue...
    + Has !readysetgo been done before?
      + **YES:** Tell player that a game is already running
      + **NO:** Continue to First Round section...
  
  _Round Setup section (Start of Gameplay)_
      + Will this be the first round?
        + **YES:** Resets all the players' roles (so that everyone is just a "Player" role, not a "Winner" or "Eliminated role)
          + Check to make sure it is the same player who did !readysetgo, and that they also input a positive integer (greater than zero), when asked by the Bot how many rounds to set for this current match
            + **NO:** Have the Bot tell that player that they didn't reply in time and should do !readysetgo again
            + **YES:** The Bot starts Round 1
            
  _Round 1 section (Start of Gameplay)_
    + Is this the first round?
      + **YES:** The Bot displays the current round number out of how many rounds total. Then it says "Ready", "Set" and then will say a bunch of random words in a random order (every half second) that look similar to "Go"
        + Has the Bot said "Go"?
          + **YES:** Stops the Bot from saying any additional words and lets the player not get eliminated, but win, for doing !dogo
          + **NO:** If a player does !dogo during this time, eliminate them   

   _Scoreboard section (End of Gameplay)_
    + Was the final round just finished?
      + **YES:** Are there any Winners in the server?
        + **YES:** Is the current channel "ready-set-go"?
          + **YES:** The Bot then lists out players with the Winner role in the match
          + **NO:** The Bot says to everyone that the current channel is wrong and should be "ready-set-go"
        + **NO:** The Bot says to everyone that there are Winners but not in the channel "ready-set-go"
      + **NO:** The Bot says to everyone that there are no Winners in this server
      + **YES:** Are there any Eliminated in the server?
          + **YES:** Is the current channel "ready-set-go"?
            + **YES:** The Bot then lists out players with the Eliminated role in the match
            + **NO:** The Bot says to everyone that the current channel is wrong and should be "ready-set-go"
          + **NO:** The Bot says to everyone that there are Eliminated but not in the channel "ready-set-go"
        + **NO:** The Bot says to everyone that there are no Eliminated in this server 
      + **YES:** The Bot makes all the players' roles reset (getting rid of the Winners and Eliminated) along with all the other variables, and then exits the game
       
+ Player does !dogo command
    
  + Has !dogo been done in the channel "ready-set-go"?
    + **NO:** The Bot tells the player that they need to do !dogo in the channel "ready-set-go"
    + **YES:** Has !readysetgo been done already?
      + **NO:** The Bot tells the player that the game hasn't started yet, so !dogo won't do anything. Then it lets them know to do !readysetgo first
      + **YES:** Has the Bot said "Go" yet?
        + **NO:** Is the player who did !dogo, Eliminated?
          + **YES:** The Bot tells that player that they are already eliminated. (This should never run though, since being Eliminated makes a player not able to speak for the rest of the match.)
          + **NO:** The Bot tells the player that they went too early and now are eliminated for it 
        + **YES:** The Bot makes players get the Waiting role (which makes them not able to speak temporarily while the next step in logic runs). Then the Bot tells the player that they were the fastest to do !dogo after "Go" appeared and that they have won this round. Then it sets the current round to be one higher and resets some other variables so that the next round can start without a hitch. Next, the Bot removes the Winners and Eliminated roles from the players so that the next round is fresh. After, the Bot removes the Waiting role from the players so that they can play in the next round. Finally, the Bot does the !readysetgo command itself which makes the game run another round

+ _Player does not do !dogo command after "Go" section_
  + Has "Go" been said by the Bot and no player has done !dogo?
    + **YES:** Checks for at least one player who isn't Eliminated and is in the channel "ready-set-go"
      + **NO:** Exit... 
      + **YES:** The Bot starts a 30-second timer
        + Has "Go" still not been said by the Bot and no player has done !dogo, after the timer expires?
          + **YES:** The Bot says that no one has responded in time and that the match is now concluded. Then it makes everyone, except the Winners, eliminated. Then the Bot runs the _Scoreboard section (End of Gameplay)_ logic
***
