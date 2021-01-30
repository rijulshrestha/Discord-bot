import os
import discord
from discord.ext import commands

token = ""

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("DO NOT DISTURB!! Gameing in progression.."))
    print("Team Wire bot is ready...")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("The Command does not exists!!")
        print(f"{error}")

# Ping Function
@client.command()
async def ping(ctx):
    await ctx.send(f"Latency is {round(client.latency * 1000)}ms")

@ping.error
async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the premission.")

# Load and Unload an extension.
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)