import os
import discord
from pathlib import Path
from discord.ext import commands
from json import load
from logging import getLogger, Formatter, StreamHandler

# Logging configuration
logger = getLogger(__name__)

# Secret
secrets_path = Path("./secrets.json")
token = load(secrets_path.open("r"))["discord"]["token"] if secrets_path.exists() else ""

# Define the bot's prefix (what you type before commands)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, )

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

# Command: Respond to a simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Respond with a greeting
@bot.command()
async def hello(ctx):
    await ctx.send('Hello! How can I assist you today?')

# Run the bot with your token
bot.run(token)
