import discord
import asyncio
from discord.ext import commands
import random
from random import randint
import requests

class games(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self.client = client
        self.bot = client
        self.ttt_games = {}
    @commands.command(aliases=['rock', 'paper', 'scissors', 'rps'])
    async def rockpaperscissors(self, ctx):

      buttons=["🪨", "🧾", "✂️"]
      embed=discord.Embed(title="Rock Paper Scissors!", description="Choose `Rock`, `Paper` Or `Scissors` For Your Answer!", color=ctx.author.color)
      embed.set_footer(text="Command Requested By {}".format(ctx.author), icon_url=ctx.author.avatar_url)
      sent=await ctx.send(embed=embed)

      for button in buttons:
         await sent.add_reaction(button)

      while True:
        try:
            reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)

        except asyncio.TimeoutError:
            await sent.delete()
            break

        else:
          bot_rps="rps"
          rps_random=random.choice(bot_rps)
          
          if rps_random == "r":
            if reaction.emoji == "🪨":
              embed=discord.Embed(title="It's A Tie!", description="Both Players Chose Rock! It's A Tie!", color=16776960)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "🧾":
              embed=discord.Embed(title="You Win!", description="You Chose Paper & I Chose Rock! You Win!", color=65280)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "✂️":
              embed=discord.Embed(title="You Lose!", description="You Chose Scissors & I Chose Rock", color=16711680)
              await ctx.send(embed=embed)
              break
          
          elif rps_random == "p":
            if reaction.emoji == "🪨":
              embed=discord.Embed(title="You Lose!", description="You Chose Rock & I Chose Paper! You Lose!", color=16711680)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "🧾":
              embed=discord.Embed(title="It's A Tie!", description="Both Players Chose Paper! It's A Tie!", color=16776960)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "✂️":
              embed=discord.Embed(title="You Win!", description="You Chose Scissors & I Chose Paper! You Win!", color=65280)
              await ctx.send(embed=embed)
              break
          
          elif rps_random == "s":
            if reaction.emoji == "🪨":
              embed=discord.Embed(title="You Win!", description="You Chose Rock & I Chose Scissors! You Win!", color=65280)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "🧾":
              embed=discord.Embed(title="You Lose!", description="You Chose Paper & I Chose Scissors! You Lose!", color=16711680)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "✂️":
              embed=discord.Embed(title="It's A Tie!", description="Both Players Chose Scissors! It's A Tie!", color=16776960)
              await ctx.send(embed=embed)
              break  

def setup(bot):
    bot.add_cog(games(bot)) 