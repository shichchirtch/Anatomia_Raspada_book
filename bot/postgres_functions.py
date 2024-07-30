from database import session_marker, User
from sqlalchemy import select

async def insert_new_user_in_table(user_tg_id: int, name: str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        if not needed_data:
            print('Now we are into first function')
            new_us = User(tg_us_id=user_tg_id, user_name=name)
            session.add(new_us)
            await session.commit()


async def check_user_in_table(user_tg_id:int):
    """Функция проверяет есть ли юзер в БД"""
    async with session_marker() as session:
        print("Work check_user Function")
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        data = query.one_or_none()
        return data

#####################################################################################

async def insert_new_jsmess_in_pic_msg(user_tg_id: int, new_page:str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        needed_data.pic_msg = new_page
        await session.commit()

async def insert_new_jsmess_in_text_msg(user_tg_id: int, new_page:str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        needed_data.text_msg = new_page
        await session.commit()

async def page_icrement(user_tg_id: int, schritt:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        needed_data.page += schritt
        await session.commit()


######################################################################################

async def return_page_index(user_id):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        page = needed_data.page
        return page


async def return_pic_msg(user_id):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        pic_msg = needed_data.pic_msg
        return pic_msg

async def return_text_msg(user_id):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        text_msg = needed_data.text_msg
        return text_msg

##########################################################################################

async def reset_text_msg(user_tg_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        needed_data.text_msg = ''
        await session.commit()

async def reset_pic_msg(user_tg_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        needed_data.pic_msg = ''
        await session.commit()

async def reset_page(user_tg_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        needed_data.page = 1
        await session.commit()


async def page_listai(user_id:int, schift:int):
    async with session_marker() as session:
        print("Work page_moving Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        print('data = ', needed_data)
        needed_data.page +=schift
        await session.commit()









