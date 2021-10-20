import discord
import asyncio
from discord.ext import commands

class random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
      print("Cog: random, Is Ready!")        

def setup(bot):
    bot.add_cog(random(bot))