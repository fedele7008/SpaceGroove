import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(':p ') or message.content.startswith(':play '):
        await message.channel.send('play')
    
    if message.content.startswith(':skip ') or message.content.startswith(':next '):
        await message.channel.send('skip')
    
    if message.content.startswith(':queue '):
        await message.channel.send('show queue')
    
    if message.content.startswith(':remove '):
        await message.channel.send('remove')

    if message.content.startswith(':leave '):
        await message.channel.send('leave call')

client.run('ODg3NDU3Mzg0MDg2MjU3NzA0.YUEbGA.NPEbwSFv2UcZX8m4LMwq18jaTvo')