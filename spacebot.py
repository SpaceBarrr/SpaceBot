import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import logging
import os

#logging to console
logging.basicConfig(level=logging.ERROR)

#defines client as the bot (?)
client = discord.Client()
bot_prefix= "$" #prefix before bot commands
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
	#initialisation message in console 
	os.system('cls' if os.name == 'nt' else 'clear')
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
async def rnjesus(ctx, arg):
	global x
	x = random.randint(1, 100)
	
	#makes the input lowercase for processing so all capitalisations are treated with equal rights
	arg = arg.lower()

	#exception for josephine
	if 'josephine' in arg:
		await client.say(":thinking: Hmm, I'd say Josephine is a 10/10")
	
	#exception for cian
	elif 'cian' in arg:
		await client.say(":thinking: Hmm, I'd say Cian is the best motherfucker out...")

	else: 
		#makes the input capitalised again for output
		reply = arg.capitalize()
		await client.say(":thinking: Hmm, I'd say {0} is a {1}/100".format(reply, x))

#gives out prisoner of war
@client.command(pass_context=True)
async def pow(ctx):
    giveRole = discord.utils.get(ctx.message.server.roles,name='Prisoner of War')
    await client.add_roles(ctx.message.mentions[0], giveRole)
    await client.say("Given {} Prisoner of War!".format(ctx.message.mentions[0]))

#'locks' the channel the user is in by setting a limit of 1, so no one new can join
@client.command(pass_context=True)
async def lock():
	# channel = discord.utils.get(guild.voice_channels, name='Gulag')
	channel = discord.Object(id='255253018314932228')
	await client.edit_channel(channel, user_limit=1)
	await client.say(":lock: | Channel locked...")

#bot token
client.run("MzcwMTM0Njc2MTg0MjM2MDM0.DMoiZw.ic9qPvPPBuspCynYaEkYyYf5xAk")

# www.spacebarrr.github.io
# Licensed under ABNF