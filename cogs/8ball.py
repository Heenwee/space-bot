from urllib import response
import discord
from discord import Member, Embed
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

import random
import time

responses = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    'Don\'t count on it.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.',
    'No way.',
    'Maybe',
    'The answer is hiding inside you',
    'No.',
    '||No||',
    '||Yes||',
    'Hang on, what?',
    'It\'s just the beginning',
    'Good Luck',
]

class ball8(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball", aliases=["8"], brief="Ask the 8ball a question")
    async def ball8_command(self, ctx):
        msg = await ctx.send("connecting to the oracle...")
        time.sleep(random.randrange(1.3, 2.5))
        await msg.edit(content="considering...")
        time.sleep(random.randrange(0.8, 2))
        await msg.edit(content=random.choice(responses))


def setup(bot):
    bot.add_cog(ball8(bot))
