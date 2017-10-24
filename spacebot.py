import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import logging
#logging to console
logging.basicConfig(level=logging.ERROR)

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
	print("Ping function ran")

#takes the random number and "rates" someone out of 10
@client.command(pass_context=True)
async def ratewaifu(ctx, arg):
	global x
	x = random.randint(1, 10)
	if 

	print('Rate waifu args: {0}, Random number: {1}'.format(arg, x))
	await client.say(':thinking: Hmm, Id say {0} is a {1}'.format(arg, x))


	# if josephine in arg
	# 	await client.say(':thinking: Hmm, Id say Josephine is a 10!')
	# elif cian in arg
	# 	await client.say(':thinking: Hmm, Id say Cian is a 10!')
	# else

client.run("MzcwMTM0Njc2MTg0MjM2MDM0.DMoiZw.ic9qPvPPBuspCynYaEkYyYf5xAk")