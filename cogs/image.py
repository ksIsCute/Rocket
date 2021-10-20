import discord
import asyncio
import json
import aiohttp
import datetime
import random
import io
import requests
import numpy as np
import cv2 as cv
from datetime import datetime
from discord.ext import commands
import PIL
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from io import BytesIO

class Images(commands.Cog):
    """ Category for image commands """

    def __init__(self, client):
        self.client = client
        self.ses = aiohttp.ClientSession()
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog: Image, Is Ready.')

    @commands.command()
    async def dog(self, ctx):
      async with aiohttp.ClientSession() as session:
          request = await session.get('https://some-random-api.ml/img/dog') 
          dogjson = await request.json() 
      embed = discord.Embed(title="Doggo!", color=discord.Colour.random()) 
      embed.set_image(url=dogjson['link']) 
      embed.set_footer(text="Woof")
      await ctx.send(embed=embed)

    @commands.command()
    async def fox(self, ctx):
      async with aiohttp.ClientSession() as session:
          request = await session.get('https://some-random-api.ml/img/fox') 
          foxjson = await request.json() 
      embed = discord.Embed(title="Fox!!", color=discord.Colour.random()) 
      embed.set_image(url=foxjson['link']) 
      embed.set_footer(text="What noise does a fox make :/")
      await ctx.send(embed=embed)

    @commands.command()
    async def panda(self, ctx):
      async with aiohttp.ClientSession() as session:
          request = await session.get('https://some-random-api.ml/img/panda') 
          pandajson = await request.json() 
      embed = discord.Embed(title="Panda!!", color=discord.Colour.random()) 
      embed.set_image(url=pandajson['link']) 
      embed.set_footer(text="i like bamboo")
      await ctx.send(embed=embed)

    @commands.command()
    async def bird(self, ctx):
      async with aiohttp.ClientSession() as session:
          request = await session.get('https://some-random-api.ml/img/birb') 
          birbjson = await request.json() 
      embed = discord.Embed(title="berb!", color=discord.Colour.random()) 
      embed.set_image(url=birbjson['link']) 
      embed.set_footer(text="birb pecc")
      await ctx.send(embed=embed)

    @commands.command()
    async def rip(self, ctx, member: discord.Member=None):
      if not member:
        member = ctx.author


      gravestone = Image.open("images/Gravestone.jpeg")

      asset = member.avatar_url_as(size=128)
      data = BytesIO(await asset.read())
      pfp = Image.open(data) 
      pfp = pfp.resize((470,588))
      gravestone.paste(pfp, (341,353))
      gravestone.save("images/output/gravestone.jpg")
      try:
        await ctx.send(file = discord.File("images/output/gravestone.jpg"))
      except:
        await ctx.send("I was not able to send the final image. Please give me picture permission.")

    @commands.command()
    async def wanted(self, ctx, user : discord.Member = None):
        if user == None:
          user = ctx.author

        wanted = Image.open("images/Wanted.jpeg")
        
        asset = user.avatar_url_as(size = 128)

        data = BytesIO(await asset.read())

        pfp = Image.open(data)
        pfp = pfp.resize((106,106))

        wanted.paste(pfp, (41,85))

        wanted.save("images/output/wanted.jpg")
        await ctx.send(file = discord.File("images/output/wanted.jpg"))
   
    @commands.command(aliases=['cmm'])
    async def changemymind(self, ctx, *, msg="No text entered"):
        async with aiohttp.ClientSession() as ses:
            async with ses.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={msg}") as f:
                if f.status in range(200, 299):
                    dat = await f.json()
                    img = dat['message']
                    em = discord.Embed(
                        title='Change My Mind.',
                        color = discord.Colour.random()
                    )
                    em.set_image(url=f'{img}')
                    await ctx.send(embed=em)
                    await ses.close()
                else:
                    await ctx.reply("Error when trying to change my mind.")
                    await ses.close()

    @commands.command(aliases=['ytc', 'ytcomment'])
    async def youtubecomment(self, ctx, member: discord.Member=None, *, text = "No text entered."):
      if not member:
        member = ctx.author
      
      async with aiohttp.ClientSession() as wastedSession:
          async with wastedSession.get(f'https://some-random-api.ml/canvas/youtube-comment?avatar={member.avatar_url_as(format="png", size=1024)}&username={member.display_name}&comment={text}') as wastedImage:
              imageData = io.BytesIO(await wastedImage.read()) 
              await wastedSession.close()
              
              await ctx.reply(file=discord.File(imageData, 'ytcomment.png'))
    
def setup(client):
    client.add_cog(Images(client))