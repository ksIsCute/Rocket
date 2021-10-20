import discord
import asyncio
import random
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
      print("Cog: Fun, Is Ready!")

    @commands.command()
    async def goodbye(self, ctx):
      embed = discord.Embed(
      title = "Aight imma head out.",
      color = discord.Color.random()
      )
      embed.set_image(url = "https://cdn.discordapp.com/attachments/830887279395340308/854735218568724490/download_1.gif")
      await ctx.send(embed=embed)

    @commands.command()
    async def hack(self, ctx, member: discord.Member=None):
      n = open("txt/ip.txt", "r")
      ip = n.readlines()
      a = open("txt/email.txt", "r")
      mail = a.readlines()
      
      b = open("txt/credit.txt", "r")
      credit = b.readlines()
      
      if not member:
        member = ctx.author

      mess = await ctx.send("**<a:CE_PepeHack:852894841322602508> | Getting Ip Address..**")
      await asyncio.sleep(2)
      await mess.edit(content="**<a:loading:838622217566814218> | Finding Ip Address..**")
      await asyncio.sleep(2)
      await mess.edit(content="**<a:loading:838622217566814218> | Found Ip Address!**")
      await asyncio.sleep(2)
      await mess.edit(content="**<a:loading:838622217566814218> | Getting Email Address.. **")
      await asyncio.sleep(2)
      await mess.edit(content="**<a:CE_PepeHack:852894841322602508> | Finding Email Address..**")
      await asyncio.sleep(2)
      await mess.edit(content="**<a:CE_PepeHack:852894841322602508> | Found email address!**")
      await asyncio.sleep(2)
      await mess.edit(content="**<a:loading:838622217566814218> | Finding Credit Card Information..**")
      await asyncio.sleep(2)
      await mess.edit(content="**<a:loading:838622217566814218> | Found credit card!**")
      await asyncio.sleep(2)
      await mess.edit(content="**<a:CE_PepeHack:852894841322602508> | Loading Data. :arrow_down_small: :arrow_down_small:**")
      await asyncio.sleep(2)
      embed = discord.Embed(
        title = "Hacked!",
        description = "All Data From User Is Below!",
        color = discord.Colour.random()
      )
      embed.add_field(
        name = ":house_with_garden: | Members Ip Address:",
        value = random.choice(ip)
      )
      embed.add_field(
        name = ":e_mail: | Members Email Address:",
        value = random.choice(mail)
      )
      embed.add_field(
        name = ":credit_card: | Members Credit Card:",
        value = random.choice(credit)
      )
      await mess.edit(embed=embed)

    @commands.command(aliases=['pp', 'ppsize', 'mypp'])
    async def ppmeter(self, ctx, member: discord.Member=None):
      ppsizes = [
            "8D", 
            "8=========D", 
            "8==D", 
            "8======D", 
            "8 (no pp just balls)", 
            "8========D", 
            "8=D", 
            "8=========D", 
            "8===============D"
        ]

      pprate = [
        "Garbage",
        "Trash",
        "Wicked",
        "Poggers",
        "Niiiice",
        "Chad",
        "Absolute monster of a",
        "Completely blown away by your",
        "Holy shit thats a nice",
        "HOLY GRAIL OF",
        "Absolutely bonkers",
        "Nice day for a nice",
        "Huge",
        "Thats a bloated"
      ]

      if not member:
        embed=discord.Embed(title="PP Meter!", color=discord.Colour.random())
        embed.add_field(name=f"{ctx.author.display_name}'s pp:", value=f"{random.choice(ppsizes)}")
        embed.set_footer(text=f"{random.choice(pprate)} pp!")
        await ctx.send(embed=embed)
        return

      embed=discord.Embed(title="PP Meter!", color=discord.Colour.random())
      embed.add_field(name=f"{member.display_name}'s pp:", value=f"{random.choice(ppsizes)}")
      embed.set_footer(text=f"{random.choice(pprate)} pp!")
      await ctx.send(embed=embed)

    @commands.command(aliases=['qt', 'quotethis'])
    async def quoteme(self, ctx, member: discord.Member, *, reason):
      if member is None:
        member = ctx.author
      
      embed = discord.Embed(
        title = "Quoted!",
        description = f"{member.mention}\n> {reason}",
        color = discord.Color.random()
      )
      embed.set_thumbnail(url = member.avatar_url)
      embed.set_footer(text = f"Quote created by {ctx.author}", icon_url = ctx.author.avatar_url)
      await ctx.send(embed=embed)

    @commands.command(aliases=['8bal', '8ball'])
    async def _8ball(self, ctx, *, question=None):
      responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes, definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "Of Course!",
        "No way!"]
      if not question:
        await ctx.send("You have to give me a question to answer!")
        return
      embed=discord.Embed(title="The 8ball has spoken!", color=discord.Colour.random())
      embed.add_field(name="Question:", value=question)
      embed.add_field(name="The 8ball says:", value=f'{random.choice(responses)}')
      embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/791575336276983809/854417537303707658/unknown.png")
      await ctx.send(embed=embed)


    @commands.command()
    async def quote(self, ctx):
      a = open("txt/quotes.txt", "r")
      quote = a.readlines()
      embed = discord.Embed(
        title = "Quote:",
        description = random.choice(quote),
        color = discord.Colour.random()
      )
      await ctx.send(embed=embed)
    
    @commands.command()
    async def kill(self, ctx, member: discord.Member):
      k = open("txt/kill.txt", "r")
      kills = k.readlines()
      await ctx.send(f"{member} {random.choice(kills)}")


def setup(bot):
    bot.add_cog(fun(bot))