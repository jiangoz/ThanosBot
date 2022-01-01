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
        try:
            self.bot.load_extension(f'cogs.{cog}')
            await ctx.send(f'{cog} was loaded successfully')
        except commands.ExtensionAlreadyLoaded:
            await ctx.send(f'{cog} is already loaded. Try using reload')
        except commands.ExtensionFailed:
            await ctx.send(f'setup function for {cog} had an execution error')
        except commands.ExtensionNotFound:
            await ctx.send(f'{cog} was not found in cogs directory')

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog):
        """| unload a cog from cogs folder"""
        try:
            self.bot.unload_extension(f'cogs.{cog}')
            await ctx.send(f'{cog} was un-loaded successfully')
        except commands.ExtensionNotLoaded:
            await ctx.send(f'{cog} failed to unload. Try using reload')

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog):
        """| reload cog - use it after u make changes"""
        try:
            self.bot.reload_extension(f'cogs.{cog}')
            await ctx.send(f'{cog} was re-loaded successfully')
        except commands.ExtensionNotLoaded:
            await ctx.send(f'{cog} failed to load')
        except commands.ExtensionNotFound:
            await ctx.send(f'{cog} was not found in cogs directory')
        except commands.ExtensionFailed:
            await ctx.send(f'setup function for {cog} had an execution error')

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
