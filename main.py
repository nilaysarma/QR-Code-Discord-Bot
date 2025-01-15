import discord
import os
from dotenv import load_dotenv
from qr_code_generator import convert_to_qr
import io

# Load the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Bot startup
@client.event
async def on_ready():
    print(f'{client.user} is ready to go!')

# Bot message handling and QR code generation
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        try:
            print(f'{message.author} in {message.channel} said: {message.content}')
            data = message.content[1:]
            img = convert_to_qr(data)
            image_binary = io.BytesIO()
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await message.channel.send('Here is your QR code!')
            await message.channel.send(file=discord.File(fp=image_binary, filename='qr_code.png'))
            image_binary.close()
            return
        except Exception as e:
            print(e)

client.run(TOKEN)