from aiogram import Router, F, html
import asyncio
from bot_instance import bot
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove, InputMediaPhoto
from aiogram.filters import CommandStart, Command
from url_kbs import one_zero_kb, II_zero_kb, III_zero_kb
import json
from aiogram.exceptions import TelegramBadRequest
from filters import PRE_START
from pagination import *
from start_menu import pre_start_clava
from lexicon import *
from aiogram.fsm.context import FSMContext
from inline_keyboard import *
from postgres_functions import *
from FSM import FSM_ST



ch_router = Router()


@ch_router.message(~F.text)
async def delete_not_text_type_messages(message: Message):
    await message.delete()


@ch_router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    user_name = message.from_user.first_name
    user_tg_id = message.from_user.id
    if not await check_user_in_table(user_tg_id):
        await insert_new_user_in_table(user_tg_id, user_name)
        await state.set_state(FSM_ST.after_start)

        first_antwort = await message.answer(
            text=f'<b>{html.bold(html.quote(user_name))}</b>, сейчас Вы узнаете много интересного !',
            parse_mode=ParseMode.HTML,
            reply_markup=ReplyKeyboardRemove())

        att = await message.answer_photo(
            photo=forzatz,
            reply_markup=enter_keyboard)
        start_page = att.model_dump_json(exclude_none=True)
        await insert_new_jsmess_in_pic_msg(user_tg_id, start_page)
        await asyncio.sleep(4)
        await first_antwort.delete()
    else:
        await message.delete()




@ch_router.message(PRE_START())
async def before_start(message: Message):
    prestart_ant = await message.answer(text='Нажми на кнопку <b>start</b> !',
                                        reply_markup=pre_start_clava)
    await message.delete()
    await asyncio.sleep(4)
    await prestart_ant.delete()


@ch_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    print('help works')
    att = await message.answer(help_command)
    await asyncio.sleep(55)
    await message.delete()
    await att.delete()

@ch_router.message(Command(commands='exit'))
async def process_command_exit(message: Message, state: FSMContext):
    print('exit works\n ')
    user_id = message.from_user.id
    await reset_page(user_id)
    pic_msg = await return_pic_msg(user_id)
    text_msg = await return_text_msg(user_id)
    if text_msg != '':
        print(' if text_msg != NONe')
        return_to_message = Message(**json.loads(text_msg))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_text_msg(user_id)

    if pic_msg !='':
        try:
            await message.edit_media(
                media=InputMediaPhoto(media=two_site, caption=soderganie_full),
            reply_markup=oglav_kb)

        except TelegramBadRequest:
            print('////Into EXIT Exeption')
            return_to_message = Message(**json.loads(pic_msg))
            msg = Message.model_validate(return_to_message).as_(bot)
            await msg.delete()
            att = await message.answer_photo(two_site, caption=soderganie_full, reply_markup=oglav_kb)
            js_f_atw = att.model_dump_json(exclude_none=True)
            await insert_new_jsmess_in_pic_msg(user_id, js_f_atw)
    else:
        att = await message.answer_photo(
            photo=two_site,
            reply_markup=oglav_kb)
        json_att = att.model_dump_json(exclude_none=True)
        await insert_new_jsmess_in_pic_msg(user_id, json_att)

    await message.delete()


@ch_router.message(Command(commands='back'))
async def process_command_back(message: Message, state: FSMContext):
    print('back works\n ')
    user_id = message.from_user.id
    pic_msg = await return_pic_msg(user_id)
    text_msg = await return_text_msg(user_id)
    if text_msg != '':
        print(' if text_msg != NONe')
        return_to_message = Message(**json.loads(text_msg))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_text_msg(user_id)

    current_state = await state.get_state()
    cut_state = current_state.split(':')[1]
    print('current_state = ', current_state)

    state_dict = {'part_I':(one_zero, one_zero_kb),
                  'part_II':(part_II_forzatz, II_zero_kb),
                  'part_III':(part_III_forzatz, III_zero_kb)}


    if pic_msg !='':
        try:
            await message.edit_media(
                media=InputMediaPhoto(media=state_dict[cut_state][0]),
            reply_markup=state_dict[cut_state][1])

        except TelegramBadRequest:
            print('////Into BACK Exeption')
            return_to_message = Message(**json.loads(pic_msg))
            msg = Message.model_validate(return_to_message).as_(bot)
            await msg.delete()
            att = await message.answer_photo(state_dict[cut_state][0], reply_markup=state_dict[cut_state][1])
            js_f_atw = att.model_dump_json(exclude_none=True)
            await insert_new_jsmess_in_pic_msg(user_id, js_f_atw)
    else:
        att = await message.answer_photo(
            photo=state_dict[cut_state][0],
            reply_markup=state_dict[cut_state][1])
        json_att = att.model_dump_json(exclude_none=True)
        await insert_new_jsmess_in_pic_msg(user_id, json_att)

    await message.delete()







# @ch_router.message(Command(commands='otzyv'), ~StateFilter(FSM_NAMES.waiting))
# async def process_command_otzyv(message: Message, state: FSMContext):
#     print("**************************************")
#     language = users_db[message.from_user.id]['language']
#     await state.set_state(FSM_NAMES.otzyv)
#     att = await message.answer(text_for_send_refferal[language])
#     await message.delete()
#     await asyncio.sleep(12)
#     await att.delete()
#
# @ch_router.message(StateFilter(FSM_NAMES.otzyv))
# async def process_send_otzyv(message: Message, state: FSMContext):
#     print('feed_back sending\n ')
#     await state.set_state(FSM_NAMES.waiting)
#     language = users_db[message.from_user.id]['language']
#     sending_data = message.text
#     user_id = message.from_user.id
#     user_name = message.from_user.first_name
#     join_text = f'User_id {user_id}, user_name  {user_name} \n\nsend MESSAGE \n\n{sending_data}'
#     await message.bot.send_message(chat_id=-4241930933, text=join_text)
#     await asyncio.sleep(1)
#     await message.delete()
#     att = await message.answer(success_send[language])
#     await asyncio.sleep(3)
#     await att.delete()
#     wait_att = await message.answer(waiting_15[language])
#     await asyncio.sleep(3)
#     await  asyncio.sleep(900)
#     await wait_att.delete()
#     await state.set_state(FSM_NAMES.base_part)

