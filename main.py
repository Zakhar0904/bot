import discord
import random
import yandex
import config 



client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        return
    if message.content == '$hello':
        await message.channel.send("Hi!")
    elif message.content == '$bye':
        await message.channel.send("\U0001f642")
    elif  message.content == 'random':
        r = random.randint(1,10)
        await message.channel.send(str(r))
    elif message.content == 'password':
        await message.channel.send(gen_pass(6))
    elif message.content == 'heads or tails':
        r = random.randint(1,2)
        await message.channel.send(str(r))
        if r == 1:
            await message.channel.send("it came up heads")
            if r == 2:
                await message.channel.send("it came up tails")
    elif message.content == 'games': 
         await message.channel.send("'heads or tails'")           
   
    elif message.content == 'calculater': 
    
         await message.channel.send('enter the first number')
        
         await message.channel.send('enter the second number')
    else:
         await message.channel.send( yandex.gpt(message.content))



def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

client.run(config.discord_key)