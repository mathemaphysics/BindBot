import discord
from pathlib import Path
from discord.ext import commands
from json import load
from log.botlog import BotLogger, INFO, ERROR, DEBUG

# Setup for logging
logger = BotLogger(__name__, DEBUG)

# Secret
secrets_path = Path("./secrets.json")
token = ""
if secrets_path.exists():
    secrets_fp = secrets_path.open("r")
    json_data = load(secrets_fp)
    token = json_data["discord"]["token"]
else:
    raise Exception("Secrets path does not exist")

# Define the bot's prefix (what you type before commands)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, )

# Event: When the bot is ready
@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name} ({bot.user.id})')

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
