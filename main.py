import inspirobot, os  # Import the libary
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(bot.user)

@bot.command()
async def inspire(ctx):
    quote = inspirobot.generate()
    await ctx.send(quote.url)

bot.run(os.getenv("DISCORD_TOKEN"))