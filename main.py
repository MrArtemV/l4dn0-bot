import discord
from discord.ext import commands
from config import settings
import random

bot = commands.Bot(command_prefix=settings["prefix"])


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Hello, {author.mention}!")


@bot.command()
async def lrandom(ctx):
    text = "your random number:" + str(random.randint(1, 100))
    await ctx.send(text)

bot.run(settings['token'])
