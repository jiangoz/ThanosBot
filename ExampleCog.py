import discord
import asyncio
from discord.ext import commands
from discord import app_commands


class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        msgContent = msg.content.lower()
        pass

    @commands.command()
    @commands.is_owner()
    async def cmd(self, ctx):
        pass

    @app_commands.command(name="slash")
    async def slash_cmd(self, interaction: discord.Interaction) -> None:
        """/slash"""
        await interaction.response.send_message(f'Slash and global command',
                                                ephemeral=True)


def setup(bot):
    bot.add_cog(Example(bot))
