import logging

from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apples_keyboard,\
    eda,lifehack,news,vkus,skils,connect,ed,drin,kats,eatO ,free, pots,pans,colds,peat,donates,free_eat,\
    alls,shcars,sites
#from keyboards.inline import eda
from keyboards.defolt import menu
from keyboards.inline import fruitt,defolt,feda,milk,other,small,wow
from config import url_donate
from loader import dp, bot

@dp.message_handler(text="Еда 🍏")
async def EDA(message: Message):
    await message.answer(text='Какая цель похода в магазин?',reply_markup=eda)

@dp.message_handler(text="Лайфхаки и халява 👌")
async def LIFEHACK(message: Message):
    await message.answer(text='Я приготовил для тебя особенные взломы жизни',reply_markup=lifehack)

@dp.message_handler(text="Новости Москвы")
async def show_items(message: Message):
    await message.answer(text='Самые горячие новости столицы тут',reply_markup=news)

@dp.message_handler(text="Сначала")
async def show_items(message: Message):
    await message.answer(text=f'Снова здравствуй, {message.from_user.full_name}!\n Я - <b>СтудХелпер</b>, твой личный помощник в выборе самого лучшего и вкусного:)', reply_markup=restart)

@dp.message_handler(text="Поддержать проект 🆘")
async def donate(message: Message):
    await message.answer(text='Я очень рад, если мой бот вам помог. Однако создание бота, обеспечение работоспособности,сервер очень затратно.\n'
                              '\Буду крайне признателен каждому рублю и распространению.\nРеквезиты: QIWI +79520669369\nКарта Тинькофф-Банк 5536 9137 8751 6745',reply_markup=donates)

@dp.message_handler(text="Книга жалоб и предложений ✍")
async def show_items(message: Message):
    await message.answer(text='Я буду признателен, если у вас есть идеи, пожелания и критика.\nСвяжитесь со мной!', reply_markup=connect)

@dp.message_handler(text="Корзина 🛒")
async def show_items(message: Message):
    await message.answer(text='В вашей корзине, находится следующее:*в разработке*', reply_markup=None)

# Попробуйем отловить по встроенному фильтру, где в нашем call.data содержится "pear"
@dp.callback_query_handler(text_contains="pear")
async def buying_pear(call: CallbackQuery):
    # Обязательно сразу сделать answer, чтобы убрать "часики" после нажатия на кнопку.
    # Укажем cache_time, чтобы бот не получал какое-то время апдейты, тогда нижний код не будет выполняться.
    await call.answer(cache_time=60)

    callback_data = call.data

    # Отобразим что у нас лежит в callback_data
    # logging.info(f"callback_data='{callback_data}'")
    # В Python 3.8 можно так, если у вас ошибка, то сделайте предыдущим способом!
    logging.info(f"{callback_data=}")

    await call.message.answer("Вы выбрали купить грушу. Груша всего одна. Спасибо.",
                              reply_markup=pear_keyboard)
###
@dp.callback_query_handler(text_contains="vkus")
async def vkusn(call: CallbackQuery):
    await call.message.answer("Прямо сейчас или есть время приготовить?", reply_markup= vkus)
###

@dp.callback_query_handler(text_contains="time")
async def time(call: CallbackQuery):
    await call.message.answer("Уровень сложности готовки", reply_markup=skils)
###

@dp.callback_query_handler(text_contains="now")
async def now(call: CallbackQuery):
    await call.message.answer("Чего изволишь?", reply_markup=ed)
###
@dp.callback_query_handler(text_contains="product")
async def time(call: CallbackQuery):
    await call.message.answer("Уровень сложности готовки", reply_markup=skils)
###

@dp.callback_query_handler(text_contains="pot")
async def product_pot(call: CallbackQuery):
    await call.message.answer("Блюда в кастрюле:", reply_markup= pots)
###

@dp.callback_query_handler(text_contains="pan")
async def product_pan(call: CallbackQuery):
    await call.message.answer("Блюда на сковородке", reply_markup= pans)
###

@dp.callback_query_handler(text_contains="cold")
async def product_cold(call: CallbackQuery):
    await call.message.answer("Салаты и десерты", reply_markup= colds)
###

@dp.callback_query_handler(text_contains="all")
async def ALL(call: CallbackQuery):
    await call.message.answer("Все рецепты", reply_markup= alls)
###

@dp.callback_query_handler(text_contains="easy")
async def product1(call: CallbackQuery):
    await call.message.answer("На чем будешь готовить?", reply_markup= peat)
###

@dp.callback_query_handler(text_contains="hard")
async def product2(call: CallbackQuery):
    await call.message.answer("На чем будешь готовить?", reply_markup= peat)
###

@dp.callback_query_handler(text_contains="fruit")
async def fruits(call: CallbackQuery):
    await call.message.answer("Фрукты и овощи", reply_markup= fruit)

###

@dp.callback_query_handler(text_contains="choose")
async def choose(call: CallbackQuery):
    await call.message.answer("Список разделов магазина:", reply_markup= kats)
###

@dp.callback_query_handler(text_contains="xz")
async def xz(call: CallbackQuery):
    await call.message.answer("Случайный выбор предлагает...\n*Рандом в разабоотке*", reply_markup= skils)
###

@dp.callback_query_handler(text_contains="drink")
async def drink(call: CallbackQuery):
    await call.message.answer("Какие напитки интересуют?", reply_markup= drin)
###

@dp.callback_query_handler(text_contains="eat")
async def eat(call: CallbackQuery):
    await call.message.answer("Что хочешь?", reply_markup= eatO)
###

@dp.callback_query_handler(text_contains="free")
async def free_f(call: CallbackQuery):
    await call.message.answer("Акции и купоны на:", reply_markup= free)
###

@dp.callback_query_handler(text_contains="feat")
async def feat(call: CallbackQuery):
    await call.message.answer("Купоны на:", reply_markup= free_eat)
###

@dp.callback_query_handler(text_contains="shcar")
async def feat(call: CallbackQuery):
    await call.message.answer("Купоны на каршеринг:", reply_markup= shcars)
###

@dp.callback_query_handler(text_contains="site")
async def feat(call: CallbackQuery):
    await call.message.answer("Залипательные сайты:", reply_markup= sites)
###

@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    # Выведем callback_data и тут, чтобы сравнить с предыдущим вариантом.
    logging.info(f"{callback_data=}")

    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали купить яблоки. Яблок всего {quantity}. Спасибо.",
                              reply_markup=apples_keyboard)

# Попробуем использовать фильтр от CallbackData


@dp.callback_query_handler(text_contains="back")
async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    #await call.answer("Вы отменили эту покупку!", show_alert=True)

    # Вариант 1 - Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(text='rename',reply_markup=skils)

    # Вариант 2 отправки клавиатуры (по API)
    # await bot.edit_message_reply_markup(chat_id=call.from_user.id,
    #                                     message_id=call.message.message_id,
    #                                     reply_markup=None)
