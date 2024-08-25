from pathlib import Path
from discord import Intents
from discord.ext import commands
from json import load
from log.botlog import BotLogger, INFO, ERROR, DEBUG

# Flamingly global configuration stuff
bot_name = "None"
bot_token = ""

# Secrets
secrets_path = Path("./secrets.json")

# Load stuff we need
if secrets_path.exists():
    # Make sure path exists, of course
    secrets_fp = secrets_path.open("r")
    json_data = load(secrets_fp)

    # Keys for consistency; they're gonna be used more than once
    discord_key = "discord"
    bindbot_key = "BindBot"
    name_key = "name"
    token_key = "token"

    # Error checking
    if discord_key not in json_data:
        print(f"No '{discord_key}' key in {str(secrets_path)}")
    elif bindbot_key not in json_data[discord_key]:
        print(f"No '{bindbot_key}' key in {str(secrets_path)}")
    else:
        if name_key not in json_data[discord_key][bindbot_key]:
            print(f"No '{name_key}' key in {str(secrets_path)}")
        else:
            bot_name = json_data[discord_key][bindbot_key][name_key]
        if token_key not in json_data[discord_key][bindbot_key]:
            print(f"No '{token_key}' key in {str(secrets_path)}")
        else:
            bot_token = json_data[discord_key][bindbot_key][token_key]
else:
    raise Exception("Secrets path does not exist")

# Setup for logging
logger = BotLogger(bot_name, DEBUG)

# Make sure token isn't empty
if len(bot_token) == 0:
    raise Exception("Token loaded but empty")

# Define the bot's prefix (what you type before commands)
intents = Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

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
bot.run(bot_token)
