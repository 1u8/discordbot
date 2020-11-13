import discord
import random
import logging
import logging
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='.')

#Starting up bot

@client.event
async def on_ready():
    print('logged in!')
    print('<--------[Username]------>')
    print(client.user.name)
    print('<--------[Bot ID]-------->')
    print(client.user.id)
    print('[+]---------------------[+]')
    print('<-Current status->')
    print(client.user.id)
    print('Current bot is online!')
    activity = discord.Game(name="@SkidTheNoob / .helpme")
    await client.change_presence(status=discord.Status.idle, activity=activity)

newUserDMMessage = "Welcome to **Federal Agent** discord.py bot!"

#missing requirements (such as someone not including a full command)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Uh oh, seems like that command isnt including all reqirements :(')

#Welcome Message

@client.event
async def on_member_join(member):

    await member.send("Welcome to the server, please get some roles and enjoy your time :)")

#Help Menu, this can be customized to your commands.

@client.command()
async def helpme(ctx):
    embed: discord.Embed = discord.Embed(
        title="Help Menu", description="Lists the current commands.", color=discord.Color.dark_green()
    )
    embed.set_author(name="Help!")
    embed.add_field(name=".helpme", value="Shows a list of commands", inline=True)

    await ctx.send(embed=embed)
    
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member!")
        return
    await member.kick()
    await ctx.send(f"{member.mention} was kicked!")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to kick people")
 
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member!")
        return
    await member.ban()
    await ctx.send(f"{member.mention} got banned! ")
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people ;(")
 
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member!")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people noob!")
 
 
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member!")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people!")        

client.run('TOKEN')
