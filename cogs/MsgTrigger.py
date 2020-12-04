import discord
import asyncio
from discord.ext import commands
from pathlib import Path
import random

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed only for Heavenly Realm


class MsgTrigger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        msgContentLower = msg.content.lower()
        trigger = msgContentLower.split()

        # if msg was sent in DM (not in a guild)
        if msg.guild == None:
            return

        # if not Heavenly, then return
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
            if "f" in trigger:
                femote = self.bot.get_emoji(471008964021059586)
                await msg.add_reaction(femote)
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
            if "jiango" in msgContentLower:
                emote = self.bot.get_emoji(784468115298975805)
                await msg.add_reaction(emote)
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
            if "gay" in msgContentLower:
                emote = self.bot.get_emoji(480073530466107392)
                await msg.add_reaction(emote)
            if "cring" in msgContentLower:
                emote = self.bot.get_emoji(441709985026539520)
                await msg.add_reaction(emote)
            if "jojo" in msgContentLower or "jjba" in trigger:
                emote1 = self.bot.get_emoji(540669998725857290)
                emote2 = self.bot.get_emoji(540669998834909194)
                emote3 = self.bot.get_emoji(540669998809481276)
                await msg.add_reaction(emote1)
                await msg.add_reaction(emote2)
                await msg.add_reaction(emote3)
            if "deus" in msgContentLower or "vult" in msgContentLower:
                emote = self.bot.get_emoji(416072792560238592)
                await msg.add_reaction(emote)
            if "crusade" in msgContentLower or "templar" in msgContentLower:
                emote = self.bot.get_emoji(480073411532554242)
                await msg.add_reaction(emote)

            # unflip the damn table!
            if "(╯°□°）╯︵ ┻━┻" in msg.content:
                await msg.channel.send("┬─┬ ノ( ゜-゜ノ)")

            # howdy greeting - only for lurkers/newfags
            if (authorTopRole <= demigod1 or demigodv not in authorRoles) and (msgContentLower.startswith("hi") or
                                                                               msgContentLower.startswith("hey") or
                                                                               msgContentLower.startswith("hello") or 
                                                                               msgContentLower.startswith("hai") or
                                                                               msgContentLower.startswith("howdy") or
                                                                               msgContentLower.startswith("sup")):

                await msg.channel.send(f'{msg.author.mention} Howdy! <:TipHat:585587679798886411>')
                await msg.channel.send("<:GWjiangoPepeFedora:389447036329656323> <a:0PepeHowdy:594175419801141273>")

            # send invite link (rick roll)
            link = "https://discordapp.com/channels/256988924390408193/256994533299060746/521483972241391616"
            if (authorTopRole <= demigod1 or demigodv not in authorRoles) and "inv" in msgContentLower and \
                                                                            ("?" in msgContentLower or
                                                                           "what" in msgContentLower or
                                                                           "where" in msgContentLower or
                                                                           "how" in msgContentLower or
                                                                           "link" in msgContentLower or
                                                                           "why" in msgContentLower):
                await msg.channel.send(f"{msg.author.mention} {link}",
                                       embed=discord.Embed(title="Click Here for Invite Link",
                                                           url="https://youtu.be/dQw4w9WgXcQ"))
                pass

        except discord.HTTPException:
            pass


def setup(bot):
    bot.add_cog(MsgTrigger(bot))
