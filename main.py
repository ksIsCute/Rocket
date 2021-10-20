from discord.ext import commands
from discord.ext.commands import CommandNotFound
from host import keep_alive
import random, asyncio, datetime, json, os, discord
from datetime import datetime

def get_prefix(client, message):
    with open("json/prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes.get(str(message.guild.id), "$")

client = commands.Bot(command_prefix = get_prefix, intents=discord.Intents.all(), allowed_mentions=discord.AllowedMentions(roles=False, everyone=False, users=False), case_insensitive=True)
bot = client
client.launch_time = datetime.utcnow()
client.remove_command("help")

counter = 0

def count():
  global counter
  counter += 1

@client.command()
@commands.is_owner()
async def leave(ctx, guil: discord.Guild=None):
  await ctx.send(f"Leaving {guil.name}..")
  try:
    await ctx.guild.leave(guil)
  except:
    await ctx.send(f"For some reason I wasnt able to leave the guild {guil.name}")

@client.event
async def on_command(ctx):
  count()
  if counter == 100:
    msg = await ctx.send("**Hooray!**\n`100`\nCommands Have Been Used!")
    await msg.add_reaction("🎉")
  if counter == 50:
    msg = await ctx.send("**Suprise!**\n`50`\nCommands Have Been Used!")
    await msg.add_reaction("🎉")
  if counter == 25:
    msg = await ctx.send("**Woop Woop!**\n`25`\n Commands Have Been Used!")
    await msg.add_reaction("🎉")

@client.command(aliases = ['cc', 'commandsused', 'commandscount', 'totalused', 'sessioncount', 'commandc'])
async def commandcount(ctx):
  await ctx.send(f'In this session there has been `{counter}` commands used!')

@client.command()
async def uptime(ctx):
  delta_uptime = datetime.utcnow() - client.launch_time
  hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
  minutes, seconds = divmod(remainder, 60)
  days, hours = divmod(hours, 24)
  embed=discord.Embed(
    title="Total uptime!", 
    description=f"`{days}d, {hours}h, {minutes}m, {seconds}s`", 
    color=0x0000ff)
  embed.set_footer(text=f"{counter} commands used in this session!")
  await ctx.send(embed=embed)

@client.command()
async def stats(ctx):
  embed = discord.Embed(
    title = "Rocket Stats!",
    description = f"**How many servers?:**\n`{len(client.guilds)}`\n**How many members?:**\n`{sum(g.member_count for g in client.guilds)}`\n"
  )
  await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=f"This server has description which says: \n**{description}**",
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Server Owner:", value=owner, inline=True)
  embed.add_field(name="Server ID:", value=id, inline=True)
  embed.add_field(name="Region:", value=region, inline=True)
  embed.add_field(name="Member Count:", value=memberCount, inline=True)

  await ctx.send(embed=embed)

async def change():
  await client.wait_until_ready()

  statuses = [f"with {len(client.guilds)} servers!", f"Version 2!", f"{round(client.latency *1000)}ms", f"{sum(g.member_count for g in client.guilds)} members!", "you"]

  while not client.is_closed():

      status = random.choice(statuses)
      
      await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

      await asyncio.sleep(6)

import textwrap
import urllib
import aiohttp
import datetime

@bot.command(aliases = ['l', 'lyrc', 'lyric'])
async def lyrics(ctx, *, search = None):
    """A command to find lyrics easily!"""
    if not search:
        embed = discord.Embed(
            title = "No search argument!",
            description = "You havent entered anything, so i couldnt find lyrics!"
        )
        return await ctx.reply(embed = embed)
    
    song = urllib.parse.quote(search)
    
    async with aiohttp.ClientSession() as lyricsSession:
        async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata:
            if not 300 > jsondata.status >= 200:
                return await ctx.send(f'Recieved poor status code of {jsondata.status}')

            lyricsData = await jsondata.json()

    error = lyricsData.get('error')
    if error:
        return await ctx.send(f'Recieved unexpected error: {error}')

    songLyrics = lyricsData['lyrics']
    songArtist = lyricsData['author'] 
    songTitle = lyricsData['title']
    songThumbnail = lyricsData['thumbnail']['genius']
    for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace = False):
        embed = discord.Embed(
            title = songTitle,
            description = chunk,
            color = discord.Color.random(),
            timestamp = datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url = songThumbnail)
        await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(send_messages=True)
async def poll(ctx, *, reason=None):
  if not reason:
    await ctx.send("You cant make a poll about nothing!")
    return

  poll=discord.Embed(title="🎉 Its Time For A Poll! 🎉", description=f"{reason}", color=0x66CCCC)
  poll.set_footer(text=f"Poll made by {ctx.author.name}")
  message = await ctx.send(embed=poll)
  await message.add_reaction('👍')
  await message.add_reaction('👎')

@client.command()
async def ping(ctx):
  embed=discord.Embed(title = ":ping_pong: | Pong!", description=f"**{round(client.latency *1000)}** milliseconds!", color=discord.Color.random())
  await ctx.send(embed=embed)

@client.event
async def on_guild_join(guild):
    with open("json/prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "$"
    with open("json/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    
    owner = str(guild.owner)
    members = str(guild.member_count)
    description = str(guild.description)
    
    print(guild.name)
    print(owner)
    print(members)
    try:
      print(description)
    except:
      pass



@client.command(aliases = ['sp', 'prefix', 'cp', 'changeprefix'])
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):
  if not prefix:
    await ctx.send("You have to give me a prefix to set!")
    return
  with open("json/prefixes.json", "r") as f:
      prefixes = json.load(f)
  prefixes[str(ctx.guild.id)] = prefix
  with open("json/prefixes.json", "w") as f:
      json.dump(prefixes, f, indent=4)
  embed=discord.Embed(color=discord.Color.random())
  embed.set_author(name="New Prefix!")
  embed.add_field(name="New prefix:", value=f"'{prefix}'")
  embed.set_footer(text="Enjoy your new prefix!")
  await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    try:
      embed = discord.Embed(title=f"Cooldown is active, {ctx.message.author}!", description=f"Try again in {error.retry_after:.2f} seconds!", color=0xff0000)
      await ctx.send(embed=embed)
    except:
      await ctx.send("Looks like I dont have permission to send embeds, please give me the `Embed Links` permission!")
  elif isinstance(error, commands.MissingRequiredArgument):
    try:
      embed=discord.Embed(title="Whoops!", description="You missed something in that command!", color=0xff0000)
      embed.add_field(name="Error:", value=error)
      await ctx.send(embed=embed)
    except:
      await ctx.send("Looks like I dont have permission to send embeds, please give me the `Embed Links` permission!")
  elif isinstance(error, commands.BotMissingPermissions):
    embed=discord.Embed(title="Whoops!", description="Im missing the required permissions to kick this member, or their role is higher than me!", color=0xff0000)
    try:
      await ctx.send(embed=embed)
    except:
      await ctx.send("Looks like I dont have permission to send embeds, please give me the `Embed Links` permission!")
  elif isinstance(error, commands.NotOwner):
    try:
      embed=discord.Embed(title="Whoops!", description="This is a OWNER ONLY command! Which means only the bot creator can use this.", color=0xff0000)
      await ctx.send(embed=embed)
    except:
      await ctx.send("This command is owner only, but I need permissions to send embeds..")
  elif isinstance(error, CommandNotFound):
    embed = discord.Embed(
      title = "Error!",
      description = "Command not found!",
      color = 0xff0000
    )
    await ctx.send(embed=embed)

@client.event
async def on_guild_remove(guild):
    with open("json/prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))
    with open("json/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f"cogs.{filename[:-3]}")
        except Exception as e:
            print(e)

@client.event 
async def on_ready():
  print("Bot is online!")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."))

@client.event
async def on_message(message):
  if ':flat:' in message.content:
    await message.add_reaction("<:flat:834061743092531201>")
  await client.process_commands(message)

client.sniped_messages = {}

@client.command(aliases = ["snipeclear", "sc"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def clearsnipe(ctx):
  await ctx.send("Clearing snipe..", delete_after = 0.1)
  await ctx.send("Snipe was cleared! Enjoy! (Cooldown is 120 seconds)")

@client.event
async def on_message_delete(message):
    if message.attachments:
        bob = message.attachments[0]
        client.sniped_messages[message.guild.id] = (bob.proxy_url, message.content, message.author, message.channel.name, message.created_at)
    else:
        client.sniped_messages[message.guild.id] = (message.content,message.author, message.channel.name, message.created_at)

@client.command()
@commands.is_owner()
async def load(ctx):
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f"cogs.{filename[:-3]}")
            await ctx.send(f"Loaded cog: {filename}")
        except Exception as e:
            print(e)
# {'' if totalInvites > 1 else 's'}
# {totalInvites}
@client.command()
async def invites(ctx, user: discord.Member=None):
  if user == 'None':
    user = ctx.author
  totalInvites = 0
  for i in await ctx.guild.invites():
      member = ctx.message.guild.get_member_named(user)
      if i.inviter == member:
        totalInvites += i.uses
  embed = discord.Embed(
    title = "Invites!",
    description = f"{user.mention} has invited {totalInvites} member{'' if totalInvites > 1 else 's'} to this guild!",
    color = discord.Color.random()
  )
  await ctx.send(embed=embed)
@client.command()
@commands.is_owner()
async def unload(ctx):
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            client.unload_extension(f"cogs.{filename[:-3]}")
            print(f"Unloaded cog: \n {filename}")
            await ctx.send(f"Unloaded cog: {filename}")
        except Exception as e:
            print(e)

@client.command()
async def snipe(ctx):
    try:
        bob_proxy_url, contents,author, channel_name, time = client.sniped_messages[ctx.guild.id]
    except:
        contents,author, channel_name, time = client.sniped_messages[ctx.guild.id]
    try:
        embed = discord.Embed(description=contents , color=0x44CDCD, timestamp=time)
        embed.set_image(url=bob_proxy_url)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
        embed.set_footer(text=f"Deleted in : #{channel_name}")
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(description=contents , color=0x0000ff, timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
        embed.set_footer(text=f"Deleted in: #{channel_name}")
        await ctx.channel.send(embed=embed)

keep_alive()
client.loop.create_task(change())
client.run(os.environ['TOKEN'])