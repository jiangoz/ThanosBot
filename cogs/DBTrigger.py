import discord
import asyncio
from discord.ext import commands
import sqlite3

# Multiple Listeners for Updating the Database


class DBTrigger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):

        # if msg was sent in DM (not in a guild)
        if msg.guild == None:
            return

        # Heavenly
        if msg.guild.id == 256988924390408193:
            conn = sqlite3.connect("data/heavenlyDB.db")
            c = conn.cursor()
            c.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?, ?, ?)",
                      (msg.id, msg.author.id, msg.content, msg.clean_content, msg.channel.id,
                       msg.created_at, msg.jump_url))

            conn.commit()
            conn.close()

        # Hellish
        elif msg.guild.id == 436263090472878081:
            conn = sqlite3.connect("data/hellishDB.db")
            c = conn.cursor()
            c.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?, ?, ?)",
                      (msg.id, msg.author.id, msg.content, msg.clean_content, msg.channel.id,
                       msg.created_at, msg.jump_url))

            conn.commit()
            conn.close()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Heavenly
        if member.guild.id == 256988924390408193:
            conn = sqlite3.connect("data/heavenlyDB.db")
            c = conn.cursor()
            c.execute("INSERT INTO members VALUES (?, ?, ?)",
                      (member.id, member.joined_at, member.created_at))

            conn.commit()
            conn.close()

        # Hellish
        elif member.guild.id == 436263090472878081:
            conn = sqlite3.connect("data/hellishDB.db")
            c = conn.cursor()
            c.execute("INSERT INTO members VALUES (?, ?, ?)",
                      (member.id, member.joined_at, member.created_at))

            conn.commit()
            conn.close()

    # @commands.command()
    # @commands.is_owner()
    # async def updateDB(self,ctx):


def setup(bot):
    bot.add_cog(DBTrigger(bot))
