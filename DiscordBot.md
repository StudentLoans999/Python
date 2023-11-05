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
  
***
## Summary
Action 1 - Installed Python, PIP, discord, and then discord.py to get access to Discord's API

Action 2 - Created a Discord application

Action 3 - Created a Discord Guild (server)

Action 4 - Added the Bot to the server

Action 5 - Gave the Bot functionality by using a Python file I wrote

Action 6 - Added custom custom features for the Bot like: Direct Messaging, Event Listeners, and Input Commands

***

## Action 1 
Make sure to install Python first, in the Windows Store. 

The rest of the steps listed below in this action were done in CMD:

Also, create a Python Virtual Environment `python -m venv C:\Users\david\Desktop\DiscordBot` and then activate it : (https://realpython.com/python-virtual-environments-a-primer/)(https://docs.python.org/3/library/venv.html)(https://stackoverflow.com/questions/11005457/how-do-i-remove-delete-a-virtualenv#:~:text=You%20can%20do%20that%20by,delete%20myspecialenv%20or%20manual%20removal.&text=if%20you%20are%20windows%20user,command%20prompt%20rmvirtualenv%20environment%20name.)

Install pip : (https://www.liquidweb.com/kb/install-pip-windows/)

Install discord `pip install discord` and `pip install discord.py`
![image](https://github.com/StudentLoans999/Python/assets/77641113/d03e263e-5c34-4d7a-8370-6ace2e547e55)

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
Here I followed the guide directly but the discord UI has been updated so it is slightly different but the steps are the same. In the video, there's a helpful comment someone posted that fixed an error I was getting where I had to add to my code `client = discord.Client(intents=discord.Intents.default())`

After following the video, I continued following the guide which pretty much overwrote a lot that was done in the video (I just created one python file instead of splitting it up into three files originally)
***
## Action 6
H
***
Helpful information:

https://realpython.com/how-to-make-a-discord-bot-python/#interacting-with-discord-apis

https://discordpy.readthedocs.io/en/stable/ext/commands/api.html

https://discordpy.readthedocs.io/en/latest/faq.

Errors I encountered:

https://stackoverflow.com/questions/71959420/client-init-missing-1-required-keyword-only-argument-intents-or-tak - I did `bot = discord.Client(intents=discord.Intents.default())`

https://stackoverflow.com/questions/68329014/discord-py-bot-not-triggering-and-ignoring-commands - I did `await bot.process_commands(message)`

https://www.reddit.com/r/Discord_Bots/comments/b97qdz/improper_token_has_been_passed_error_using_python/ - I did 
