import discord
import asyncio
from discord.ext import commands
import random
from langdetect import detect
import emoji

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed only for Heavenly Realm


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

        # if not Heavenly, then return
        if msg.guild.id != 256988924390408193:
            return

        try:
            authorTopRole = msg.author.top_role  # member's highest role
            viprole = msg.guild.get_role(388850225881546752)
            botrole = msg.guild.get_role(272888325940051969)
            authorRoles = msg.author.roles
        except AttributeError:
            return

        # if msg from bots
        if botrole in authorRoles:
            return

        # general chat auto mod, VIP+ are immune
        if msg.channel.id == 568437502680104960 and authorTopRole < viprole:
            text: str = msg.content
            msglist = text.split()

            # Detect non-english
            if (len(msglist) >= 10 and detect(text) != "en") or \
                (not text.isascii() and not any(em in text for em in emoji.UNICODE_EMOJI) and
                 "’" not in text and "‘" not in text):
                # not ascii && no unicode emoji in text
                await msg.delete()
                emb = discord.Embed(title="Make sure your msg only contains ASCII codes",
                                          url="https://en.wikipedia.org/wiki/ASCII",
                                          description="(VIP+ are immune to this auto-mod)")
                outputMsg = (f'{msg.author.mention} Please use English to chat here. '
                             + 'You may use other langs in <#309478950772670470>')
                await msg.channel.send(outputMsg, embed=emb)
                return
            # all cap detection, ignore custom emotes
            if len(text) >= 10 and text.isupper() and "<" not in text and ">" not in text:
                await msg.channel.send(f'{msg.author.mention} ||calm down lmao||', 
                embed = discord.Embed().set_image(url="https://i.imgur.com/LoK9MJD.png"))

        # Auto moderate emote chat  #Only custom/global emotes allowed
        if msg.channel.id == 459893562130300928:
            if msgContentLower.startswith('<:') and msgContentLower.endswith('>'):
                pass
            elif msgContentLower.startswith('<a:') and msgContentLower.endswith('>'):
                pass
            else:
                await msg.delete()
                channel = self.bot.get_channel(
                    416385919919194113)  # spam channel
                await channel.send(f'{msg.author.mention} Your msg was deleted in <#459893562130300928> '
                                   + '(it is only for ***CUSTOM EMOTES***)')
                return

        # hide Nitro/gift links
        if msg.channel.id != 627651034445250560 and "discord.gift/" in msg.content:
            await msg.delete()
            private = self.bot.get_channel(
                627651034445250560)  # private channel
            await private.send("<@220997668355178496> NITRO LINK: " + msg.content)
            return

        # show off global emotes
        if ("emot" in msgContentLower or "emoj" in msgContentLower) and \
            ("how" in msgContentLower or "global" in msgContentLower or "?" in msgContentLower or
             "where" in msgContentLower or "what" in msgContentLower or "why" in msgContentLower or
             "which" in msgContentLower):

            demigodV = msg.guild.get_role(310541971179700224)  # demigod v
            role1 = msg.guild.get_role(398253816971264000)  # emote role 1
            role2 = msg.guild.get_role(400871836876931092)  # emote role 2
            if role1 not in authorRoles or role2 not in authorRoles or authorTopRole <= demigodV:
                # meme no
                await msg.channel.send(embed = discord.Embed().set_image(url="https://i.imgur.com/kxB6izB.png"))
                # list of emote IDs
                gwemotes = [407619074466643978, 389447036329656323, 402867980356288515, 402867987574685717,
                            402867992930680833, 408280788749254658, 408280780951912451, 402866531802939398,
                            402866539491229696, 389904150886088723, 408280804675026965, 398568908971573248]
                random.shuffle(gwemotes)
                for id in gwemotes:
                    emote = self.bot.get_emoji(id)
                    await msg.add_reaction(emote)
                # meme howto
                await msg.channel.send(msg.author.mention, embed = discord.Embed().set_image(
                    url="https://i.imgur.com/rRoClpC.png"))

def setup(bot):
    bot.add_cog(AutoMod1(bot))
