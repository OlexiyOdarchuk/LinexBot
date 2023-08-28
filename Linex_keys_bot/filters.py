from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id == 5440056373 or message.from_user.id == 1433760480