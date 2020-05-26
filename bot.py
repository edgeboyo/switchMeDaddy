import discord
import requests

from twitter import findAndReply

def downloadImg(url, name):
    ext = url.split("/")
    ext = ext[len(ext)-1].split(".")
    ext = ext[len(ext)-1]

    filename = "{}.{}".format(name, ext)

    with open("{}.{}".format(name, ext), "wb") as handle:
        resp = requests.get(url, stream=True)

        if not resp.ok:
            return False

        for block in resp.iter_content(1024):
            if not block:
                break

            handle.write(block)
    return filename

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        text = message.content
        if text[0] == '$':
            text = text[1:]
        else:
            return

        for url in findAndReply(text):
            handle = downloadImg(url, str(message.author.id))
            if not handle:
                continue

            with open(handle, "rb") as f:
                media = discord.File(f)
                await message.channel.send(content="There you go OwO", file=media)

        print('Message from {0.author}: {0.content}'.format(message))