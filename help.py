import discord
from discord.ext import commands
import os
from dotenv import load_dotenv



    
bot = commands.Bot(command_prefix='!', description = 'A bot that helps you guys and manages the Pickems and Survivor pools')
load_dotenv()

class CustomHelpCommand(commands.HelpCommand):
  
    def __init__(self):
      super().__init__()
      
    async def send_bot_help(self, mapping):
      return await super().send_bot_help(mapping)
       
@bot.event
async def on_ready():
  await bot.change_presence(status= discord.Status.online, activity= discord.Game("Tom Brady's Divorce Lawyer"))
  print('Bot is ready')

  
@bot.command()
async def keepers(ctx):
  keepers = ["Offense:", "Brandin Cooks (Year 1)", "Johnathan Taylor (Year 2), ", "Justin Herbert (Year 2)", "Matthew Stafford (Year 1)", "Justin Jefferson (Year 2)",
    "Ja'Marr Chase (Year 1)", "Deebo Samuel (Year 1)", "Diontae Johnson (Year 2)", "Rashod Bateman (Year 1)", "Javonte Williams (Year 1)", "Leonard Fournette (Year 1)",
    "Antonio Gibson (Year 2)", "AJ Dillon (Year 1)", "Michael Carter (Year 1)", "Tony Pollard (Year 1)", "Travis Etienne (Year 1)", "Mike Gesicki (Year 1)", "Defense:", 
    "Derwin James Jr (Year 1)", "Jeremy Chinn (Year 2)", "TJ Watt (Year 2)", "Fred Warner (Year 2)", "C.J. Mosely (Year 1)", "Foye Oluokun (Year 1)", "Cole Holcomb (Year 1)", 
    "Myles Garrett (Year 1)", "Joey Bosa (Year 1) "]
  await ctx.send("Here are the keepers for the 2022 season: ")
  await ctx.send("\n".join(map(str,keepers)))
  
@bot.command()
async def deadlines(ctx):
  deadlines = ["Registration/Dropout Deadine: Sunday, Aug 7th", "League Schedule Release: Thursday, Aug 11th", "Keeper Declaration Deadline: Sunday, August 21st", "Super Bowl Pickem Deadline: Wednesday September 7th", "COVID Contingency Plan Deadline: Monday, November 7th", "Trade Deadline: Saturday, November 19th"]
  await ctx.send("Here are the deadlines for the 2022 season: ")
  await ctx.send("\n".join(map(str,deadlines)))
  
@bot.command()
async def playoffs(ctx):
  await ctx.send("Playoffs start December 13th, the top 6 teams make it in. Single elimination bracket. The bottom half of the table participate in the consolation bracket to fight for draft position.")

@bot.command()
async def keeperrules(ctx):
  await ctx.send("The rules regarding keepers is as follows: \n 1. Each keeper must have been drafted in the 4th round or later. \n 2. Each keeper being kept for their first year costs $5 and any 2nd year keeper costs $10 \n 3. The player you wish to keep must have been on your team at all times. No trades, no drops or pickups")
bot.run(os.getenv('TOKEN'))
