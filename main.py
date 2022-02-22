import discord
from discord.ext import commands
from config import settings
from imageparser import ImageLinkHTMLParser
import random
import requests

bot = commands.Bot(command_prefix=settings["prefix"])


@bot.event
async def on_ready():
    print(f"Logged as {bot.user}")


@bot.command()
async def hello(ctx, extend=""):
    author = ctx.message.author
    await ctx.send(f"Hello, {author.mention}! {extend}")


@bot.command()
async def lrandom(ctx):
    text = "your random number:" + str(random.randint(1, 100))
    await ctx.send(text)


@bot.command()
async def nh(ctx, manga_id, number=1):
    r = requests.get(f"http://nhentai.net/g/{str(manga_id)}")
    parser = ImageLinkHTMLParser()
    parser.feed(r.text)
    linklist = parser.linklist
    embed = discord.Embed(color=0x1fa398, title=f"страница №{number}, манга {manga_id}")
    embed.set_image(url=linklist[number-1])
    await ctx.send(embed=embed)


bot.run(settings['token'])
