import discord
import asyncio
from discord.ext import commands

#Designed only for Heavenly Realm
class Heavenly(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    #Auto Roles for new member joins
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 256988924390408193:
            await asyncio.sleep(300)
            role1 = member.guild.get_role(398253816971264000)  # emote role 1
            role2 = member.guild.get_role(400871836876931092)  # emote role 2
            if role1 not in member.roles:
                await member.add_roles(role1, reason="AutoRole After 5 Mins")
            if role2 not in member.roles:
                await member.add_roles(role2, reason="AutoRole After 5 Mins")
    
    @commands.command(aliases=['addMemeVoteReact'])
    @commands.is_owner()
    async def addMemeVoteReacts(self, ctx, limit=30):
        """| add vote reactions to the last <num> msgs in meme channel"""
        memeChannel = self.bot.get_channel(459767444437729280)
        messages = await memeChannel.history(limit=limit).flatten()
        up = self.bot.get_emoji(592355631667740683)
        down = self.bot.get_emoji(592355631877324820)
        upcount = 0
        downcount = 0
        for msg in messages:
            if up not in (react.emoji for react in msg.reactions):
                await msg.add_reaction(up)
                upcount += 1
            if down not in (react.emoji for react in msg.reactions):
                await msg.add_reaction(down)
                downcount += 1
        await ctx.send(f'Added {upcount} upvote reacts and {downcount} downvote reacts')

    @commands.command(aliases=['cleanWeebGif'])
    @commands.is_owner()
    async def cleanWeebGifs(self, ctx, limit=20):
        """| go thru <num> msgs in weeb channel & delete non-embedded gifs"""
        weebChannel = self.bot.get_channel(332674779213463553)
        messages = await weebChannel.history(limit=limit).flatten()
        delCount = 0
        for msg in messages:
            if "//v.redd.it/" in msg.content.lower():
                await msg.delete()
                delCount += 1
        await ctx.send(f'Deleted {delCount} non-embedded gif links')
    
def setup(bot):
    bot.add_cog(Heavenly(bot))


