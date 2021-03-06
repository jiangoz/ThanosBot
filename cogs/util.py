import discord
import asyncio
from discord.ext import commands


class Util(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """| pong! returns latency"""
        await ctx.send(f'Pong! {round(self.bot.latency*1000)}ms')
    
    @commands.command()
    async def info(self, ctx):
        """| see information about the bot"""
        infoembed = discord.Embed(color=discord.Color.purple()).set_author(name="Thanos", 
        icon_url="https://i.imgur.com/LPX0BfY.png")
        infoembed = infoembed.add_field(name="API", value="d.py").add_field(name="Language", value="Python3"
        ).add_field(name="Creator", value="jiango#0215").add_field(name="Version", value="420.69").add_field(
            name="GitHub", value="[ThanosBot](https://github.com/jiangoz/ThanosBot)").add_field(name="Users", 
            value=str(len(self.bot.users)))

        infoembed = infoembed.add_field(name="Heavenly", value="[discord.gg/LMAO](https://discord.gg/XdBgdZt)"
        ).add_field(name="Hellish", value="[discord.gg/MbnDzAR](https://discord.gg/MbnDzAR)")

        await ctx.send(embed=infoembed)

    @commands.command(aliases=['noAttention', 'removeNicks'])
    @commands.has_guild_permissions(manage_guild=True)
    async def removeNick(self, ctx, usercount:int=10, symbol:str='!', *, newNick:str=None):
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
