"""A Markov chain generator that can tweet random messages."""

import sys
import os
import discord
import requests
import json


def get_random_stoic_quote():
    """Takes a random quote and turns it into a string."""

    source = requests.get("https://stoicquotesapi.com/v1/api/quotes/random")
    quote = json.loads(source.text)

    return f"""{quote['body']}
- {quote['author']}"""


# Connect to discord
client = discord.Client()


@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "kilo" in message.content or "Kilo" in message.content:
        await message.channel.send(get_random_stoic_quote())


client.run(os.environ['DISCORD_TOKEN'])