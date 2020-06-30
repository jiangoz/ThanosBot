import discord
import asyncio
from discord.ext import commands

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed only for Heavenly Realm
class MsgTrigger2(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        msgContent = msg.content

        # if msg was sent in DM (not in a guild)
        if msg.guild == None:
            react = self.bot.get_emoji(579882318664302592)  # thanos ugh emote
            await msg.add_reaction(react)
            channel = self.bot.get_channel(
                550456326053036034)  # msg log channel
            await channel.send(f'{msg.author.mention} said in DM: {msg.content}')
            return

        # if not Heavenly, then return
        if msg.guild.id != 256988924390408193:
            return

        # Auto add vote reactions in meme channel
        if msg.channel.id == 459767444437729280:
            up = self.bot.get_emoji(592355631667740683)
            down = self.bot.get_emoji(592355631877324820)
            await msg.add_reaction(up)
            await msg.add_reaction(down)

        # Auto delete non-embedded gifs in weeb channel
        if msg.channel.id == 332674779213463553 and "//v.redd.it/" in msgContent:
            await msg.delete()


def setup(bot):
    bot.add_cog(MsgTrigger2(bot))
