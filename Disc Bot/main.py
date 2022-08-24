import discord
import os
import sqlite3
from dotenv import load_dotenv


load_dotenv('.env')

client=discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))
   

@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  if message.content.startswith('!deadline'):
    await message.channel.send("League of Legends Deadlines: ")
    deadlines = ["Registration/Dropout Deadine: Sunday, Aug 7th", "League Schedule Release: Thursday, Aug 11th", "Keeper Declaration Deadline: Sunday, August 21st", "Super Bowl Pickem Deadline: Wednesday September 7th", "COVID Contingency Plan Deadline: Monday, November 7th", "Trade Deadline: Saturday, November 19th"]
    await message.channel.send("\n".join(map(str, deadlines)))
  if message.content.startswith('!draft'):
    await message.channel.send('The draft for League of legends is Sunday August 28th at 11am. PLEASE MAKE SURE YOU ARE AVAILABLE FOR THIS DAY')
  if message.content.startswith('!keepers'):
    keepers = ["Offense:", "Brandin Cooks (Year 1)", "Johnathan Taylor (Year 2), ", "Justin Herbert (Year 2)", "Matthew Stafford (Year 1)", "Justin Jefferson (Year 2)",
    "Ja'Marr Chase (Year 1)", "Deebo Samuel (Year 1)", "Diontae Johnson (Year 2)", "Rashod Bateman (Year 1)", "Javonte Williams (Year 1)", "Leonard Fournette (Year 1)",
    "Antonio Gibson (Year 2)", "AJ Dillon (Year 1)", "Michael Carter (Year 1)", "Tony Pollard (Year 1)", "Travis Etienne (Year 1)", "Mike Gesicki (Year 1)", "Defense:", 
    "Derwin James Jr (Year 1)", "Jeremy Chinn (Year 2)", "TJ Watt (Year 2)", "Fred Warner (Year 2)", "C.J. Mosely (Year 1)", "Foye Oluokun (Year 1)", "Cole Holcomb (Year 1)", 
    "Myles Garrett (Year 1)", "Joey Bosa (Year 1) "]
    await message.channel.send('Here is the list of keepers for the 2022 season:\n')
    await message.channel.send("\n".join(map(str, keepers)))
  if message.content.startswith('!keeperrules'):
    await message.channel.send('The rules regarding keepers is as follows: \n 1. Each keeper must have been drafted in the 4th round or later. \n 2. Each keeper being kept for their first year costs $5 and any 2nd year keeper costs $10 \n 3. The player you wish to keep must have been on your team at all times. No trades, no drops or pickups')
  if message.content.startswith('!clown'):
    await message.channel.send('Remeber the one time K-rod was on time for something? Yeah I dont either')
  if message.content.startswith('!playoffs'):
    await message.channel.send('Playoffs start December 13th, the top 6 teams make it in. Single elimination bracket. The bottom half of the table participate in the consolation bracket to fight for draft position.')
  if message.content.startswith('!rulebook'):
    await message.channel.send("If you cant seem to find the answer to your question or wish to have a rule elaborated on please refer to the 2022 Rule Book below: ")
    await message.channel.send(file=discord.File('Book of Legend 2022.pdf'))
  if message.content.startswith('!help'):
    help_commands = ["!tradedeadline= Trade Deadline Date", "!keeperdeadline = Deadline to declare keepers", "!keepers = List of the keepers that have been claimed", "!draft = Our leagues draft date and time", "!playoffs = Playoff start for Championship and Consolation bracket" , "!keeperrules = Rules for declaring keepers", "!rulebook = Link to our Leage of Legends 2022 rule book in case your question couldnt be answered or you needed an elaboration on one of the rules"]
    await message.channel.send('Having trouble using me? Here is a list of my commands to answer our most commonly asked questions in the league: ')
    await message.channel.send("\n\n".join(map(str, help_commands)))
  

client.run(os.getenv("TOKEN"))