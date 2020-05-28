import discord
from discord.ext import commands
import os

# read from settings file
f = open("settings.txt", "r")
flines = f.readlines()
for l in flines:
    l=l.strip()
    if l.startswith("TOKEN"):
        tokenLine = l.split('{', 1)
        TOKEN = tokenLine[1][:-1]
    elif l.startswith("PREFIX"):
        prefixLine = l.split('{', 1)
        PREFIX = prefixLine[1][:-1]

bot = commands.Bot(command_prefix=PREFIX,case_insensitive=True)

@bot.event
async def on_connect():
    appInfo = await bot.application_info()
    print(f'Bot Owner: {appInfo.owner.name}#{appInfo.owner.discriminator}  |  Bot Prefix: {PREFIX}')
    print('Successfully connected to Discord...')

    # load the cogs
    cogStrList = bot.cogs.keys()
    cogcount = 0
    coglist = ''
    for filename in os.listdir('./cogs'):
        cogName = filename[:-3]  # without the '.py' part
        if filename.endswith('.py') and cogName not in cogStrList:
            bot.load_extension(f'cogs.{cogName}')
            cogcount += 1
            coglist += filename+' | '

    bot.load_extension('jishaku')
    print("Loaded jishaku: https://pypi.org/project/jishaku/")
    print(f'Loaded {cogcount} cogs: {coglist[:-3]}')

@bot.event
async def on_ready():

    membercount = 0
    for member in bot.get_all_members():
        membercount += 1

    serverlist = ''
    guilds = await bot.fetch_guilds().flatten()
    for guild in guilds:
        serverlist += guild.name+' | '

    print(f'{membercount} members total')
    print(f'In {len(guilds)} servers: {serverlist[:-3]}')
    print('\nBOT IS READY!')

bot.run(TOKEN)
