import discord
import asyncio
from discord.ext import commands
import datetime
import random
import aiohttp


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog: Utility, Is Ready!")

    @commands.command(aliases=['whois', 'usrinfo', 'info', 'userstats', 'ui'])
    async def userinfo(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(description=user.mention,
                              color=discord.Color.random())
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined",
                        value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Join position",
                        value=str(members.index(user) + 1))
        embed.add_field(name="Made account on",
                        value=user.created_at.strftime(date_format))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles) - 1),
                            value=role_string,
                            inline=False)
        embed.set_footer(text='ID: ' + str(user.id))
        await ctx.send(embed=embed)

    format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

    @commands.command(aliases=["remind", "remindme", "remind_me", "timer", "alarm", 'rm'])
    async def reminder(self, ctx, time, *, reminder):
      embed = discord.Embed(color=0x0000f0,timestamp=datetime.utcnow())
      embed.set_footer(text=f"{reminder}",
        icon_url=f"{ctx.author.avatar_url}")
      seconds = 0
      if time.lower().endswith("d"):
          seconds += int(time[:-1]) * 60 * 60 * 24
          counter = f"{seconds // 60 // 60 // 24} day(s)"
      if time.lower().endswith("h"):
          seconds += int(time[:-1]) * 60 * 60
          counter = f"{seconds // 60 // 60} hour(s)"
      elif time.lower().endswith("m"):
          seconds += int(time[:-1]) * 60
          counter = f"{seconds // 60} minutes"
      elif time.lower().endswith("s"):
          seconds += int(time[:-1])
          counter = f"{seconds} seconds"
      if seconds == 0:
          embed.add_field(
              name='Warning',
              value=
              'Please specify a proper duration, please put a time minimum of `5` minutes for more information.'
          )
      elif seconds < 300:
          embed.add_field(
              name='Warning',
              value=
              'You have specified a too short duration!\nMinimum duration is 5 minutes.'
          )
      elif seconds > 7776000:
          embed.add_field(
              name='Warning',
              value=
              'You have specified a too long duration!\nMaximum duration is 90 days.'
          )
      else:
          await ctx.send(
              f"Alright, {ctx.author.mention}. I will remind you to `{reminder}` in `{counter}`."
          )
          await asyncio.sleep(seconds)

          embed = discord.Embed(
              title="Reminded!",
              description=
              f"Hey, {ctx.author.mention}. You asked me to remind you to: \n`{reminder}` \n`{counter}` ago.",
              color=discord.Colour.random())
          embed.set_footer(text=f"{ctx.author.name}",
                            icon_url=f"{ctx.author.avatar_url}")
          await ctx.send(content=ctx.author.mention, embed=embed)

    @commands.command(aliases=['avatar', 'av'])
    async def aVatur(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        userAvatar = member.avatar_url
        em = discord.Embed(title='User avatar:', color=discord.Colour.random())
        em.set_image(url=userAvatar)
        await ctx.send(embed=em)

    commands.sniped_messages = {}

    async def on_message_delete(message):
        if message.attachments:
            bob = message.attachments[0]
            commands.sniped_messages[message.guild.id] = (bob.proxy_url,
                                                          message.content,
                                                          message.author,
                                                          message.channel.name,
                                                          message.created_at)
        else:
            commands.sniped_messages[message.guild.id] = (message.content,
                                                          message.author,
                                                          message.channel.name,
                                                          message.created_at)

    @commands.command(aliases=['gb', 'banlist'])
    @commands.has_permissions(ban_members=True)
    async def getbans(self, ctx):
        x = await ctx.message.guild.bans()
        x = '\n'.join([str(y.user) for y in x])
        embed = discord.Embed(title="List of Banned Members",
                              description=x,
                              colour=0xFFFFF)
        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utility(bot))
