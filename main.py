import discord
import os
import logging
from discord.ext import commands
from config import settings
bot = commands.Bot(command_prefix='+')
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    bot.run('token')

    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    client = MyClient()
    client.run('')
     token = os.environ.get('BOT_TOKEN')
        bot.run(str(token))
        @bot event
async def on_ready():
    print("bot online")
