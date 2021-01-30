import discord
from discord.ext import commands
import random

class Random_(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Random extention has been initialized...")
    
    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        await ctx.send(f"Question:- {question}\nAnswer:- {random.choice(responses)}")
    
    @commands.command(aliases=["game"])
    async def randomGame(self, ctx):
        game_list = ["Fortnite",
        "Valorant",
        "Cs-go",
        "Among us"]
        await ctx.send(f"You should play {random.choice(game_list)}")
    
    @commands.command(aliases=["choose"])
    async def chooseBetween(self, ctx, choice1, choice2):
        choice_  = [choice1, choice2]
        if choice1 and choice2 == "":
            await ctx.send(f"Please provide two choices!")
        else:
            await ctx.send(f"{random.choice(choice_)}")

def setup(client):
    client.add_cog(Random_(client))