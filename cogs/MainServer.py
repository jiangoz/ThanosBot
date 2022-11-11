from datetime import datetime, timezone

import discord
import emoji
from discord.ext import commands

# Designed only for main server


class MainServer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # #Auto Roles for new member joins
    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     if member.guild.id == 256988924390408193:
    #         await asyncio.sleep(310)
    #         role1 = member.guild.get_role(398253816971264000)  # emote role 1
    #         role2 = member.guild.get_role(400871836876931092)  # emote role 2
    #         try:
    #             if role1 not in member.roles:
    #                 await member.add_roles(role1, reason="AutoRole After 5 Mins")
    #             if role2 not in member.roles:
    #                 await member.add_roles(role2, reason="AutoRole After 5 Mins")
    #         except discord.HTTPException:
    #             pass

    # Auto kicks new accs without pfp (prevent bot raids)
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if (member.guild.id == 256988924390408193
                and member.avatar_url == member.default_avatar_url):

            demigod1 = member.guild.get_role(257006648583913472)  # demigod 1

            delta = datetime.now() - member.created_at
            # new acc created less than 7 days ago
            if delta.days < 7 and demigod1 not in member.roles:
                try:
                    emb = discord.Embed(title="Join back the server",
                                        url="https://discord.gg/XdBgdZt",
                                        description="(Level 1+ are immune to this auto-mod)")
                    warnMsg = (f'{member.mention} You were kicked because your account is new and '
                               + 'you have no profile picture; marked as potential bot/raid')
                    await member.send(warnMsg, embed=emb)
                    await member.kick(reason='potential new acc bot/raid')
                except discord.HTTPException:
                    pass

    @commands.command(aliases=['kickPotentialBot'])
    @commands.is_owner()
    async def kickPotentialBots(self, ctx, limit=100):
        """| kicks new accs without pfp (potential bots)"""
        await ctx.send(f'Attempting to kick {limit} potential bots...')
        kickCount = 0
        for member in ctx.guild.members:
            if (kickCount < limit
                    and member.avatar_url == member.default_avatar_url):

                try:
                    demigod1 = member.guild.get_role(
                        257006648583913472)  # demigod 1

                    delta = datetime.now() - member.created_at
                    # new acc created less than 7 days ago
                    if delta.days < 7 and demigod1 not in member.roles:
                        emb = discord.Embed(title="Join back the server",
                                            url="https://discord.gg/XdBgdZt",
                                            description="(Level 1+ are immune to this auto-mod)")
                        warnMsg = (f'{member.mention} You were kicked because your account is new and '
                                   + 'you have no profile picture; marked as potential bot/raid')
                        await member.send(warnMsg, embed=emb)
                        await member.kick(reason='potential new acc bot/raid')
                        kickCount += 1
                except discord.HTTPException:
                    pass

        await ctx.send(f'Finished. Kicked {kickCount} potential bots')

    @commands.command(aliases=['addMemeVote'])
    @commands.is_owner()
    async def addMemeVotes(self, ctx, limit=30):
        """| add vote reactions to the last <num> msgs in memes channel"""
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

    @commands.command(aliases=['addSuggestVote', 'addSuggestionVote', 'addSuggestionVotes'])
    @commands.is_owner()
    async def addSuggestVotes(self, ctx, limit=10):
        """| add vote reactions to the last <num> msgs in suggestions channel"""
        suggestChannel = self.bot.get_channel(838570502091833345)
        messages = await suggestChannel.history(limit=limit).flatten()
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
            if "v.redd.it" in msg.content.lower():
                try:
                    await msg.delete()
                    delCount += 1
                except discord.HTTPException:
                    pass
        await ctx.send(f'Deleted {delCount} non-embedded gif links')

    @commands.command(aliases=['cleanEmote', 'cleanEmotes'])
    @commands.is_owner()
    async def cleanEmoteChat(self, ctx, limit=100):
        """| go thru <num> msgs in emote channel & delete non-emotes"""
        emoteChannel = self.bot.get_channel(459893562130300928)
        messages = await emoteChannel.history(limit=limit).flatten()
        delCount = 0
        for msg in messages:
            if msg.content.startswith('<:') and msg.content.endswith('>'):
                pass
            elif msg.content.startswith('<a:') and msg.content.endswith('>'):
                pass
            elif all(em in emoji.UNICODE_EMOJI_ENGLISH for em in msg.content):
                pass
            else:
                try:
                    await msg.delete()
                    delCount += 1
                except discord.HTTPException:
                    pass
        await ctx.send(f'Deleted {delCount} non-emote messages')


async def setup(bot):
    await bot.add_cog(MainServer(bot))
