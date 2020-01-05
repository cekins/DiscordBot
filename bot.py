import os
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

os.environ['Path'] += os.pathsep + os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ffmpeg\\bin')

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print('Bot Ready')


@bot.command()
async def run(ctx):
    vchan = ctx.message.author.voice.channel
    vcon = await vchan.connect()
    vcon.play(discord.FFmpegPCMAudio('audio/run.mp3'))
    while vcon.is_playing():
        pass
    await vcon.disconnect()






bot.run(token)
