import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import logging
import os
from time import localtime, strftime

#logging to console
logging.basicConfig(level=logging.ERROR)

#defines client as the bot
client = discord.Client()
bot_prefix= "$" #prefix before bot commands
client = commands.Bot(command_prefix=bot_prefix)

#called when the bot is originally loaded
@client.event
async def on_ready():
	#initialisation message in console 
	os.system('cls' if os.name == 'nt' else 'clear')
	print('-----------')
	print(strftime("%a, %d %b %Y %X", localtime()))
	print('Status: Online')
	print('Name: {}'.format(client.user.name))
	print('ID: {}'.format(client.user.id))
	print('Command Prefix: {}'.format(bot_prefix))
	print('View the library docs at discordpy.readthedocs.io/en/rewrite/api.html')
	print('View the source code at github.com/SpaceBarrr/SpaceBot')
	print('-----------')
	#initialisation message in chat
	startUp = discord.Embed(title='SpaceBot now online!', description='Command prefix: $', colour=0x57FE01)
	await client.send_message(client.get_channel("366216076012290049"), embed=startUp)
	#set the bot's current playing game
	await client.change_presence(game=discord.Game(name='github.com/SpaceBarrr/SpaceBot'))

#a ping function to test the bot
@client.command(pass_context=True)
async def ping(ctx):
	await client.say('Pong!')
	print('{}: @{} ran ping func'.format(strftime("%a, %d %b %Y %X", localtime()), ctx.message.author))

#takes the random number and "rates" someone out of 10 (with some exceptions)
@client.command(pass_context=True)
async def rnjesus(ctx, arg):
	global x
	x = random.randint(1, 100)
	print('{}: @{} ram RNG func'.format(strftime("%a, %d %b %Y %X", localtime()), ctx.message.author))
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
		await client.say(":thinking: Hmm, I'd say {} is a {}/100".format(reply, x))

#gives the mentioned user POW rank and strips their ranks if the command user has admin
@client.command(pass_context=True)
async def demote(ctx):
	general = discord.utils.get(ctx.message.server.roles,name='General Secretary of USSR')
	marshal = discord.utils.get(ctx.message.server.roles,name='Marshal of the USSR')
	chief = discord.utils.get(ctx.message.server.roles,name='Chief Marshal')
	general = discord.utils.get(ctx.message.server.roles,name='General of the Army')
	cosmonaut = discord.utils.get(ctx.message.server.roles,name='Russian Cosmonaut')
	soldier = discord.utils.get(ctx.message.server.roles,name='USSR Soldier')
	citizen = discord.utils.get(ctx.message.server.roles,name='USSR Citizen')
	POW = discord.utils.get(ctx.message.server.roles,name='Prisoner of War')
	
	if discord.utils.get(ctx.message.server.roles,name='General Secretary of USSR') in ctx.message.author.roles:
		await client.remove_roles(ctx.message.mentions[0], marshal, chief, general, cosmonaut, soldier, citizen)
		await client.add_roles(ctx.message.mentions[0], POW)
		await client.say("Demoted @{}".format(ctx.message.mentions[0]))
		print('{}: @{} ran demote func'.format(strftime("%a, %d %b %Y %X", localtime()), ctx.message.author))
	
	else:
		await client.say("You do not have permission to use this command you fucking pleb")
		print('{}: @{} attempted to run demote func'.format(strftime("%a, %d %b %Y %X", localtime()), ctx.message.author))

#pretty much a magic 8 ball func
@client.command(pass_context=True)
async def should(ctx):
	global x
	x = random.randint(1, 10)
	print('{}: @{} ran should func'.format(strftime("%a, %d %b %Y %X", localtime()), ctx.message.author))
	if x == 1:
		await client.say('Yes')
	elif x == 2:
		await client.say('The future is cloudy...')
	elif x == 3:
		await client.say('Without a doubt')
	elif x == 4:
		await client.say('FUCKING HELL YES')
	elif x == 5:
		await client.say('NO WAY JOSÉ')
	elif x == 6:
		await client.say('idk man??')
	elif x == 7:
		await client.say(':thinking: Perhaps...')
	elif x == 8:
		await client.say('nah knt')
	elif x == 9:
		await client.say('yup')
	else:
		await client.say('No')

#'locks' the channel the user is in by setting a limit of 1, so no one without admin can join
@client.command(pass_context=True)
async def lock(ctx):
	if channel is not None:
		await client.edit_channel(channel=255264570141179905, user_limit=1)
		print('{}: @{} ran lock func'.format(strftime("%a, %d %b %Y %X", localtime()), ctx.message.author))
		await client.say(":lock: | Channel locked...")
	else:
		await client.say('Error: You are not in a voice channel')
		print('{}: @{} attempted to run lock func'.format(strftime("%a, %d %b %Y %X", localtime()), ctx.message.author))

#bot token (pleae dont steal this :( )
client.run("MzcwMTM0Njc2MTg0MjM2MDM0.DMoiZw.ic9qPvPPBuspCynYaEkYyYf5xAk")

#www.spacebarrr.github.io
#Licensed under Anyone But Nicholas Franz 2017 (ABNF)