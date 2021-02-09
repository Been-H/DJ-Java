#imports
import discord
from discord.ext import commands
from random import randint

import aiohttp
import youtube_dl
import os

# dotenv.load_dotenv()

#setup
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality': '192'
    }]
}
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
    async def play(self, ctx, arg):
        song = os.path.isfile("song.mp3")
        try:
            if song:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")

        if ctx.author.voice is None or ctx.author.voice.channel == None:
            await ctx.send("You don't appear to be in a channel. Join one and I'll play some music for you in there! :)")
        else:

            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                vc = await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)
                vc = ctx.voice_client
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([arg])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
            voice.play(discord.FFmpegPCMAudio("song.mp3"))

async def on_message(message):
    if message.author == client.user:
        return

    print(f"{message.guild} - {message.channel} - {message.author} <{message.author.id}>: {message.content}")



client.add_listener(on_message)

client.add_cog(MyCog(client))
client.run(TOKEN)
