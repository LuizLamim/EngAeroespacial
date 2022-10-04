import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    if message.content == '!teste':
        await message.author.send('Mensagem teste!')

client = MyClient()
client.run('MTAyNTQ4OTQxNzY1MTEwNTgwMw.GZlQ4J.iY5ckLTVszqe1SweWAxY74Im7-5KgSivG5oKUc')