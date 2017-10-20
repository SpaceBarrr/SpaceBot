import discord
from discord.ext.commands import Bot
from discord.ext import commands
import logging
#logging to console
logging.basicConfig(level=logging.INFO)

client = discord.Client()
bot_prefix= "$" #prefix before bot commands
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
	#initialisation message in console 
	print('-----------')
	print('Status: Online')
	print('Name: {}'.format(client.user.name))
	print('ID: {}'.format(client.user.id))
	print('Bot Prefix: {}'.format(bot_prefix))
	print('-----------')
	#set the bot's current playing game
	await client.change_presence(game=discord.Game(name='github.com/SpaceBarrr/SpaceBot'))

#a ping function to test the bot
@client.command(pass_context=True)
async def ping(ctx):
	await client.say("Pong!")

@client.command(pass_context=True)
async def lock(ctx):
	edit_channel(channel, **options)
	

client.run("MzcwMTM0Njc2MTg0MjM2MDM0.DMoiZw.ic9qPvPPBuspCynYaEkYyYf5xAk")