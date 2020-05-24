import discord
import asyncio
from discord.ext import commands


class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['addMemeVoteReact'])
    @commands.is_owner()
    async def addMemeVoteReacts(self, ctx, limit=30):
        """| add vote reactions to the last <num> msgs in meme channel"""
        memeChannel = self.bot.get_channel(459767444437729280)
        messages = await memeChannel.history(limit=limit).flatten()
        up = self.bot.get_emoji(592355631667740683)
        down = self.bot.get_emoji(592355631877324820)
        upcount = 0
        downcount = 0
        for msg in messages:
            if up not in (react.emoji for react in msg.reactions):
                await msg.add_reaction(up)
                upcount += 1
            if down not in (react.emoji for react in msg.reactions):
                await msg.add_reaction(down)
                downcount += 1
        await ctx.send(f'Added {upcount} upvote reacts and {downcount} downvote reacts')

    @commands.command(aliases=['cleanWeebGif'])
    @commands.is_owner()
    async def cleanWeebGifs(self, ctx, limit=20):
        """| go thru <num> msgs in weeb channel & delete non-embedded gifs"""
        weebChannel = self.bot.get_channel(332674779213463553)
        messages = await weebChannel.history(limit=limit).flatten()
        delCount = 0
        for msg in messages:
            if "//v.redd.it/" in msg.content.lower():
                await msg.delete()
                delCount += 1
        await ctx.send(f'Deleted {delCount} non-embedded gif links')

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
