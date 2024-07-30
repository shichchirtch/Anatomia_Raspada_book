from aiogram.types import CallbackQuery, Message
from aiogram.filters import BaseFilter
from postgres_functions import check_user_in_table

class PRE_START(BaseFilter):
    async def __call__(self, message: Message):
        print("PRE_START Filter works")
        user_tg_id = message.from_user.id
        if await check_user_in_table(user_tg_id):
            return False
        return True


class ENTER_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Содержание':
            return True
        return False

class VVED_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Введение':
            return True
        return False

class ALBUM_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Реальные Истории':
            return True
        return False

class MOVE_PAGE(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data in ['forward', 'backward']:
            return True
        return False


class VVED_2_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Так выглядят':
            return True
        return False


class ONE_ZERO_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Часть I':
            return True
        return False

class ONE_TWO_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='От руин':
            return True
        return False

class ONE_THREE_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Как в современной':
            return True
        return False

class ONE_FOUR_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Институты':
            return True
        return False

#############################################################################################

class II_ZERO_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Часть II':
            return True
        return False

class II_TWO_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Кто принимает':
            return True
        return False


class II_THREE_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Принципы и парадоксы':
            return True
        return False


class II_FOUR_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Эволюция':
            return True
        return False
####################################################################################

class III_ZERO_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Часть III':
            return True
        return False


class III_FIVE_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Права':
            return True
        return False



class III_SEX_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data =='Синдром':
            return True
        return False



