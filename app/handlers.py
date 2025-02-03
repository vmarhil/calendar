# from aiogram import Router, F
# from aiogram.types import Message
# from aiogram.filters import CommandStart, CommandObject

# router = Router()

# @router.message(CommandStart(deep_link=True, magic=F.args.isdigit()))
# async def cmd_start(message: Message, command: CommandObject):
#     await message.answer(f'Привет! Ты пришел от {command.args}')


# @router.message(F.photo)
# async def get_photo(message: Message):
#     await message.answer(f'ID фотографии: {message.photo[-1].file_id}')