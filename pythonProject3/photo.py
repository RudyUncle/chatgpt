from aiogram import Bot, Dispatcher, executor, types

bot = Bot("5906935409:AAH5yjJbwHHFGFtxaLTzQUFhi_L_nvbyokI")
dp = Dispatcher(bot)
@dp.message_handler(commands=["help", "start"])
async def cmd_start(msg: types.Message) -> None:
    print(msg)
    await msg.answer('<em>Добро пожаловать </em>в <b> чат</b>', parse_mode="HTML")

from aiogram import Bot, Dispatcher, executor, types

bot = Bot("5906935409:AAH5yjJbwHHFGFtxaLTzQUFhi_L_nvbyokI")
dp = Dispatcher(bot)
@dp.message_handler(commands=["help", "start"])
async def cmd_start(msg: types.Message) -> None:
    print(msg)
    await msg.answer('<em>Добро пожаловать </em>в <b> чат</b>', parse_mode="HTML")

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Привет, я еще не умею отвечать на вопросы!')



if __name__ == '__main__':
    executor.start_polling(dp)



if __name__ == '__main__':
    executor.start_polling(dp)
