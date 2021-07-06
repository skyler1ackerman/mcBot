import discord, shortuuid, asyncio
from config import TOKEN
from discord.ext import commands

shortuuid.set_alphabet('0123456789')

all_items = dict()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
	print("Candice is online.")
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('I am ALIVE'))

# async def get
@bot.command(name='sell')
async def trade(ctx):
	await ctx.send(f'Hello {ctx.author.name}, what would you like to sell today?')

	def check(m):
		return m.author == ctx.author and m.channel == ctx.channel

	try:
		item_msg = await bot.wait_for('message', check=check)
	except asyncio.TimeoutError:
		await ctx.send('Trade timed out')
		return

	await ctx.send(f'How many {item_msg.content} are you selling?')

	def numCheck(m):
		return check(m) and m.content.isnumeric()

	try:
		number_msg = await bot.wait_for('message', check=numCheck, timeout=60)
	except asyncio.TimeoutError:
		await ctx.send('Trade timed out')
		return

	await ctx.send('Item added to roster')

	# TODO: Don't allow overlaps
	shortID = shortuuid.uuid()[0:6]

	all_items[shortID] = {'item': item_msg.content, 'quantity': int(number_msg.content), \
	 'seller': ctx.author.name, 'offers' = list()} 

@bot.command()
async def offer(ctx, tradeID)

@bot.command()
async def list(ctx):
	await ctx.send(all_items)

bot.run(TOKEN)