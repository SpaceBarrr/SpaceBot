import discord
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
bot_prefix= "$"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
	print('Bot online!')
	print('Name: {}'.format(client.user.name))
	print('ID: {}'.format(client.user.id))

@client.command(pass_context=True)
async def ping(ctx):
	await client.say("Pong!")

client.run("MzcwMTM0Njc2MTg0MjM2MDM0.DMoiZw.ic9qPvPPBuspCynYaEkYyYf5xAk")