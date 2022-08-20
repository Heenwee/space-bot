
import discord
from discord import Member, Embed
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

from time import time

import libraries.economyLib as EL
import libraries.standardLib as SL 

class showCooldowns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="cooldown",
        aliases=["cooldowns", "cd"],
        brief="show the cooldown for a couple commands",
    )
    @cooldown(2, 5, BucketType.user)
    async def cooldown(self, ctx):
        await EL.open_account(self, ctx)
        
        userNotExist = await EL.check_if_not_exist(ctx.author)
        if userNotExist == "banned":
            return
        if userNotExist:
            return await ctx.send("i could not find your inventory, you need to create an account first")
        
        data = await EL.get_bank_data()
        
        voteCD = round(time() - data[str(ctx.author.id)]["dailyvote"]["last_vote"])
            
        
        embed = Embed(title="Cooldowns", color=ctx.author.color)
        
        # if voteCD > 43200:
        #     embed.add_field(name="Vote", value=f"✅", inline=False)
        # else:
        #     timeLeft = await self.time_conversion(abs(43200-voteCD))
        #     embed.add_field(name="Vote", value=f"{timeLeft}", inline=False)
        
        command = self.bot.get_command("scavenge")
        command_cooldown = await self.get_cooldown(command, ctx)
        desc = f"{await self.time_conversion(command_cooldown)}"
        if command_cooldown > 0: desc = f" <t:{command_cooldown+round(time())}:R>"
        embed.add_field(name="Scavenge", value=desc, inline=False)
        
        command = self.bot.get_command("hunt")
        command_cooldown = await self.get_cooldown(command, ctx)
        desc = f"{await self.time_conversion(command_cooldown)}"
        if command_cooldown > 0: desc = f" <t:{command_cooldown+round(time())}:R>"
        embed.add_field(name="Hunt", value=desc, inline=False)
        
        command = self.bot.get_command("eat")
        command_cooldown = await self.get_cooldown(command, ctx)
        desc = f"{await self.time_conversion(command_cooldown)}"
        if command_cooldown > 0: desc = f" <t:{command_cooldown+round(time())}:R>"
        embed.add_field(name="Eat", value=desc, inline=False)
        

        await ctx.send(embed=embed)
    
    async def get_cooldown(self, command, ctx):
        return round(command.get_cooldown_retry_after(ctx))
    
    async def time_conversion(self, sec):
        sec_value = sec % (24 * 3600)
        hour_value = sec_value // 3600
        sec_value %= 3600
        min_value = sec_value // 60
        sec_value %= 60
        returnStr = ""
        if hour_value >= 1:
            returnStr += f"{hour_value}H "
        if min_value >= 1:
            returnStr += f"{min_value}M "
        if sec_value >= 1:
            returnStr += f"{sec_value}S"
        
        if returnStr == "":
            returnStr = "✅"

        return returnStr

async def setup(bot):
    await bot.add_cog(showCooldowns(bot))
