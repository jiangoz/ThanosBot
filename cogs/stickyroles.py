import discord
import asyncio
from discord.ext import commands

class StickyRoles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(aliases=["stickyrole"])
    @commands.is_owner()
    async def stickyroles(self, ctx: commands.Context) -> None:
        """| Add/remove roles to be re-applied on join"""
        pass
    
    
def setup(bot):
    bot.add_cog(StickyRoles(bot))