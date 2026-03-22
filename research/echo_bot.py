import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
print(f"Bot Token Loaded: {TELEGRAM_BOT_TOKEN}")

# Initialize Bot and Dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start", "help"))
async def command_start_handler(message: types.Message):
    """This handler will be called when user sends /start command"""
    await message.reply("Hi! I'm an Echo Bot. Send me any message!")

@dp.message()
async def echo_handler(message: types.Message):
    """This handler will echo the user's message"""
    if message.text:
        await message.reply(message.text)
    else:
        await message.reply("Thank you!")

async def main():
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())