from aiogram.types import BotCommand
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Функция для настройки кнопки Menu бота
async def set_main_menu(bot):
    # Создаем список с командами и их описанием для кнопки menu
    # bot
    main_menu_commands = [
        BotCommand(command='/exit',
                   description='Вернуться к оглавлению'),
        BotCommand(command='/help',
                   description='Bot commands')
    ]

    await bot.set_my_commands(main_menu_commands)

start_button = KeyboardButton(text='/start')

pre_start_clava = ReplyKeyboardMarkup(
    keyboard=[[start_button]],
    resize_keyboard=True,
    input_field_placeholder='Приятного чтения'
)