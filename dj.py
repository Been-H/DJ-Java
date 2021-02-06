#imports
import discord
from discord.ext import commands
from random import randint
import aiohttp
from youtube_dl import YoutubeDL
import os

# dotenv.load_dotenv()

#setup
audio_downloder = YoutubeDL({'format':'bestaudio'})
client = commands.Bot(command_prefix=commands.when_mentioned_or("dj/"))

#commands
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
    
    @commands.command()
    async def play(self, ctx, *args):
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="Studying")
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        await voiceChannel.connect()
        [await ctx.send(arg) for arg in args]

async def on_message(message):
    if message.author == client.user:
        return

    print(f"{message.guild} - {message.channel} - {message.author} <{message.author.id}>: {message.content}")



client.add_listener(on_message)

client.add_cog(MyCog(client))
client.run("ODA1NjQwMzExOTg4Mjg5NTU3.YBd1Ag.PEkzrvUFclI6i0IVgF1yr3UQ_eI")
