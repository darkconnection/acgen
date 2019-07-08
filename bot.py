#!/usr/bin/env python3
# encoding: utf-8

import asyncio
import json

import asyncpg
import discord
from discord.ext import commands

with open('config.json') as f:
	config = json.load(f)
del f

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config['prefix']))
db_ready = asyncio.Event()

@bot.event
async def on_ready():
	global db

	# change .connect to .create_pool if you use a DB host that allows more than one connection
	db = await asyncpg.connect(**config.pop('db'))
	db_ready.set()

	print('Ready.')

	
	
@bot.command()
async def spotify(context):
	await db_ready.wait()
	data = await db.fetchrow('SELECT * FROM <row> LIMIT 1')
	await db.execute('DELETE FROM <row> WHERE id = $1', data['id'])
	await context.author.send(data['alt'])
	

@bot.command()
async def hulu(context):
	await db_ready.wait()
	data = await db.fetchrow('SELECT * FROM priv33 LIMIT 1')
	await db.execute('DELETE FROM <row> WHERE id = $1', data['id'])
	await context.author.send(data['alt'])

	
@bot.command()
async def crunchyroll(context):
	await db_ready.wait()
	data = await db.fetchrow('SELECT * FROM <row> LIMIT 1')
	await db.execute('DELETE FROM <row> WHERE id = $1', data['id'])
	await context.author.send(data['alt'])
	
	


def run():
	bot.run(config['tokens'].pop('discord'))

if __name__ == '__main__':
	run()
