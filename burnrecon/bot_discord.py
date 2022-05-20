import tempfile
from pathlib import Path

import discord

from burnrecon.base import list_subdomains, subdomain_enum
from burnrecon.config import settings

TOKEN = settings.DISCORD_TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if "+enum" in msg:
        await message.channel.send("Enumerating subdomains...")
        cmd, target, domain = msg.split()

        subdomain_enum(target, domain)
        await message.channel.send(f"subdomains of {target} added to DB")
        await message.channel.send(
            f"To see all subdomains from {target}, run `+list-subs {target}`"
        )
    elif "+list-subs" in msg:
        await message.channel.send("Listing subdomains...")
        cmd, target = msg.split()
        file_ = f"{Path(tempfile.NamedTemporaryFile(delete=False).name)}.txt"
        subs = open(file_, "w")
        subdomains = list_subdomains(target)
        for sub in subdomains:
            subs.write(sub["subdomain"] + "\n")
        subs.close()
        await message.channel.send(f"Subdomains of {target}:- 🍺\n")
        await message.channel.send(file=discord.File(file_))
    elif "+help" in msg:
        await message.channel.send("Commands: `+enum, +list_subs`")
    else:
        await message.channel.send(
            "Wrong command, please sendme `+help` to see all commands"
        )


client.run(TOKEN)
