import discord
from discord.ext import commands

class Spam(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Spam extention has been initialized...")

    @commands.command()
    async def spam(self, ctx, name, num = 7):
        if num > 69:
            await ctx.send("Please have mercy!!")
        else:
            for i in range(int(num)):
                await ctx.send(f"{name}")

    # Clear Function.
    @commands.command()
    async def clear(self, ctx, num : int):
        await ctx.channel.purge(limit = (num + 1))
    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify an amount of message to delete.")

def setup(client):
    client.add_cog(Spam(client))