import discord
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()


class Util(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """| pong! returns latency"""
        await ctx.send(f'Pong! {round(self.bot.latency*1000)}ms')

    @commands.command()
    @commands.is_owner()
    async def purgeMsg(self, ctx, amount: int):
        """| purge <amount> most recent msgs in channel"""
        messages = await ctx.channel.history(limit=amount).flatten()
        c = 0
        for m in messages:
            await m.delete()
            c += 1
        await ctx.send(f'Finished deleting {c} messages!')

    @commands.command()
    @commands.is_owner()
    async def purgeTargetMsg(self, ctx, target: str):
        """| purge all msgs in channel that contain <target> str"""
        await ctx.send('Fetching all messages in channel...')
        messages = await ctx.channel.history(limit=None).flatten()
        await ctx.send('Fetched the messages. Starting the deletion phase...')
        c = 0
        for m in messages:
            if target.lower() in m.content.lower():
                await m.delete()
                c += 1
        await ctx.send(f'Finished deleting {c} messages!')

    @commands.command()
    async def info(self, ctx):
        """| see information about the bot"""
        infoembed = discord.Embed(color=discord.Color.purple()
                                  ).set_author(name="Thanos", icon_url="https://i.imgur.com/LPX0BfY.png")
        
        GITHUB = os.getenv('GITHUB')
        appInfo = await self.bot.application_info()
        CREATOR = f'{appInfo.owner.name}#{appInfo.owner.discriminator}'

        infoembed = infoembed.add_field(name="API", value="d.py"
                            ).add_field(name="Language", value="Python3"
                            ).add_field(name="Creator", value=CREATOR
                            ).add_field(name="Version", value=os.getenv('VERSION')
                            ).add_field(name="GitHub", value=f'[ThanosBot]({GITHUB})'
                            ).add_field(name="Users", value=str(len(self.bot.users)))

        await ctx.send(embed=infoembed)

    @commands.command(aliases=['noAttention', 'removeNicks'])
    @commands.has_guild_permissions(manage_guild=True)
    async def removeNick(self, ctx, usercount: int = 10, symbol: str = '!', *, newNick: str = None):
        """| remove/change nicknames that start with \"symbol\""""
        if ctx.guild == None:
            await ctx.send(f'Hey! You need to type that command in a server!')
        else:
            badnamelist = []
            for member in ctx.guild.members:
                if member.bot:
                    continue
                if member.display_name.startswith(symbol):
                    badnamelist.append(member)

            # number of bad names found in total
            badnamecount = len(badnamelist)
            await ctx.send(f'Attempting to change {usercount} names that start with `{symbol}` to `{newNick}` ...')

            changecount = 0
            if badnamecount <= usercount:
                for member in badnamelist:
                    await member.edit(nick=newNick)
                    changecount += 1
                await ctx.send(
                    f'Only {badnamecount} bad nicknames found. {changecount} members changed to `{newNick}`')
            else:  # since there are too many bad names, only change the specified amount
                for member in badnamelist:
                    if changecount < usercount:
                        await member.edit(nick=newNick)
                        changecount += 1
                await ctx.send(
                    f'{badnamecount} bad nicknames found. {changecount} members changed to `{newNick}`')


def setup(bot):
    bot.add_cog(Util(bot))
