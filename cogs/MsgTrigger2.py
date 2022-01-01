import discord
import asyncio
from discord.ext import commands
import random

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed only for main server


class MsgTrigger2(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        msgContent = msg.content

        # if msg was sent in DM (not in a guild)
        if msg.guild == None:
            try:
                react = self.bot.get_emoji(
                    579882318664302592)  # thanos ugh emote
                await msg.add_reaction(react)
                channel = self.bot.get_channel(
                    550456326053036034)  # msg log channel
                await channel.send(f'{msg.author.mention} said in DM: `{msg.content}`')
            except discord.HTTPException:
                pass
            return

        # if not main server, then return
        if msg.guild.id != 256988924390408193:
            return

        # Auto add vote reactions in meme channel or suggestions channel
        if msg.channel.id == 459767444437729280 or msg.channel.id == 838570502091833345:
            up = self.bot.get_emoji(592355631667740683)
            down = self.bot.get_emoji(592355631877324820)
            try:
                await msg.add_reaction(up)
                await msg.add_reaction(down)
            except discord.errors.Forbidden:
                # cannot react to message
                pass

        # Weeb channel auto delete: non-embed gif/link, discord link
        if msg.channel.id == 332674779213463553:
            if "//v.redd.it/" in msgContent or "discord.gg" in msgContent:
                try:
                    await msg.delete()
                except discord.HTTPException:
                    pass

        # Auto add random reaction in epic_boosters channel
        if msg.channel.id == 838530366997266432:
            react_list = [590614599515111440, 601185935714943005, 597917965178109952, 594177649266524160,
                          645117585918132224, 594175419801141273, 645117585704091681, 645117585767006219,
                          588780698693795840, 590614599590739968, 645117584743858196, 642785362124472363]

            rand_react = self.bot.get_emoji(random.choice(react_list))
            await msg.add_reaction(rand_react)


def setup(bot):
    bot.add_cog(MsgTrigger2(bot))
