from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pagination import pagin_dict


enter_button = InlineKeyboardButton(text='Содержание', callback_data='Содержание')

enter_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[enter_button]])


vvedenie_button = InlineKeyboardButton(text='Введение', callback_data='Введение')
part_1_button = InlineKeyboardButton(text='Часть I. Место права на жизнь', callback_data='Часть I')
part_2_button = InlineKeyboardButton(text='Часть II. Правоохранительная система', callback_data='Часть II')

# part_2_button = InlineKeyboardButton(text='****', callback_data='****')
part_3_button = InlineKeyboardButton(text='Часть III. Как общество и государство говорят о правах человека', callback_data='Часть III')
zakl_button = InlineKeyboardButton(text='Заключение', url='https://telegra.ph/Vmesto-zaklyucheniya-S-chem-my-prishli-v-2024-god-07-29')

oglav_kb = InlineKeyboardMarkup(inline_keyboard=[[vvedenie_button], [part_1_button], [part_2_button], [part_3_button], [zakl_button]])
#################################################################################################################

albom_button = InlineKeyboardButton(text='Реальные Истории', callback_data='Реальные Истории')
text_vved_button = InlineKeyboardButton(text='Так выглядят пытки', url='https://telegra.ph/Tak-vyglyadyat-pytki-07-24')

vved_kb = InlineKeyboardMarkup(inline_keyboard=[[albom_button], [text_vved_button]])

########################################################################################################




def create_pagination_keyboard(page=1) -> InlineKeyboardMarkup:
    forward_button = InlineKeyboardButton(text=f'>>', callback_data='forward')
    backward_button = InlineKeyboardButton(text='<<', callback_data='backward')
    if page == 1:
        pagination_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[forward_button]]

        )
        return pagination_keyboard
    elif page<10:
        pagination_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[backward_button, forward_button,]])
        return pagination_keyboard
    else:
        pagination_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[backward_button, text_vved_button]])
        return pagination_keyboard
