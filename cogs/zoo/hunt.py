import discord
from discord import Member, Embed
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import json

import random

import libraries.animalLib as aniLib
from libraries.captchaLib import *

tiers = {
    # chance of finding an animal, from 0 to 1 where 1 is 100%
    "legendary": 0.001,
    "epic": 0.01,
    "rare": 0.08,
    "uncommon": 0.25,
    "common": 1,
}

class ecobuild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="hunt",
        brief="go look for some animals, perhaps even add them to your zoo"
    )
    @cooldown(1, 300, BucketType.user)
    async def huntCommand(self, ctx):
        await aniLib.open_zoo(self, ctx)
        
        if await aniLib.check_if_zoo_not_exist(ctx.author):
            return await ctx.send("you need to create an account first")
        
        if await check_captcha(self, ctx, 0.5):
            return

        with open("storage/animals.json", "r") as f:
            animals = json.load(f)

        await aniLib.open_bot()
        
        roll = random.random()
        for tier in tiers:
            if tiers[tier] > roll:
                break
        
        ID = random.randint(1  , 6)
        selectedAnimal = animals[tier]["animals"][str(ID)]
        animal_name = selectedAnimal["name"][0]
        await ctx.send(f"You caught a {animal_name} {selectedAnimal['icon']}, it's {animals[tier]['aoran']} {tier}{animals[tier]['icon']} animal")
        
        data = await aniLib.get_animal_data()
        
        data[str(ctx.author.id)]["animals"][tier][animal_name]["caught"] += 1
        data[str(ctx.author.id)]["animals"][tier][animal_name]["count"] += 1
        
        with open("storage/playerInfo/animals.json", "w") as f:
            json.dump(data, f)#, indent=4)
        
        # for i in animals:
        #     #await ctx.send(animals(i)["name"])
        #     for y in range(1, 7):
        #         await ctx.send(animals[i]["animals"][str(y)]["icon"])
        #         await ctx.send(animals[i]["animals"][str(y)]["name"][0])
    
def setup(bot):
    bot.add_cog(ecobuild(bot))
