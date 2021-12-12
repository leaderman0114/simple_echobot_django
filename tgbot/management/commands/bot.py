from django.core.management.base import BaseCommand
import logging
from aiogram import Bot, Dispatcher, executor, types
from asgiref.sync import sync_to_async

from tgbot.models import TgUser


TOKEN = 'TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    try: 
        id = message.from_user.id
        await sync_to_async(TgUser.objects.get_or_create, thread_sensitive=True)(chat_id=id)
    except Exception as e:
        print(f"[ERROR] <<< {e} >>>")

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


class Command(BaseCommand):
    help = 'Aiogram bot'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Successfully closed!"))
    
    executor.start_polling(dp, skip_updates=True)