import discord
import random
from discord.ext import commands
client = commands.Bot(command_prefix = '-')
TOKEN = 'ODA4NTE5NTczNTU2OTUzMTM4.YCHuhw.EHKaO-zY-XtWiX7cGWei388ZsdA'
@client.event
async def on_ready():
    print('bot is ready')
#ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Noh! {round(client.latency*1000)}ms')

#information
@client.command(aliases=['i'])
async def info(ctx):
    await ctx.send(f'This is still in constant development since 8/02/2021.\nPrefix is -, and features currently available are: 8ball, EPL.')
#8ball
@client.command(aliases=['8ball','8b'])
async def _8ball(ctx, *, question):
    responses = ['it is certain',
                 'it is decidedly so',
                 'Without a doubt',
                 'Yes, definitely',
                 'You may rely on this',
                 'As i see it, yes',
                 'Most likely',
                 'Outlook looks good',
                 'Yes',
                 'Signs point to yes',
                 'Reply hazy, try again',
                 'Ask again later',
                 'Better not tell you now',
                 'cannot predict now',
                 'concentrate and ask again',
                 'Dont count on it',
                 'My sources say no',
                 'Outlook not so good',
                 'Very doubtful',
                 'Tak',
                 'Noh',
                 'Nie',
                 'Si',
                 'No']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#rip
@client.command(aliases=['r'])
async def rip(ctx):
    death_cause = ['You are now in a sand coffin',
                   'A snake bit you',
                   'You ate a kinder egg, you choke on it',
                   'A fish fell from the sky and landed on your head',
                   'Lee Jong Suk kissed you, you get a heart attack',
                   'Yungblud told you to be fooking happy',
                   'A drunk dude hugs you a bit too hard']
    await ctx.send(f'{random.choice(death_cause)}, so you are now dead.')

#English pro level
@client.command(aliases=['engpro'])
async def english_pro(ctx):
    percent = []
    randoint=random.randint(1,100)
    randoint= str(randoint)
    percent.append(randoint)
    await ctx.send(f'Your english pro level is: {random.choice(percent)}%')
#Polish pro level
@client.command(aliases=['plpro'])
async def polish_pro(ctx):
    percentp = []
    randointp=random.randint(1,100)
    randointp= str(randointp)
    percentp.append(randointp)
    await ctx.send(f'Twój poziom polskiego to: {random.choice(percentp)}%')

@client.command(aliases=['esppro'])
async def spanish_pro(ctx):
    percentes = []
    randointes=random.randint(1,100)
    randointes= str(randointes)
    percentes.append(randointes)
    await ctx.send(f'Tu nivel de español pro es: {random.choice(percentes)}%')

client.run(TOKEN)
