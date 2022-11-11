import discord
from discord.ext import commands
import os
import sqlite3

class Pickems(commands.Cog, name= 'SB Pickems Draft'):

    def __init__(self, bot):
        self.bot = bot
        self.num_drafters = 0
        self.team = None
        self.begin = False
    @commands.command()
    async def pickems(self, ctx):
        num_drafters = 0
        team = None
        conn = None
        begin = input('Are you ready to start the draft? y/n')
        try: 
            conn = sqlite3.connect('leagueoflegends.db')
            cur = conn.cursor()
            cur.execute('''CREATE TBALE IF NONE EXISTS pickemDraft(
                    pickID INTEGER AUTO_INCREMENT PRIMARY KEY,
                    draftRound INTEGER,
                    team VARCHAR(50),
                    draftedBy VARCHAR(50),
                )''')
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.close()   