import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('MTAyNTQ4OTQxNzY1MTEwNTgwMw.Gl1u7R.o4LJcD9CNyIunJkMCGt3NrGw_etoVWJ7C0B7jg')