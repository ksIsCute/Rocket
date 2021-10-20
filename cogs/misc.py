import discord
from discord.ext import commands
import datetime
import json
from datetime import datetime
from discord.ext.commands import Cog as c, command as cmd


class Miscellaneous(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
      print("Cog: Miscellaneous, Is Ready!")   

    @commands.command(aliases = ['suggestion', 'sg', 'sugges'])
    async def suggest(self, ctx, reason=None):
      if not reason:
        await ctx.send("It has to be an actual suggestion.")
        return
      embed = discord.Embed(
        title = "New Suggestion!",
        description = reason,
        color = discord.Color.random()
      )
      embed.set_author(
        text = ctx.author,
        icon_url = ctx.author.avatar_url
      )
      channel = self.bot.get_channel(839857214297604126)
      await channel.send(embed=embed)
    @commands.command()
    async def credits(self, ctx):
      embed = discord.Embed(
        title = "Staff and Owners Of Rocket!",
        description = "This is a list of all workers for Rocket!",
        color = discord.Color.random()
      )
      embed.add_field(
        name = "ks",
        value = "Lead developer and Founder of Rocket, created it by himself and built it from its members."
      )
      embed.add_field(
        name = "roliv",
        value = "Roliv is a good friend of ks, irl, and online, he helped with advertising and creating the server, making him the second founder/co-founder, of Rocket."
      )
      embed.add_field(
        name = "Ricewill23",
        value = "Ricewill is now resigned but used to own about 25% of Rocket, while helping out, Ricewill was part of ks's favourite staff members at the time."
      )
      embed.add_field(
        name = "Lenny / King Quacc",
        value = "Lenny aka King Quacc was very helpful during Rockets early days, while only knowing JS, could help with some pretty harsh errors when needed. Lenny was also owning 25% of Rocket at that time aswell, and still works there to this day, Ricewill and Lenny were ks's favouite staff members."
      )
      embed.add_field(
        name = "Patchysid",
        value = "Patchysid was the **very first** staff member at Rocket, and still works there to this day. Patchy helped with alot and had all perms/custom role, and was the third founder. Then left for a couple months after some personal issues, but came back and all is/was good."
      )
      embed.add_field(
        name = "You",
        value = "Without you Rocket would never be the same, as the popularity would go down, and we would have to just die off with other failed bots."
      )
      await ctx.send(embed=embed)
    @commands.command()
    async def invite(self, ctx):
      embed = discord.Embed(
        description = "[Click Here!](https://discord.com/oauth2/authorize?client_id=828380019406929962&permissions=8589934591&redirect_uri=https%3A%2F%2Frocketdiscord.xyz%2Finvited&response_type=code&scope=bot%20applications.commands%20identify)",
        color = discord.Color.random()
      )
      await ctx.send(embed=embed)
    @commands.command(aliases = ["FrontierGG", "Front", "Frontier_GG", "Fr0nt"])
    async def frontier(self, ctx):
      if ctx.author.id == 689461924038967346:
        frontierembed = discord.Embed(
          title = "Hey front it seems you found your command... :flushed:",
          description = "What colour is a mirror? :thinking:",
          color = discord.Color.random())
        
        await ctx.send(embed=frontierembed)
      embed = discord.Embed(
        title = "FrontierGG",
        description = "Frontier is an epic youtuber. ||[Click To Join](https://discord.gg/pTr9y3Vnpx)|| :)",
        color = discord.Color.random()
      )
      await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Miscellaneous(bot))