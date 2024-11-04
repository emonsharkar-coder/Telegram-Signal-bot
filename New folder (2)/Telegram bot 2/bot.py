import random
import asyncio
from telegram import Bot
from telegram.error import TelegramError

TOKEN = '7524461281:AAEeaTCm5gxQ2nPJIkBiXxTe2I8qaoV3FZs'
CHANNEL_ID = '@bdtgamesignal_hgzy'

bot = Bot(token=TOKEN)

#  sticker file ID
BIG_STICKER_ID = 'CAACAgUAAxkBAAIBYmNJ4kU_Tc9EOYkgc4FXAAGG4kLQ0AACyQEAAi6E6FCXqPjCV1qgSyME'
SMALL_STICKER_ID = 'CAACAgUAAxkBAAIBZ2NJ4mrfZST4O4b3QZVfL0Z4OTRxAAK0AQACLoToUJd69PCVJqrIzDME'

async def send_signal():
    message = random.choice(['big', 'small'])
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=message)
        sticker_id = BIG_STICKER_ID if message == 'big' else SMALL_STICKER_ID
        await bot.send_sticker(chat_id=CHANNEL_ID, sticker=sticker_id)
        print(f"Sent: {message} with sticker")
    except TelegramError as e:
        print(f"Error sending message or sticker: {e}")

async def main():
    while True:
        await send_signal()
        await asyncio.sleep(10)

asyncio.run(main())
