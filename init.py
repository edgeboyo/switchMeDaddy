import tweepy

from bot import DiscordClient

import discord
from discord.ext import commands

from twitter import clearcomment

def init():
    with open("discord.token", "r") as f:
        dtoken = clearcomment(f.readline())


    client = DiscordClient()
    client.run(dtoken)



if __name__ == "__main__":
    init()

