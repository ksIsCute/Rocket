import discord
import asyncio
from discord.ext import commands
import random

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
      print("Cog: Help, Is Ready!")        

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def help(self, ctx):
      if ctx.invoked_subcommand is None:
        embed = discord.Embed(
          title = "Help!",
          description = "**This is the updated help command from 14/06/2021 (DD/MM/YY)**",
          color = discord.Colour.random()
        )
        embed.add_field(name = "⚒️ | Type `help mod` for all moderation commands!", value = "**<a:loading:852551706075725855> | Type `help image` for all image commands!**")
        embed.add_field(
          name = "⚙️ | Type `help utility` for all utility commands!",
          value = "**<a:DuckWalk:883937419576102972> | Type `help fun` for all fun commands!**"
        )
        embed.add_field(
          name = "Type `help games` for all of the fun games!",
          value = "More sooooooooon!"
        )
        b = open("txt/gifs.txt", "r")
        pictures = b.readlines()
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text = f"Command requested by {ctx.message.author}")
        embed.set_image(url = random.choice(pictures))
        await ctx.send(embed=embed)
        return
    @help.command()
    async def fun(self, ctx):
      embed = discord.Embed(
        title = "All fun commands!",
        value = "Listed Below!",
        color = discord.Colour.random()
      )
      embed.add_field(
        name = "Hack",
        value = "Get someone back by hacking them with this *totally* real hack command!"
      )
      embed.add_field(
        name = "PP Meter",
        value = "Whats your PP size? Find out with this command!"
      )
      embed.add_field(
        name = "8ball",
        value = "Tell the magic 8ball anything your heard desires, see what it says."
      )
      embed.add_field(
        name = "Quote",
        value = "Get a random quote!"
      )
      embed.add_field(
        name = "Poll",
        value = "Create a poll with a yes or no voting system!"
      )
      embed.add_field(
        name = "quotethis",
        value = "Quote a member, or yourself, on something!"
      )
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text = f"Command requested by {ctx.message.author}")
      await ctx.send(embed=embed)
    @help.command()
    async def mod(self, ctx):
      embed = discord.Embed(
        title = "All Moderation Commands!",
        color = discord.Colour.random()
      )
      embed.add_field(
        name = "Ban",
        value = "Ban whoever you want in this guild, or someones ID!"
      )
      embed.add_field(
        name = "Unban",
        value = "Unban a users ID from this guild."
      )
      embed.add_field(
        name = "Role",
        value = "Role a user a role in this guild! (case sensitive)"
      )
      embed.add_field(
        name = "Nuke",
        value = "Delete and clone the channel provided to remove all of its contents!"
      )
      embed.add_field(
        name = "Kick",
        value = "Kick a user from your server!"
      )
      embed.add_field(
        name = "Mute",
        value = "Mutes a specified user!"
      )
      embed.add_field(
        name = "Unmute",
        value = "Unmutes a specfic user!"
      )
      embed.add_field(
        name = "Purge",
        value = "Purges a certain amount of messages!"
      )
      embed.add_field(
        name = "Slowmode",
        value = "Changes the slowmode of this channel to a specfic time!"
      )
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text = f"Command requested by {ctx.message.author}")
      await ctx.send(embed=embed)
    @help.command()
    async def image(self, ctx):
      embed = discord.Embed(
        title = "Image help!",
        color = discord.Color.random()
      )
      embed.add_field(
      name = "ChangeMyMind (cmm)",
      value = "Change your mind with this meme template!"
      )
      embed.add_field(
        name = "youtubeComment (ytc)",
        value = "Make someone, or yourself, comment something!"
      )
      embed.add_field(
        name = "Wanted",
        value = "Give a user, or yourself, a 10 thousand dollar bounty!"
      )
      embed.add_field(
        name = "Rip",
        value = "Give a user a grave! (cuz their dead right?)"
      )
      embed.add_field(
        name = "Dog",
        value = "Get a random photo of a cute dog!"
      )
      embed.add_field(
         name = "Panda",
         value = "Get a random picture of a panda online!"
      )
      embed.add_field(
        name = "Fox",
        value = "Get a picture of a fox online!"
      )
      embed.add_field(
        name = "Bird",
        value = "Get a picture of a bird online!"
      )
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text = f"Command requested by {ctx.message.author}")
      await ctx.send(embed=embed)
    @help.command()
    async def utility(self, ctx):
      embed = discord.Embed(
        title = "Utility Commands!",
        color = discord.Color.random()
      )
      embed.add_field(
        name = "Whois",
        value = "Get basic information like join position, join date, creation date, and role count, of a specific user!"
      )
      embed.add_field(
        name = "Snipe",
        value = "Someone delete an image or message you didnt see? No worry! Use the command snipe and see what it was!"
      )
      embed.add_field(
        name = "Reminder",
        value = "Create an reminder up to 90 days!"
      )
      embed.add_field(
        name = "Avatar",
        value = "Get a users avatar!" 
      )
      embed.add_field(
        name = "uptime",
        value = "Check the bots uptime!"
      )
      embed.add_field(
        name = "Ping",
        value = "Check the bots latency!"
      )
      embed.add_field(
        name = "Stats",
        value = "Get Rockets stats!"
      )
      embed.add_field(
        name = "cc",
        value = "Look at how many commands have been used!"
      )
      embed.add_field(
        name = "Credits",
        value = "Look at all the people who made Rocket possible!"
      )
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text = f"Command requested by {ctx.message.author}")
      await ctx.send(embed=embed)
    @help.command()
    async def games(self, ctx):
      embed = discord.Embed(
        title = "Games!",
        color = discord.Color.random()
      )
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text = f"Command requested by {ctx.message.author}")
      embed = discord.Embed(
        title = "rps",
        description = "Play rock paper scissors with me!",
        color = discord.Color.random())
      await ctx.send(embed=embed)
    @help.command()
    async def faq(self, ctx):
      embed = discord.Embed(
        Title = "Rocket FAQ:",
        description = "These questions probably arent asked much, but I thought i'd answer to some speculation about Rockets recent *'lack'* of updates.",
        color = discord.Color.random()
      )
      embed.add_fiend(
        name = "What Happened To Rocket?",
        value = "Nothing but lack of motivation. Rocket as a bot has been highly sucsessful as reaching 50 thousand members in april, to the server being deleted and nuked. I have began to work on other things, but am now drifting back towards coding."
      )
      embed.add_field(
        name = "Is it true that the owner is a p||edophile||?",
        value = "(I have actually gotten this) Uhh.. The owner is a 13 year old Canadian kid, he is not a p||edophile||, please stop asking me this."
      )
      embed.add_field(
        name = "What do you do now?",
        value = "I manage the contents and details in a database containing 500,000 users for a Indonesian based company."
      )
      await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(help(bot))