import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Zalogowano jako {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def hej(ctx):
    await ctx.send(f"Cześć, {ctx.author.name}!")

@bot.command()
async def pomoc(ctx):
    await ctx.send("Dostępne komendy: !ping, !hej, !pomoc")

bot.run(os.getenv("https://discord.com/oauth2/authorize?client_id=1398089779845005473&permissions=8&integration_type=0&scope=bot"))
