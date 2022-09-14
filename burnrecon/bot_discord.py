import tempfile
from pathlib import Path

import discord
from base import (
    getalive,
    list_subdomains,
    list_urls_from_target,
    naabu_scan,
    subdomain_enum,
)
from config import settings

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
    # TODO: check if send necessary params
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
        subdomains_result = (
            f"{Path(tempfile.NamedTemporaryFile(delete=False).name)}.txt"
        )
        subs = open(subdomains_result, "w")
        subdomains = list_subdomains(target)
        for sub in subdomains:
            subs.write(sub["subdomain"] + "\n")
        subs.close()
        await message.channel.send(f"Subdomains of {target}:- 🍺\n")
        await message.channel.send(file=discord.File(subdomains_result))
    elif "+alive-hosts" in msg:
        await message.channel.send("Check if subdomain is alive...")
        cmd, target = msg.split()
        naabu_scan(target)
        getalive(target)

        await message.channel.send(f"Urls of {target} added to DB")
        await message.channel.send(
            f"To see all urls from {target}, run `+list-urls {target}`"
        )
    elif "+list-urls" in msg:
        await message.channel.send("Listing urls...")
        cmd, target = msg.split()

        urls_result = (
            f"{Path(tempfile.NamedTemporaryFile(delete=False).name)}.txt"
        )
        urls_list = open(urls_result, "w")
        urls = list_urls_from_target(target)
        for url in urls:
            urls_list.write(url["url"] + "\n")
        urls_list.close()

        await message.channel.send(f"Urls of {target}:- 🍺\n")
        await message.channel.send(file=discord.File(urls_result))
    elif "+help" in msg:
        await message.channel.send(
            "Commands: `+enum, +list-subs, +alive-hosts, +list-urls`"
        )
    else:
        await message.channel.send(
            "Wrong command, please sendme `+help` to see all commands"
        )


client.run(TOKEN)
