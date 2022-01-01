import discord
import asyncio
from discord.ext import commands
from pathlib import Path
import random
import json

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed only for main server


class MsgTrigger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        # fetch reaction data paths
        triggerPath = Path(__file__).parents[1].joinpath(
            "data", "reactionTrigger.json")
        msgPath = Path(__file__).parents[1].joinpath(
            "data", "reactionMsg.json")

        # for specific trigger standalone words
        with open(triggerPath) as t:
            self.triggerReacts: dict = json.load(t)

        # for any wildcards match in msg/sentence
        with open(msgPath) as m:
            self.msgReacts: dict = json.load(m)

    @commands.Cog.listener()
    async def on_message(self, msg):
        msgContentLower = msg.content.lower()
        trigger = msgContentLower.split()

        # if msg was sent in DM (not in a guild)
        if msg.guild == None:
            return

        # if not main server, then return
        if msg.guild.id != 256988924390408193:
            return

        try:
            botrole = msg.guild.get_role(272888325940051969)  # get bot role
            demigod1 = msg.guild.get_role(257006648583913472)  # demigod I
            demigodv = msg.guild.get_role(310541971179700224)  # demigod V
            authorRoles = msg.author.roles
            authorTopRole = msg.author.top_role  # member's highest role
        except AttributeError:
            return

        # if msg from bots
        if botrole in authorRoles:
            return

        try:
            # Emote reaction triggers

            for t in self.triggerReacts.keys():
                if t in trigger:
                    react = self.bot.get_emoji(self.triggerReacts.get(t))
                    await msg.add_reaction(react)

            for m in self.msgReacts.keys():
                if m in msgContentLower:
                    react = self.bot.get_emoji(self.msgReacts.get(m))
                    await msg.add_reaction(react)

            if msgContentLower == "no u":
                await msg.channel.send("<:ThanosNOU:571052438619029524>")
            if "owo" in trigger:  # owo combo emotes!
                o1 = self.bot.get_emoji(490916040964964354)
                w2 = self.bot.get_emoji(490916041166159872)
                o3 = self.bot.get_emoji(490921532734963722)
                await msg.add_reaction(o1)
                await asyncio.sleep(0.1)
                await msg.add_reaction(w2)
                await asyncio.sleep(0.1)
                await msg.add_reaction(o3)
            if "220997668355178496" in msg.content:  # ping jiango
                emote = self.bot.get_emoji(560468390154731530)
                await msg.add_reaction(emote)
            if ("jiango" in msgContentLower) and (":" not in msgContentLower):
                emote = self.bot.get_emoji(784468115298975805)  # me
                emote2 = self.bot.get_emoji(839690866289016852)  # pepe
                await msg.add_reaction(emote)
                await msg.add_reaction(emote2)
            if "436643551993004033" in msg.content or "thano" in msgContentLower:  # ping thanos
                t1 = self.bot.get_emoji(611039828003389440)
                t2 = self.bot.get_emoji(585580175031533597)
                await msg.add_reaction(t1)
                await msg.add_reaction(t2)
                # pull a random quote from file
                relpath = Path(__file__).parents[1].joinpath(
                    "data", "thanosquotes.txt")
                with open(relpath, "r") as f:
                    quote_list = f.readlines()
                await msg.channel.send(random.choice(quote_list))
            if "jojo" in msgContentLower or "jjba" in trigger:
                emote1 = self.bot.get_emoji(540669998725857290)
                emote2 = self.bot.get_emoji(540669998834909194)
                emote3 = self.bot.get_emoji(540669998809481276)
                await msg.add_reaction(emote1)
                await msg.add_reaction(emote2)
                await msg.add_reaction(emote3)

            # unflip the damn table!
            if "(╯°□°）╯︵ ┻━┻" in msg.content:
                await msg.channel.send("┬─┬ ノ( ゜-゜ノ)")

        except discord.HTTPException:
            pass


def setup(bot):
    bot.add_cog(MsgTrigger(bot))
