
import discord
from discord.ext import commands
from random import randint
import aiohttp

import os

# dotenv.load_dotenv()

client = discord.Client()

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        num = randint(0,2)
        if num == 0:
            await ctx.send("It's heads")
        elif num == 1:
            await ctx.send("No")
        else:
            await ctx.send("It's tails")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Conducting'))

async def on_message(message):
    if message.author == bot.user:
        return

    print(f"{message.guild} - {message.channel} - {message.author} <{message.author.id}>: {message.content}")

bot = commands.Bot(command_prefix=commands.when_mentioned_or("conductor-"))

bot.add_listener(on_ready)
bot.add_listener(on_message)

bot.add_cog(MyCog(bot))
bot.run("NzcwNzM1Mzc2MjI2NDUxNDU2.X5h5QQ.fGnsAjAsAhJoQ6KYhdxBDxo-uMg")
