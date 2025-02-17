# QR Code Discord Bot
This is a Discord bot that generate QR Codes from messages. When a user sends a message starting with `!`, the bot will generate a QR code from the message and send it back as an image. The message can be texts, URLs etc.

## Installation
1. Clone the repository:
```sh
git clone https://github.com/nilaysarma/QR-Code-Discord-Bot.git
```

2. Install the required packages:
```sh
pip install -r requirements.txt
```

3. Open the `.env` file and replace `YOUR_BOT_TOKEN_HERE` with your discord bot token.
```
DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE
```

## Usage
1. To run the bot, execute the following command:
- On Windows:
```sh
python main.py
```
- On Linux / MacOS
```sh
python3 main.py
```

2. Start your message with `!` followed by the text/URL you want to convert to a QR code.

3. The bot will respond with a QR code image.

## Example
Here is an example below:

![QR Code Discord Bot](example.png)

## Dependencies
- `discord.py`: Python wrapper for the Discord API.
- `python-dotenv`: Reads key-value pairs from a `.env` file and can set them as environment variables.
- `qrcode[pil]`: A pure Python QR Code generator with PIL (Python Imaging Library) support.