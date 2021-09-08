from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_APPLES, URL_PEAR,URL_news,url_me,url_plov,url_cez,url_sup, url_gsup,url_oliv,url_salvlav,url_borch,url_makSm,url_makSsh, \
    url_mplov,url_shava, url_dran,url_kor,url_donate,url_kfc,url_bk,url_mc, url_vill, url_belca,url_ya
from keyboards.inline.callback_datas import buy_callback

# Вариант 2 - с помощью row_width и insert.
choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple:5")
choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)

###

eda=InlineKeyboardMarkup(row_width=1)
eda1=InlineKeyboardButton(text='Просто, за вкусняшками',callback_data="vkus")
eda2=InlineKeyboardButton(text='Рецепты, буду готовить',callback_data='product')
eda3=InlineKeyboardButton(text='Вообще не знаю(',callback_data='xz')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
eda.add(eda1,eda2,eda3,back)
###

kats=InlineKeyboardMarkup(row_width=3)
k1 = InlineKeyboardButton(text="Овощи и фрукты", callback_data='fruit')
k2 = InlineKeyboardButton(text="Молочка", callback_data='milk')
k3 = InlineKeyboardButton(text="Приправы и мелочь", callback_data='small')
k4 = InlineKeyboardButton(text="К чаю", callback_data='tea')
k9= InlineKeyboardButton(text='Замороженное',callback_data='freeze')
k10= InlineKeyboardButton(text='Напитки б/а',callback_data='drinks')
k11= InlineKeyboardButton(text='Алкоголь',callback_data='alco')
k5 = InlineKeyboardButton(text="Химия и др.", callback_data='other')
k6 = InlineKeyboardButton(text="Особенное", callback_data='wow')
k7 = InlineKeyboardButton(text="На каждый день", callback_data='defolt')
k8 = InlineKeyboardButton(text="У кассы", callback_data='cassa')
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
kats.add(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,back)
###

vkus=InlineKeyboardMarkup(row_width=1)
v1=InlineKeyboardButton(text='Прямо сейчас',callback_data='now')
v2=InlineKeyboardButton(text='Есть время приготовить',callback_data='time')
kat=InlineKeyboardButton(text='Выбрать раздел магазина',callback_data='choose')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
vkus.add(v1,v2,kat,back)
###


###

skils=InlineKeyboardMarkup(row_width=1)
s1=InlineKeyboardButton(text='Легко',callback_data='easy')
s2=InlineKeyboardButton(text='Трудно',callback_data='hard')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
skils.add(s1,s2,back)
###

peat=InlineKeyboardMarkup(row_width=2)
p1 = InlineKeyboardButton(text='Кастрюля',callback_data='pot')
p2 = InlineKeyboardButton(text='Сковородка',callback_data='pan')
p3 = InlineKeyboardButton(text='Техника',callback_data='other')
p4 = InlineKeyboardButton(text='Салаты и десерты',callback_data='cold')
p5 = InlineKeyboardButton(text='Неважно',callback_data='all')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
peat.add(p1,p2,p3,p4,p5,back)
###

pots=InlineKeyboardMarkup(row_width=2)
po1=InlineKeyboardButton(text="Крестянский суп",url=url_sup)
po2=InlineKeyboardButton(text="Быстрый борщ",url=url_borch)
po3=InlineKeyboardButton(text="Гороховый супец",url=url_gsup)
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
pots.add(po1,po2,po3,back)
###

pans=InlineKeyboardMarkup(row_width=2)
pa1=InlineKeyboardButton(text="Классический плов",url=url_plov)
pa2=InlineKeyboardButton(text="Шаурма на сковородке",url=url_shava)
pa3=InlineKeyboardButton(text="Вкусные драники за 5 минут",url=url_dran)
pa4=InlineKeyboardButton(text="Корейская марковка",url=url_kor)
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
pans.add(pa1,pa2,pa3,pa4,back)
###

donates=InlineKeyboardMarkup(row_width=1)
D=InlineKeyboardButton(text="Поддержать",url=url_donate)
donates.add(D)
###

colds=InlineKeyboardMarkup(row_width=2)
c1=InlineKeyboardButton(text="Салат в лаваше",url=url_salvlav)
c2=InlineKeyboardButton(text="Классическое оливье",url=url_oliv)
c3=InlineKeyboardButton(text="Вкусный цезарь с сухариками",url=url_cez)
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
colds.add(c1,c2,c3,back)
###

alls=InlineKeyboardMarkup(row_width=2)
po1=InlineKeyboardButton(text="Крестянский суп",url=url_sup)
po2=InlineKeyboardButton(text="Быстрый борщ",url=url_borch)
po3=InlineKeyboardButton(text="Гороховый супец",url=url_gsup)

pa1=InlineKeyboardButton(text="Классический плов",url=url_plov)
pa2=InlineKeyboardButton(text="Шаурма на сковородке",url=url_shava)
pa3=InlineKeyboardButton(text="Вкусные драники за 5 минут",url=url_dran)
pa4=InlineKeyboardButton(text="Корейская марковка",url=url_kor)

c1=InlineKeyboardButton(text="Салат в лаваше",url=url_salvlav)
c2=InlineKeyboardButton(text="Классическое оливье",url=url_oliv)
c3=InlineKeyboardButton(text="Вкусный цезарь с сухариками",url=url_cez)
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
alls.add(po1,po2,po3,pa1,pa2,pa3,pa4,c1,c2,c3,back)
###

ed=InlineKeyboardMarkup(row_width=1)
eat=InlineKeyboardButton(text='Поесть',callback_data='eat')
drink=InlineKeyboardButton(text='Попить',callback_data='drink')
kat=InlineKeyboardButton(text='Выбрать раздел магазина',callback_data='choose')
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
ed.add(eat,drink,kat,back)
###

eatO=InlineKeyboardMarkup(row_width=2)
ea1=InlineKeyboardButton(text='Похрустеть и т.п.🍿',callback_data='hrust')
ea2=InlineKeyboardButton(text='Перекусить🍔',callback_data='kus')
ea3=InlineKeyboardButton(text='Что-то необычное🔮',callback_data='wow')
kat=InlineKeyboardButton(text='Выбрать раздел магазина',callback_data='choose')
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
eatO.add(ea1,ea2,ea3,kat,back)


drin=InlineKeyboardMarkup(row_width=2)
d1 = InlineKeyboardButton(text='Газировка',callback_data='gas')
d2 = InlineKeyboardButton(text='Сок',callback_data='sok')
d3 = InlineKeyboardButton(text='Энергетики',callback_data='energy')
d4 = InlineKeyboardButton(text='Алькоголь',callback_data='alcogol')
kat=InlineKeyboardButton(text='Выбрать раздел магазина',callback_data='choose')
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
drin.add(d1,d2,d3,d4,kat,back)
###

lifehack=InlineKeyboardMarkup(row_width=2)
lh1=InlineKeyboardButton(text='Халява и купоны 💸',callback_data='free')
lh2=InlineKeyboardButton(text='Куда сходить в МСК 🌇',callback_data='msk')
lh3=InlineKeyboardButton(text='Залипательные сайты',callback_data='site')
lh4=InlineKeyboardButton(text='Шутки и анекдоты',callback_data='joke')
lifehack.add(lh1,lh2,lh3,lh4)
###

free=InlineKeyboardMarkup(row_width=2)
f1 = InlineKeyboardButton(text='Еда и фастфуд',callback_data='feat')
f2 = InlineKeyboardButton(text='Доставка',callback_data='dilivery')
f3 = InlineKeyboardButton(text='Такси',callback_data='taxi')
f4 = InlineKeyboardButton(text='Каршеринг',callback_data='shcar')
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
free.add(f1,f2,f3,f4,back)
###

shcars=InlineKeyboardMarkup(row_width=1)
sh1 = InlineKeyboardButton(text='Делимобил :  ,<b> REFJMW7L <b>')
sh2 = InlineKeyboardButton(text='Rentmee :  ,<b> BA669369 <b>')
sh3 = InlineKeyboardButton(text='Belka car',url=url_belca)
sh4 = InlineKeyboardButton(text='Яндекс Драйв',url=url_ya)
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
shcars.add(sh1,sh2,sh3,sh4,back)
###

sites=InlineKeyboardMarkup(row_width=1)
si1=InlineKeyboardButton(text='Гимны стран',url='localingual.com')
si2=InlineKeyboardButton(text='Все фильмо по словам',url='playphrase.me')
si3=InlineKeyboardButton(text='Котятки',url='purrli.com')
si4=InlineKeyboardButton(text='NASA и Марс',url='uahirise.org/catalog/')
si5=InlineKeyboardButton(text='Прогулка по эйфелевой башне',url='artsandculture.google.com')
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
sites.add(si1,si2,si3,si4,si5,back)

free_eat=InlineKeyboardMarkup(row_width=2)
fr1= InlineKeyboardButton(text='KFC',url=url_kfc)
fr2 = InlineKeyboardButton(text='McDonalds',url=url_mc)
fr3 = InlineKeyboardButton(text='Burgerking',url=url_bk)
fr4 = InlineKeyboardButton(text='Вкусвилл',url=url_vill)
back=InlineKeyboardButton(text='Назад 🔙',callback_data='back')
free_eat.add(fr1,fr2,fr3,fr4,back)
###

msk=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=' Лучшие 50 мест в Москве от Куда GO',url=URL_news)],
    InlineKeyboardButton(text='Метса обязательного посещения в МСК', url=URL_news)]
)

###
news=InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Переходи', url=URL_news)
    ]
])
###
connect=InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Написать', url=url_me)
    ]
])
# А теперь клавиатуры со ссылками на товары
pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url=URL_APPLES)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url=URL_PEAR)
    ]
])
