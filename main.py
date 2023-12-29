import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def len_word(ctx, word):
    lenword = len(word)
    await ctx.send('Длинна вашего слова ', word)

bot.run("MTE4ODg0ODc2MTU5MDUyNjAwMg.GpIYHa.JbUus-TLZPpDZYq9cErw76qeckXT5tnObiADCc")