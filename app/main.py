import time
import random
import telegram
import asyncio

# Bot token and channel ID
TOKEN = '7854854102:AAHcO7z88eTUgAjDKJvXFkwnRLn_wpFsJgw'
CHANNEL_ID = '@bdtgamesignal_hgzysignal'

# Paths to the "Big" and "Small" images
BIG_IMAGE_PATH = "C:/Users/Premium Laptop/Desktop/Telegram bot 4/image/big.png"
SMALL_IMAGE_PATH = "C:/Users/Premium Laptop/Desktop/Telegram bot 4/image/small.png"

# Initialize bot
bot = telegram.Bot(token=TOKEN)

# Function to send checking message
async def send_checking_message():
    message = "Checking New Signal........🚨"
    await bot.send_message(chat_id=CHANNEL_ID, text=message)

# Function to send signal image only
async def send_signal():
    # Randomly select between "Big" and "Small" signal
    signal = random.choice(["Big", "Small"])

    # Select the corresponding image based on the signal
    image_path = BIG_IMAGE_PATH if signal == "Big" else SMALL_IMAGE_PATH
    with open(image_path, 'rb') as image_file:
        await bot.send_photo(chat_id=CHANNEL_ID, photo=image_file)

    # Follow-up message
    follow_up_message = """
    🔔 সবাইকে অনুরোধ করছি ৮ স্টেপ নিয়েই খেলুন 🔔

    ⚠ ওয়ার্নিং: আমাদের গ্রুপের লিংক ব্যবহার করে আইডি না খুললে সিগন্যাল মিলবে না।

    🔗 সাইট লিংক: https://hgzy.bet/#/register?invitationCode=21416326321

    প্রশ্ন থাকলে বা সহায়তা প্রয়োজন হলে, আমাদের হেল্প বটের সাথে যোগাযোগ করুন 👉 @bdtgamesignalhelpe_bot 💬
    """
    await bot.send_message(chat_id=CHANNEL_ID, text=follow_up_message)

# Main function to run the bot
async def run_bot():
    while True:
        # Send checking message 5 seconds before the signal
        await send_checking_message()
        await asyncio.sleep(5)

        # Send the random signal image and follow-up message
        await send_signal()

        # Wait for 1 minute before the next signal
        await asyncio.sleep(55)

# Start the bot
asyncio.run(run_bot())
