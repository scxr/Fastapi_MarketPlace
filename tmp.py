import discord, asyncio
from discord.ext import commands
import os
os.system('cls')
print(r"""auto dbumper made by xo#0111""")
TOKEN = 'your token here'
client = discord.Client()
prefix = '~'
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print('We have reached alive status !!')

@bot.command(pass_context=True)
async def dbump(ctx):
    while 1:
        try:
            print('Bumped, waiting 2 hours before bumping again')
            await ctx.message.channel.send('!d bump')
        except:
            pass
        await asyncio.sleep(1)

bot.run(TOKEN, bot=False)