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
	print("Ping function ran succesfully")

#takes the random number and "rates" someone out of 10 (with some exceptions)
@client.command(pass_context=True)
async def ratewaifu(ctx, arg):
	global x
	x = random.randint(1, 10)
	
	#makes the input lowercase for processing so all capitalisations are treated equal
	arg = arg.lower()

	#exception for josephine
	if 'josephine' in arg:
		await client.say(":thinking: Hmm, I'd say Josephine is a 10!")
	
	#exception for cian
	elif 'cian' in arg:
		await client.say(":thinking: Hmm, I'd say Cian is the best motherfucker out!")

	else: 
		#makes the input capitalised again for output
		reply = arg.capitalize()
		await client.say(":thinking: Hmm, I'd say {0} is a {1}".format(reply, x))

client.run("MzcwMTM0Njc2MTg0MjM2MDM0.DMoiZw.ic9qPvPPBuspCynYaEkYyYf5xAk")