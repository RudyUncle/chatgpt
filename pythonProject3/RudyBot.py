from aiogram import Bot, Dispatcher, executor, types

bot = Bot("5906935409:AAH5yjJbwHHFGFtxaLTzQUFhi_L_nvbyokI")
dp = Dispatcher(bot)
@dp.message_handler(commands=["help", "start"])
async def cmd_start(msg: types.Message) -> None:
    print(msg)
    await msg.answer("Привет")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    executor.start_polling(dp)
