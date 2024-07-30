from aiogram import Router
from filters import *
from aiogram.filters import StateFilter
import asyncio
from pagination import *
from aiogram.types import CallbackQuery, Message, InputMediaPhoto
from aiogram.exceptions import TelegramBadRequest
from inline_keyboard import *
from url_kbs import *
from lexicon import *
from bot_instance import bot
import json
from aiogram.fsm.context import FSMContext
from FSM import FSM_ST
from postgres_functions import *


lese_router = Router()

@lese_router.callback_query(ENTER_FILTER())
async def press_enter(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=two_site, caption=soderganie_full),
            reply_markup=oglav_kb
        )

    except TelegramBadRequest:
        print('////Into Exeption')
    await callback.answer()

@lese_router.callback_query(VVED_FILTER())
async def press_vvedenie(callback: CallbackQuery, state:FSMContext):
    await state.set_state(FSM_ST.vved)
    user_id = callback.from_user.id
    pic_msg = await return_pic_msg(user_id)
    if pic_msg != '':

        return_to_message = Message(**json.loads(pic_msg))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_pic_msg(user_id)

    text_att = await callback.message.answer(text=vvedenie_text, reply_markup=vved_kb)
    js_atw = text_att.model_dump_json(exclude_none=True)
    await insert_new_jsmess_in_text_msg(user_id, js_atw)
    await callback.answer()

@lese_router.callback_query(ALBUM_FILTER(), StateFilter(FSM_ST.vved))
async def press_album(callback: CallbackQuery):
    user_id = callback.from_user.id
    text_msg = await return_text_msg(user_id)
    if text_msg != '':
        return_to_message = Message(**json.loads(text_msg))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_text_msg(user_id)
    pic_att = await callback.message.answer_photo(pagin_dict[1][0],caption=pagin_dict[1][1],
                                                reply_markup=create_pagination_keyboard())

    js_atw = pic_att.model_dump_json(exclude_none=True)
    await insert_new_jsmess_in_pic_msg(user_id, js_atw)
    await callback.answer()

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед-назад"
# во время взаимодействия пользователя с сообщением-книгой
@lese_router.callback_query(MOVE_PAGE())
async def page_moving(callback: CallbackQuery):
    shitt = -1 if callback.data == 'backward' else 1
    user_id = callback.from_user.id
    await page_icrement(user_id, shitt)
    pagin_index = await return_page_index(user_id)
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=pagin_dict[pagin_index][0], caption=pagin_dict[pagin_index][1]),
            reply_markup=create_pagination_keyboard(pagin_index)
        )
    except TelegramBadRequest:
        print('////Into Exeption')
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=pagin_dict[1][0], caption=pagin_dict[1][1]),
            reply_markup=create_pagination_keyboard(pagin_index))
    await callback.answer()


@lese_router.callback_query(VVED_2_FILTER(), StateFilter(FSM_ST.vved))
async def press_vved_2(callback: CallbackQuery):
    user_id = callback.from_user.id
    text_att = await callback.message.answer(text=vvedenie_text, reply_markup=vved_kb)
    js_atw = text_att.model_dump_json(exclude_none=True)
    await insert_new_jsmess_in_text_msg(user_id, js_atw)
    await callback.answer()

@lese_router.callback_query(ONE_ZERO_FILTER())
async def press_one_zero(callback: CallbackQuery, state:FSMContext):
    print("THIS BUTTOM PUSHED")
    await state.set_state(FSM_ST.part_I)
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=one_zero),
            reply_markup=one_zero_kb
        )
    except TelegramBadRequest:
        print('////Into Exeption')
    await callback.answer()

@lese_router.callback_query(ONE_TWO_FILTER())
async def press_one_two(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=one_two, caption=back),
            reply_markup=one_two_kb
        )
    except TelegramBadRequest:
        print('////Into Exeption 1-2')
    await callback.answer()

@lese_router.callback_query(ONE_THREE_FILTER())
async def press_one_three(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=one_three, caption=back),
            reply_markup=one_three_kb
        )
    except TelegramBadRequest:
        print('////Into Exeption 1-3')
    await callback.answer()


@lese_router.callback_query(ONE_FOUR_FILTER())
async def press_one_four(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=one_fore, caption=back),
            reply_markup=one_four_kb
        )
    except TelegramBadRequest:
        print('////Into Exeption 1-4')
    await callback.answer()

###########################################################################################

@lese_router.callback_query(II_ZERO_FILTER())
async def press_II_zero(callback: CallbackQuery, state:FSMContext):
    await state.set_state(FSM_ST.part_II)

    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=part_II_forzatz),
            reply_markup=II_zero_kb
        )
    except TelegramBadRequest:
        print('////Into press_II_zero Exeption')
    await callback.answer()

@lese_router.callback_query(II_TWO_FILTER())
async def press_II_two(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=part_II_2, caption=back),
            reply_markup=II_two_kb
        )
    except TelegramBadRequest:
        print('////Into Exeption 2-2')
    await callback.answer()

@lese_router.callback_query(II_THREE_FILTER())
async def press_II_three(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=part_II_3, caption=back),
            reply_markup=II_three_kb
        )
    except TelegramBadRequest:
        print('////Into Exeption 2-3')
    await callback.answer()


@lese_router.callback_query(II_FOUR_FILTER())
async def press_II_four(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=part_II_4, caption=back),
            reply_markup=II_four_kb
        )
    except TelegramBadRequest:
        print('////Into Exeption 2-4')
    await callback.answer()
###################################################################################

@lese_router.callback_query(III_ZERO_FILTER())
async def press_III_zero(callback: CallbackQuery, state:FSMContext):
    await state.set_state(FSM_ST.part_III)

    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=part_III_forzatz),
            reply_markup=III_zero_kb
        )
    except TelegramBadRequest:
        print('////Into press_III_zero Exeption')
    await callback.answer()


@lese_router.callback_query(III_FIVE_FILTER())
async def press_III_five(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=part_III_5, caption=back),
            reply_markup=III_6_kb
        )
    except TelegramBadRequest:
        print('////Into press_III_6 Exeption')
    await callback.answer()


@lese_router.callback_query(III_SEX_FILTER())
async def press_III_sex(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=part_III_6, caption=back),
            reply_markup=III_7_kb
        )
    except TelegramBadRequest:
        print('////Into press_III_7 Exeption')
    await callback.answer()


@lese_router.message()
async def send_echo(message: Message):
    print("Works send_echo")
    att = await message.answer(other_ant)
    await asyncio.sleep(4)
    await att.delete()
    await message.delete()

