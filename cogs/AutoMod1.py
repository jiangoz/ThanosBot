import discord
import asyncio
from discord.ext import commands
import random
import emoji

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed only for main server


class AutoMod1(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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
            authorTopRole = msg.author.top_role  # member's highest role
            viprole = msg.guild.get_role(388850225881546752)
            botrole = msg.guild.get_role(272888325940051969)
            demigodX = msg.guild.get_role(340275236865966090)  # demigod X
            demigodV = msg.guild.get_role(310541971179700224)  # demigod v
            demigod1 = msg.guild.get_role(257006648583913472)  # demigod 1
            authorRoles = msg.author.roles
        except AttributeError:
            return

        # if msg from bots
        if botrole in authorRoles:
            return

        # Auto moderate emote chat  #Only custom/global emotes allowed
        if msg.channel.id == 459893562130300928:
            if msgContentLower.startswith('<:') and msgContentLower.endswith('>'):
                pass
            elif msgContentLower.startswith('<a:') and msgContentLower.endswith('>'):
                pass
            elif all(em in emoji.UNICODE_EMOJI_ENGLISH for em in msg.content):
                pass
            else:
                try:
                    await msg.delete()
                    channel = self.bot.get_channel(
                        416385919919194113)  # spam channel
                    await channel.send(f'{msg.author.mention} Your msg was deleted in <#459893562130300928> '
                                       + '(it is only for ***CUSTOM EMOTES***)')
                    return
                except discord.HTTPException:
                    pass

        # delete Nitro or gift links
        if "discord.gift/" in msgContentLower:
            try:
                await msg.delete()
                return
            except discord.HTTPException:
                pass

        # delete and kick nitro scammers
        if "nitro" in msgContentLower and demigod1 not in authorRoles:
            try:
                await msg.delete()
                emb = discord.Embed(title="Join back the server",
                                    url="https://discord.gg/XdBgdZt",
                                    description="(Level 1+ are immune to this auto-mod)")
                warnMsg = (f'{msg.author.mention} You were kicked because your message contained \'nitro\''
                           + '; marked as potential spam/scam')
                await msg.author.send(warnMsg, embed=emb)
                await msg.author.kick(reason='potential nitro scam msg')
            except discord.HTTPException:
                pass


async def setup(bot):
    await bot.add_cog(AutoMod1(bot))
