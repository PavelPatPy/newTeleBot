from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

kb = types.ReplyKeyboardMarkup(one_time_keyboard=True)
b1 = types.KeyboardButton(text='button1')
b2 = types.KeyboardButton(text='button2')
b3 = types.KeyboardButton(text='button3')
b4 = types.KeyboardButton(text='button4')
kb.add(b1, b2, b3)


@dp.message_handler(commands=['start'])
async def start_handler(massage: types.Message):
    await massage.answer('its help bot', reply_markup=kb)


@dp.message_handler(commands=['welcome', 'about'])
async def cmd_handler(massage: types.Message):
    await massage.answer('its help bot')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
