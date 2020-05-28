import discord
import asyncio
from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    @commands.is_owner()
    async def set(self, ctx):
        """| set the status and presence"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help("set")

    @set.command()
    async def status(self, ctx, status: str.lower):
        """| set online, idle, dnd, invis"""
        thanosOK = self.bot.get_emoji(
            585580175031533597)  # thanos OK hand emote

        if status == 'online':
            await self.bot.change_presence(status=discord.Status.online)
            await ctx.message.add_reaction(thanosOK)
        elif status == 'idle':
            await self.bot.change_presence(status=discord.Status.idle)
            await ctx.message.add_reaction(thanosOK)
        elif status == 'dnd':
            await self.bot.change_presence(status=discord.Status.dnd)
            await ctx.message.add_reaction(thanosOK)
        elif status == 'invis' or status == 'invisible':
            await self.bot.change_presence(status=discord.Status.invisible)
            await ctx.message.add_reaction(thanosOK)
        else:
            await ctx.send('Invalid status...try again')

    @set.command()
    async def game(self, ctx, *, gameName: str):
        """| set bot to playing something"""
        await self.bot.change_presence(activity=discord.Game(name=gameName))
        await ctx.message.add_reaction(self.bot.get_emoji(585580175031533597))

    @set.command()
    async def stream(self,ctx, streamURL:str, *,streamName:str):
        """| set bot to stream something"""
        if "https://" in streamURL:
            await self.bot.change_presence(activity=discord.Streaming(name=streamName, url=streamURL))
            await ctx.message.add_reaction(self.bot.get_emoji(585580175031533597))
        else:
            await self.bot.change_presence(
                activity=discord.Streaming(name=streamName, url=f"https://twitch.tv/{streamURL}"))
            await ctx.message.add_reaction(self.bot.get_emoji(585580175031533597))

    @set.command()
    async def listen(self, ctx, *, songName: str):
        """| set bot to listen to something"""
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=songName))
        await ctx.message.add_reaction(self.bot.get_emoji(585580175031533597))

    @set.command()
    async def watch(self, ctx, *, itemName: str):
        """| set bot to watch something"""
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=itemName))
        await ctx.message.add_reaction(self.bot.get_emoji(585580175031533597))

    # @set.command() # SADLY bots can't use custom activity!!!
    # async def customActivity(self,ctx,emoji=None,*,activityName:str):

def setup(bot):
    bot.add_cog(Misc(bot))
