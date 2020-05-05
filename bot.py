import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='j!')  # create bot with prefix

# read from settings file
f = open("settings.txt", "r")
flines = f.readlines()
for l in flines:
    if l.startswith("TOKEN"):
        tokenLine = l.split('{', 1)
        TOKEN = tokenLine[1][:-1]
    else:
        print('TOKEN not found!')

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


@bot.event
async def on_connect():
    appInfo = await bot.application_info()
    print(f'Bot Owner: {appInfo.owner.name}#{appInfo.owner.discriminator}')
    print('Successfully connected to Discord...')

# @bot.event
# async def on_disconnect():
#     cogStrList = bot.cogs.keys()
#     #unload the cogs to prevent error
#     for cog in cogStrList:
#         bot.unload_extension(f'cogs.{cog}')


@bot.event
async def on_ready():
    # print the logic from line 17
    print(f'Loaded {cogcount} cogs: {coglist[:-3]}')

    membercount = 0
    for member in bot.get_all_members():
        membercount += 1
    print(f'{membercount} members total')

    serverlist = ''
    guilds = await bot.fetch_guilds().flatten()
    for guild in guilds:
        serverlist += guild.name+' | '
    print(f'In {len(guilds)} servers: {serverlist[:-3]}')

    print('\nBOT IS READY!')

bot.run(TOKEN)
