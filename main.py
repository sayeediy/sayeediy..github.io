from aiogram import Bot, Dispatcher

import asyncio
import configg


bot = Bot(configg.TOKEN)
dp = Dispatcher(bot)

async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
