import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! **{round(client.latency * 1000)}ms**')

@client.command()
async def hello(ctx):
    await ctx.send("Hey there! How is it going?")

@client.command()
async def Hello(ctx):
    await ctx.send("Hey there! How is it going?")

@client.command()
async def hi(ctx):
    await ctx.send("Hey there! How is it going?")

@client.command()
async def Hi(ctx):
    await ctx.send("Hey there! How is it going?")

@client.command()
async def bye(ctx):
    await ctx.send("See you soon!")
    
@client.command()
@commands.has_role('Moderator')
async def ban(ctx, member:discord.user=None, reason=None):
    moderator == ctx.message.author
    if member==ctx.message.author:
        await ctx.channel.send("You cannot ban yourself!")
        return
    if member==none:
        await ctx.channel.send("You need to enter an user id, it cannot be empty.")
        return
    if reason==none:
        reason="The ban hammer has spoken."
    banmessage = f"You have been banned from {ctx.guild.name} for: {reason}!"
    await ctx.send(banmessage)
    punishmentlog= 727552384926220318
    channel = client.get_channel(punishmentlog)
    await channel.send(f"NEW LOG! {member} has been banned by {moderator} for {reason}.")
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
  

client.run("NzczMTAzMDUxMjc5OTU4MDE2.X6EWUg.tcDfntuGAFTHl_ORxSiWNYwgtDc")