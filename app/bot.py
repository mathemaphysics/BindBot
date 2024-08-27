from pathlib import Path
from discord import Intents, File
from discord.ext import commands
from util.logger import BotLogger, INFO, ERROR, DEBUG
from util.config import Configuration
from typing import Union

# Secrets
secrets_path = Path("./secrets.json")

# Make y'all's config
config = Configuration(secrets_path)

# Setup for logging
logger = BotLogger(config.name, DEBUG)

# Announce start with version
logger.info(f"{config.name} version {config.version}")

# Make sure token isn't empty
if len(config.token) == 0:
    raise Exception("Token loaded but empty")

# Define the bot's prefix (what you type before commands)
intents = Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name} ({bot.user.id})')

## Event: When message received
#@bot.event
#async def on_message(message):
#    logger.info(f'MessageID: {message.id} Author: {message.author} Content: {message.content}')

# Command: Respond to a simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Respond with a greeting
@bot.command()
async def hello(ctx):
    await ctx.send('Hello! How can I assist you today?')

@bot.command()
async def image(ctx, image_path: Union[str, Path] = ""):
    image_path_obj = Path(image_path)
    if not image_path_obj.exists():
        await ctx.send(f"Could not find {str(image_path_obj)}")
    else:
        with image_path_obj.open("rb") as fp:
            image_data = File(fp)
            await ctx.send(f"Argument: {str(image_path_obj)}")
            await ctx.send("Your image", file=image_data)

# Run the bot with your token
bot.run(config.token)
