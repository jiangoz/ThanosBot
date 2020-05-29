import discord
import asyncio
from discord.ext import commands
import random

# NO COMMANDS HERE, only 1 listener for on_message()
# Designed only for Heavenly Realm
class MsgListener(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        msgContent = msg.content.lower()
        trigger = msgContent.split()

        #if msg from self(bot)
        if msg.author.id == 436643551993004033:
            return

        #if msg was sent in DM (not in a guild)
        if msg.guild == None:
            react = self.bot.get_emoji(579882318664302592) #thanos ugh emote
            await msg.add_reaction(react)
            channel = self.bot.get_channel(550456326053036034) #msg log channel
            await channel.send(f'{msg.author.mention} said in DM: {msgContent}')
            return

        #if not Heavenly, then return
        if msg.guild.id != 256988924390408193:
            return

        # Emote reaction triggers
        if "f" in trigger:
            femote = self.bot.get_emoji(471008964021059586)
            await msg.add_reaction(femote)
        if msgContent == "no u":
            await msg.channel.send("<:ThanosNOU:571052438619029524>")
        if "owo" in trigger: #owo combo emotes!
            o1 = self.bot.get_emoji(490916040964964354)
            w2 = self.bot.get_emoji(490916041166159872)
            o3 = self.bot.get_emoji(490921532734963722)
            await msg.add_reaction(o1)
            await asyncio.sleep(0.1)
            await msg.add_reaction(w2)
            await asyncio.sleep(0.1)
            await msg.add_reaction(o3)
        if "220997668355178496" in msgContent:   #ping jiango
            emote = self.bot.get_emoji(560468390154731530)
            await msg.add_reaction(emote)
        if "gay" in msgContent:
            emote = self.bot.get_emoji(480073530466107392)
            await msg.add_reaction(emote)
        if "jojo" in msgContent or "jjba" in trigger:
            emote1 = self.bot.get_emoji(540669998725857290)
            emote2 = self.bot.get_emoji(540669998834909194)
            emote3 = self.bot.get_emoji(540669998809481276)
            await msg.add_reaction(emote1)
            await msg.add_reaction(emote2)
            await msg.add_reaction(emote3)

        #Auto moderate emote chat  #Only custom/global emotes allowed
        if msg.channel.id == 459893562130300928:
            if msgContent.startswith('<:') and msgContent.endswith('>'):
                pass
            elif msgContent.startswith('<a:') and msgContent.endswith('>'):
                pass
            else:
                await msg.delete()
                channel = self.bot.get_channel(416385919919194113) #spam channel
                await channel.send(f'{msg.author.mention} Your msg was deleted in <#459893562130300928> '
                                    +'(it is only for ***CUSTOM EMOTES***)')
        
        #Racial slur filter
        if ("nigger" in msgContent or "chink" in msgContent or "kike" in trigger or "spic" in trigger 
            or "gook" in trigger or "honkey" in trigger):

            muted = msg.guild.get_role(316401466875314178)
            botrole = msg.guild.get_role(272888325940051969)
            modrole = msg.guild.get_role(388736972845482004)

            if botrole in msg.author.roles:
                pass
            elif modrole in msg.author.roles:
                await msg.delete()
            else:
                await msg.delete()
                await msg.author.add_roles(muted,reason='racial slur')
                await msg.channel.send(f'{msg.author.mention} has been {muted.mention} (for 69 mins) '
                                        +'<a:aComicSans:528411471990751235>')
                await msg.channel.send("**SO GUYS WE DID IT WE ENDED RACISM**")
                modlog = self.bot.get_channel(316332561448042496) 
                logmsg = await modlog.send(msg.author.mention + " was temporarily muted for racial slur")
                await asyncio.sleep(4140)
                await msg.author.remove_roles(muted,reason='timed mute is over')
                await logmsg.edit(content=f'{msg.author.mention} was ~~temporarily muted for racial slur~~ unmuted')

        #Auto add vote reactions in meme channel
        if msg.channel.id == 459767444437729280:
            up = self.bot.get_emoji(592355631667740683)
            down = self.bot.get_emoji(592355631877324820)
            await msg.add_reaction(up)
            await msg.add_reaction(down)
        
        #Auto delete non-embedded gifs in weeb channel
        if msg.channel.id == 332674779213463553 and "//v.redd.it/" in msgContent:
            await msg.delete()
        
        # hide Nitro/gift links
        if msg.channel.id != 627651034445250560 and "discord.gift/" in msgContent:
            await msg.delete()
            private = self.bot.get_channel(627651034445250560) #private channel
            await private.send("<@220997668355178496> NITRO LINK: " + msg.content)

        #howdy greeting - only for lurkers/newfags
        if (msgContent.startswith("hi") or msgContent.startswith("hey") or msgContent.startswith("hello") 
        or msgContent.startswith("hai") or msgContent.startswith("howdy") or msgContent.startswith("sup")):
            
            demigod = msg.guild.get_role(257006648583913472) #demigod i
            botrole = msg.guild.get_role(272888325940051969)
            if demigod not in msg.author.roles and botrole not in msg.author.roles:
                await msg.channel.send(f'{msg.author.mention} Howdy! <:TipHat:585587679798886411>')
                await msg.channel.send("<:GWjiangoPepeFedora:389447036329656323> <a:0PepeHowdy:594175419801141273>")
        
        #unflip the damn table!
        if "(╯°□°）╯︵ ┻━┻" in msgContent:
            await msg.channel.send("┬─┬ ノ( ゜-゜ノ)")
        
        #show off global emotes
        if ("emot" in msgContent or "emoj" in msgContent) and \
            ("how" in msgContent or "global" in msgContent or "?" in msgContent or "where" in msgContent or 
            "what" in msgContent or "why" in msgContent or "which" in msgContent):
            await msg.channel.send("https://i.imgur.com/kxB6izB.png") #emotes screenshot
            #list of emote IDs
            gwemotes = [407619074466643978,389447036329656323,402867980356288515,402867987574685717,402867992930680833,
                        408280788749254658,408280780951912451,402866531802939398,402866539491229696,389904150886088723,
                        408280804675026965,398568908971573248]
            random.shuffle(gwemotes)
            for id in gwemotes:
                emote = self.bot.get_emoji(id)
                await msg.add_reaction(emote)
                

def setup(bot):
    bot.add_cog(MsgListener(bot))