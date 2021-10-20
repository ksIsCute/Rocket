import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['addrole', 'removerole', 'r'])
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, user: discord.Member, *, role: discord.Role):
      if role.position > ctx.author.top_role.position:
        return await ctx.send('**:x: | That role is above your top role!**')
      if role in user.roles:
          await user.remove_roles(role)
          await ctx.send(f"**Removed {role} from {user.mention}**")
      else:
          await user.add_roles(role)
          await ctx.send(f"**Added {role} to {user.mention}!**")

    @commands.Cog.listener()
    async def on_ready(self):
      print("Cog: Mod, Is Ready!") 
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, user: discord.Member, *, reason = None):
      if not reason:
        await user.kick(reason = f"Responsible user: {ctx.author}")
        await ctx.send(f"**{user}** has been kicked for **No Reason Provided**.")
      else:
        await user.kick(reason=reason)
        await ctx.send(f"**{user}** has been kicked for **{reason}**.")
      
    @commands.command(aliases = ['hb', 'b'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No Reason Provided"):
      if member is ctx.author:
        await ctx.send("You cannot ban yourself!")
        return
      if member.guild_permissions.administrator and member != None:
        fail = discord.Embed(
          title = "Administrator.",
          description = "That user is an administrator so I cannot ban them.",
          color = discord.Colour.random()
        )
        await ctx.send(embed=fail)
        return
      else:
        embed=discord.Embed(
          title = "Banned!",
          description = f"{member} has been banned sucsessfully!",
          color = discord.Colour.random()
        )
        try:
          await member.ban(reason=reason)
        except:
          await ctx.send("I do not have the required permissions to ban, or they are higher than me!")
        try:
          await member.send(f"You have been banned from {ctx.guild.name} for {reason}.")
        except:
          await ctx.send("I couldnt dm them for their ban reason..")
        await ctx.send(embed=embed)
    @commands.command(aliases = ['n'])
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        if channel == None: 
            await ctx.send("You did not mention a channel!")
            return

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="Has been Nuked!")
            await nuke_channel.delete(reason=f"Responsible user: {ctx.author}")
            embed=discord.Embed(title="Channel Nuked!", description=f"Channel was destroyed and rebuilt by {ctx.message.author}!", color=discord.Colour.random())
            embed.set_image(url="https://media2.giphy.com/media/oe33xf3B50fsc/giphy.gif?cid=e96d9011mg8bzhy34bcfnsst91z7dbys429b3ux2z5jieecl&rid=giphy.gif&ct=g")
            await new_channel.send(embed=embed)

        else:
            await ctx.send(f"No channel named {channel.name} was found!")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send('**:x: | You do not have permission to use this command!**')     
        return 

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
      mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

      await member.remove_roles(mutedRole, reason=reason)
      embed = discord.Embed(title="Member unmuted!", description=f" Unmuted: {member.mention}",colour=discord.Color.random())
      embed.add_field(name="Notes: ", value=reason, inline=False)
      embed.set_footer(text=f"Muted by {ctx.message.author}")
      await ctx.send(embed=embed)
      await member.send(f" You are now unmuted from: {ctx.guild.name}, Notes: **{reason}**")

    @commands.command(description="Mutes the specified user.")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
        try:
            embed = discord.Embed(title="Member Muted", description=f"{member.mention} was muted ", colour=discord.Color.random())
            embed.add_field(name="Because:", value=reason, inline=False)
            await ctx.send(embed=embed)
        except:
            await ctx.send("The member was muted. But please give me the embed links permission.")
        try:
          await member.add_roles(mutedRole, reason=reason)
        except:
          await ctx.send("I do not have the required permission to mute this member!")
        await member.send(f" You have been muted from: {guild.name} For: {reason}")
  
    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
      lemet = 1001
      if amount > lemet:
        await ctx.send("Thats too much! You can only purge up to 1000 messages at a time!")
        return
      deleted = await ctx.channel.purge(limit=amount+1)
      await ctx.send(f"**<a:RocketCheck:831796328937291816> | Deleted {len(deleted)} messages**", delete_after=2)


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        try:
          await ctx.channel.edit(slowmode_delay=seconds)
          await ctx.send(f"**:clock10: | Set the slowmode delay in this channel to {seconds} seconds!**")
        except:
          await ctx.send("**<:Denied:829503280161882163> | I dont have the required permissions to perform this action!**")

def setup(bot):
    bot.add_cog(mod(bot))