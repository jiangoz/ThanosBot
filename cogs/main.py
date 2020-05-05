import discord
import asyncio
from discord.ext import commands


class Main(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog):
        """| load a cog from cogs folder"""
        self.bot.load_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} was loaded')

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog):
        """| unload a cog from cogs folder"""
        self.bot.unload_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} was un-loaded')

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog):
        """| reload cog - use it after u make changes"""
        self.bot.reload_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} was re-loaded')

    @commands.command()
    @commands.is_owner()
    async def servers(self, ctx):
        """| list the servers using this bot"""
        serverlist = ''
        guilds = await self.bot.fetch_guilds().flatten()
        for guild in guilds:
            serverlist += guild.name+' | '
        await ctx.send(f'In {len(guilds)} servers: {serverlist[:-3]}')

    @commands.command()
    @commands.is_owner()
    async def cogs(self, ctx):
        """| list the cogs being used"""
        cogStrList = self.bot.cogs.keys()
        output = ''
        for cog in cogStrList:
            output += cog+' | '
        await ctx.send(f'Using {len(cogStrList)} cogs: {output[:-3]}')


def setup(bot):
    bot.add_cog(Main(bot))
