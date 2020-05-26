import tweepy
import discord
from twitter import clearcomment

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

with open("discord.token", "r") as f:
	dtoken = clearcomment(f.readline())


client = MyClient()
client.run(dtoken)