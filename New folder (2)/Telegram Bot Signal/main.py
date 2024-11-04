import random
import asyncio
from telegram import Bot
from telegram.error import TelegramError


TOKEN = '7854854102:AAHcO7z88eTUgAjDKJvXFkwnRLn_wpFsJgw'
CHANNEL_ID = '@help263'

bot = Bot(token=TOKEN)


async def send_signal():
    message = random.choice(['big', 'small']) 
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=message)  
        print(f"Sent: {message}")
    except TelegramError as e:
        print(f"Error sending message: {e}")


async def main():
    while True:
        await send_signal()
        await asyncio.sleep(10)  


asyncio.run(main())
