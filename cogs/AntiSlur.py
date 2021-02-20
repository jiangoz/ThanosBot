import discord
import asyncio
from discord.ext import commands
from pathlib import Path

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed only for Heavenly Realm


class AntiSlur(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        # fetch file path
        fPath = Path(__file__).parents[1].joinpath(
            "data", "slursFilter.txt")
        wPath = Path(__file__).parents[1].joinpath(
            "data", "wildcardFilter.txt")

        with open(fPath) as f:
            self.slursList = f.readlines()
        
        with open(wPath) as w:
            self.wildcardList = w.readlines()

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
            authorRoles = msg.author.roles
        except AttributeError:
            return

        # if msg from bots
        if botrole in authorRoles:
            return

        # Racial slur filter
        # standalone word match (not wildcard match)
        for s in self.slursList:
    
            if s in trigger:
                muted = msg.guild.get_role(316401466875314178)
                modrole = msg.guild.get_role(388736972845482004)

                try:
                    if modrole in authorRoles:
                        await msg.delete()
                        return
                    else:
                        await msg.delete()
                        await msg.author.add_roles(muted, reason='racial slur')
                        await msg.channel.send(f'{msg.author.mention} has been {muted.mention} (for 69 mins) '
                                               + '<a:aComicSans:528411471990751235>')
                        await msg.channel.send("**SO GUYS WE DID IT WE ENDED RACISM**")
                        modlog = self.bot.get_channel(316332561448042496)
                        logmsg = await modlog.send(msg.author.mention + " was temporarily muted for racial slur")
                        await asyncio.sleep(4140)
                        await msg.author.remove_roles(muted, reason='timed mute is over')
                        await logmsg.edit(content=f'{msg.author.mention} was ~~temporarily muted for racial slur~~ unmuted')
                        return
                except discord.HTTPException:
                    pass
        
        # wildcard match
        for w in self.wildcardList:
            if w in msgContentLower:
                try:
                    await msg.delete()
                    return
                except discord.HTTPException:
                    pass


def setup(bot):
    bot.add_cog(AntiSlur(bot))
