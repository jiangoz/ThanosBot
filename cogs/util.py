import discord
import asyncio
from discord.ext import commands

class Util(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def ping(self,ctx):
        """| pong! returns latency"""
        await ctx.send(f'Pong! {round(self.bot.latency*1000)}ms')

def setup(bot):
    bot.add_cog(Util(bot))