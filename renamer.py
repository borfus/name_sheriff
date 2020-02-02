import asyncio
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '_')

@client.event
async def on_ready():
    print('Ready to protect the people of this town.')

@client.command()
async def rename(ctx, renamee: discord.Member, *, new_name):
    author = ctx.message.author
    print('{} renaming {} to {}.'.format(author, renamee, new_name))
    await renamee.edit(nick=new_name)

def read_token():
    with open("token", "r") as token_file:
        lines = token_file.readlines()
        return lines[0].strip()

try:
    client.run(read_token())
except Exception:
    print("That token doesn't work!!!!")
