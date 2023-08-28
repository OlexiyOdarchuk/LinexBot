import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked, UserDeactivated
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboardsru import MenuRu, CategoriesRuIkb, FortniteRuIkb, CodesRuIkb, GiftsRuIkb, BuyCodeRuIkb, BuyGiftRuIkb, RandAccRuIkb, BuyRandomRuIkb, AdminPanelRuIkb, SendALlRuIkb, AdminMenuRu, AccRuIkb, BuyAccRuIkb, SpotifyRuIkb, BuySpotifyRuIkb, BuyNitroRuIkb, NitroRuIkb, VBucksRuIkb, BuyVbRuIkb, OtherRuIkb, YouTubeRuIkb, BuyYtRuIkb, PacksRuIkb, BuyPacksRuIkb
from keyboardsua import MenuUa, CategoriesUaIkb, FortniteUaIkb, CodesUaIkb, GiftsUaIkb, BuyCodeUaIkb, BuyGiftUaIkb, RandAccUaIkb, BuyRandomUaIkb, Language, AdminMenuUa, AdminPanelUaIkb, SendALlUaIkb, AccUaIkb, BuyAccUaIkb, SpotifyUaIkb, BuySpotifyUaIkb, NitroUaIkb, BuyNitroUaIkb, BuyVbUaIkb, VBucksUaIkb, OtherUaIkb, YouTubeUaIkb, BuyYtUaIkb, PacksUaIkb, BuyPacksUaIkb
from filters import IsPrivate, IsAdmin
from defs import get_menuRu, get_menuUa
from db import Database

API_TOKEN = '6522889029:AAGhpJOPZCJASd-xnNd4M1qubgUp1FoQoqs' 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database('base.db')

class SendAllClassUa(StatesGroup):
    text = State()

class SendAllClassRu(StatesGroup):
    text = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.user_exist(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(1433760480, f'<b>Зареєстрований новий користувач:</b> \n<a href="{message.from_user.url}">{message.from_user.full_name}</a>.')
        await bot.send_message(5440056373, f'<b>Зареєстрований новий користувач:</b> \n<a href="{message.from_user.url}">{message.from_user.full_name}</a>.')
    await message.answer(f'🇺🇦Привіт, <b>{message.from_user.full_name}</b>, обери мову, якою тобі зручніше спілкуватися:\n\n🇷🇺Привет, <b>{message.from_user.full_name}</b>, выбери язык на котором тебе комфортнее общатся:', reply_markup=Language)

@dp.callback_query_handler(lambda query: query.data.startswith('ua'))
async def Ua_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('\n🔥Ти знаходишься в найкращому магазині доповнень для Fortnite🔥\n✅Тут все за низькими цінами, і операції проходять швидко 💨\n😉Хвилюватися не варто😉\n😎Наші модератори працюють 24/7🥇\n😋Бажаю вдалих купівель!😋\n\n😊Для продовження виберіть пункт в меню😊\n\n⬇️<b>ЯКЩО ВИНИКЛИ ПИТАННЯ 🙋‍♂️⬇️\n@Moder_Linex</b>', reply_markup=get_menuUa(query.from_user.id))

@dp.callback_query_handler(lambda query: query.data.startswith('ru'))
async def Ru_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('\n🔥Ты находишься в лучшем магазине дополнений на Fortnite🔥\n✅Здесь все по низким ценам, и операции проходят быстро 💨\n😉Волноваться не стоит😉\n😎Наши модеры работают 24/7🥇\n😋Желаю удачных покупок!😋\n\n😊Для продолжения выберете пункт в меню😊\n\n⬇️<b>ЕСЛИ ВОЗНИК ВОПРОС 🙋‍♂️⬇️\n@Moder_Linex</b>', reply_markup=get_menuRu(query.from_user.id))

@dp.message_handler(lambda message: message.text == '🛍️ Категории 🛍️')
async def process_categories_button(message: types.Message):
    with open("img/Category.jpg", "rb") as photo_file:
        await bot.send_photo(message.chat.id, photo_file, caption="<b>🛍️ Все категории 🛍️</b>", reply_markup=CategoriesRuIkb)
    
@dp.callback_query_handler(lambda query: query.data.startswith('leftru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Category.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Все категории 🛍️</b>", reply_markup=CategoriesRuIkb)

@dp.message_handler(lambda message: message.text == '✔️Отзывы☑️')
async def process_categories_button(message: types.Message):
    await message.answer("<b>✅Отзывы на БОТА🤖</b>\nhttps://t.me/Linex_otzowy")

@dp.message_handler(lambda message: message.text == '📃 Гарантии 📃')
async def start(message: types.Message):
    await message.answer('<b>⚠️Покупая товар в нашем магазине, вы соглашаетесь с правилами гарантии, перечисленными ниже⚠️</b>\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n1. Все ключи, 🔑 которые предоставлены вам, действуют до 1 мая 2025 года.\n\n2. Замену ключа мы можем сделать, если вы сможете показать видео, где ключ 🔑 стал не рабочим!\n\n3. ⚠️ЕСЛИ У ВАС НЕТ ВИДЕО, МЫ НЕ МОЖЕМ ЗАМЕНИТЬ🔑\n\n4. Покупая ключи 🔑, на всякий случай снимайте все на камеру.\n\n5. Если вы купили у нас (Вб) Вы должны добавить в друзья в фортнайте НИК: jipo123423.\n\n6. После покупки вы должны модеру скинуть скрин или видео, что деньги были отправлены.\n\n7. После покупки (Вб) Вам нужно будет ждать 2 дня и потом мы сможем отправить вам подарок\n\n8. Если вы покупаете аккаунт фортнайт БЕЗ ДОСТУПА К ПОЧТЕ, то если он НЕ рабочий вам его НЕ смогут поменять.\n\n👇Если что-то пошло не так, пишите сюда👇\n@Moder_Linex\n\n⬇️Или сюда⬇️\n@Linex_Moder_keys')

@dp.message_handler(lambda message: message.text == '👨‍💻 Поддержка 👨‍💻')
async def start(message: types.Message):
    await message.answer('⬇️Вот наш Гл. модератор 👨‍💼 напишите ему, он даст вам ответ на любой ваш вопрос(Связанный с нашим телеграм ботом)⬇️\n@Moder_Linex\n\n⬇️Вот наш модератор по ключам⬇️\n@Linex_Moder_keys')

@dp.message_handler(lambda message: message.text == '🧩О нас 🧩')
async def start(message: types.Message):
    await message.answer('<b>@Linex_keys_bot - является лучшим магазином дополнений для игры Fortnite.</b> \n\n⁉️Почему же он самый лучший⁉️\n\n✅Потому что мы даём 100% гарантию что продукт будет качественный и выдан вам в течении 10 минут✅\n\n☑️Очень вежливые модераторы  объяснят, как правильно купить товар или ответят на любой ваш вопрос (Связанный с нашим телеграм ботом)‼️\n\n⬇️Наши модераторы⬇️\n\n⬇️Гл. модератор:\n@Moder_Linex\n\n⬇️Модератор по ключам:\n@Linex_Moder_keys') 

@dp.callback_query_handler(lambda query: query.data.startswith('fortniteru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Fortnite.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Категория: Fortnite</b>", reply_markup=FortniteRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('otherru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Other.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Другие приложения</b>", reply_markup=OtherRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('spotifyru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Spotify.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Категория: Spotify Premium</b>", reply_markup=SpotifyRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('indru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/SpotifyIndividual.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Spotify Individual\n💸 <b>Цена</b>: 120 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuySpotifyRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('duoru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/SpotifyDuo.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Spotify Duo\n💸 <b>Цена</b>: 140 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuySpotifyRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('familyru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/SpotifyFamily.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Spotify Family\n💸 <b>Цена</b>: 150 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuySpotifyRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('ytru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/YouTube.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Категория: YouTube Premium</b>", reply_markup=YouTubeRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('indytru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/YoutubeIndividual.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: YouTube Individual\n💸 <b>Цена</b>: 90 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyYtRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('familyytru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/YoutubeFamily.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: YouTube Family\n💸 <b>Цена</b>: 140 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyYtRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('studentytru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/YoutubeStudent.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: YouTube Student\n💸 <b>Цена</b>: 80 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyYtRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('nitroru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Nitro.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Категория: Discord Nitro</b>", reply_markup=NitroRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('nbru30'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Discord Nitro Basic 30 days\n💸 <b>Цена</b>: 110 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyNitroRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('nbru365'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Discord Nitro Basic 365 days\n💸 <b>Цена</b>: 760 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyNitroRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('nru30'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Discord Nitro 30 days\n💸 <b>Цена</b>: 210 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyNitroRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('nru365'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Discord Nitro 365 days\n💸 <b>Цена</b>: 1760 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyNitroRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('codesru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Keys.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️Ключи (коды) на Fortnite:</b>", reply_markup=CodesRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('giftsru'))
async def process_buy_gift_button(query: types.CallbackQuery):
    with open("img/Gifts.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Подарки Fortnite</b>", reply_markup=GiftsRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('accru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Accaunt.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Аккаунты Fortnite</b>", reply_markup=AccRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('randaccru'))
async def process_buy_code_button(query: types.CallbackQuery):
    #with open("img/Accaunt.jpg", "rb") as photo_file:
        await query.message.delete()
        await query.message.answer("<b>🛍️ Рандомные аккаунты Fortnite</b>", reply_markup=RandAccRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('vbucksru'))
async def process_buy_gift_button(query: types.CallbackQuery):
    with open("img/VBucks.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ V-Bucks на ваш аккаунт Fortnite</b>", reply_markup=VBucksRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('packsru'))
async def process_buy_gift_button(query: types.CallbackQuery):
    with open("img/Dodelat.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Наборы Fortnite</b>", reply_markup=PacksRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('bioluminescensru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Bioluminescens.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Набор заданий "Биолюминесценция"\n💸 <b>Цена</b>: 120 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyPacksRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('temnyogonru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Temnyogon.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Комплект "Тёмный огонь"\n💸 <b>Цена</b>: 190 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyPacksRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('orysheynicaru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Orysheynica.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Набор "Оружейница Клип"\n💸 <b>Цена</b>: 200 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyPacksRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('korolyandvoinsru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Korolyandvoins.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Набор "Короли и воины"\n💸 <b>Цена</b>: 250 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyPacksRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('otradru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Otrad.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Подписка Отряд Fortnite\n💸 <b>Цена</b>: 240 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyPacksRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_coderu_1'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/BatmanAHAHA.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Скин "Бэтмен который смеётся"\n💸 <b>Цена</b>: 260 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyCodeRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_coderu_2'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/SpiderMan.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Скин "Человек паук из эпицентра"\n💸 <b>Цена</b>: 135 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyCodeRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_coderu_3'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Harly.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Скин "Возрождённая Харли Квинн"\n💸 <b>Цена</b>: 170 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyCodeRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_coderu_4'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Kruk.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Инструмент "Крюк Женщины-Кошки"\n💸 <b>Цена</b>: 245 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyCodeRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_coderu_5'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/AdamantyKohty.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Инструмент "Адамантиевые когти"\n💸 <b>Цена</b>: 95 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyCodeRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_coderu_6'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/ObertkaStarka.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Обёртка "Разработка Старка"\n💸 <b>Цена</b>: 95 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyCodeRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_coderu_7'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/GrafytyShih.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Граффити "Ших! Ших!"\n💸 <b>Цена</b>: 95 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyCodeRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_coderu_8'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Batman.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Скин "Бэтмен из эпицентра"\n💸 <b>Цена</b>: 230 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyCodeRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_coderu_9'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Category.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Экран загрузки "Битва за эпицентр"\n💸 <b>Цена</b>: 95 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyCodeRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftru_200'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарок на 200 V-Bucks\n💸 <b>Цена</b>: 25 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyGiftRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftru_1500'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарок на 1500 V-Bucks\n💸 <b>Цена</b>: 155 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyGiftRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftru_500'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарок на 500 V-Bucks\n💸 <b>Цена</b>: 55 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyGiftRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftru_800'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарок на 800 V-Bucks\n💸 <b>Цена</b>: 80 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyGiftRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftru_1200'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарок на 1200 V-Bucks\n💸 <b>Цена</b>: 125 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyGiftRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftru_1800'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарок на 1800 V-Bucks\n💸 <b>Цена</b>: 180 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyGiftRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftru_2000'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарок на 2000 V-Bucks\n💸 <b>Цена</b>: 210 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyGiftRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftru_2500'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарок на 2500 V-Bucks\n💸 <b>Цена</b>: 260 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyGiftRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftru_3000'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарок на 3000 V-Bucks\n💸 <b>Цена</b>: 310 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyGiftRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('acc_lowru'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/acc_low.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Аккаунт 17 скинов Fortnite\n💸 <b>Цена</b>: 65 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyAccRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('rand_accru_25'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Рандом дешевый\n💸 <b>Цена</b>: 25 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyRandomRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('rand_accru_65'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Рандом средний\n💸 <b>Цена</b>: 65 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyRandomRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('rand_accru_120'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Рандом дорогой\n💸 <b>Цена</b>: 120 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyRandomRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('vbru1000'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Vb1000.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: 1 000 V-Bucks\n💸 <b>Цена</b>: 105 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyVbRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('vbru2800'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Vb2800.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: 2 800 V-Bucks\n💸 <b>Цена</b>: 230 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyVbRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('vbru5000'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Vb5000.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: 5 000 V-Bucks\n💸 <b>Цена</b>: 345 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyVbRuIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('vbru13500'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Vb13500.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: 13 500 V-Bucks\n💸 <b>Цена</b>: 770 грн\n👇 Для покупки воспользуйтесь кнопкой ниже:', reply_markup=BuyVbRuIkb)

@dp.callback_query_handler(Text(equals='buyru'))
async def buy_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('‼️Оплатите заказ на номер карты💳\n<b>5168 7520 2459 2043</b>\n\n⬇️После оплаты напишите модератору⬇️\n@Moder_Linex.')




#Зверху РОС







#Рос адмінка
@dp.message_handler(IsAdmin(), Text(equals='👤Админ-Панель'), state='*')
async def admin_panel(message: types.Message):
    await message.answer('<b>Вы в админ-панели.</b>', reply_markup=AdminPanelRuIkb)


@dp.message_handler(IsAdmin(), Text(equals='📢Создать рассылку'))
async def send_all_handler(message: types.Message, state: FSMContext):
    await message.answer('<b>🖊 Введите текст рассылки:</b>', reply_markup=SendALlRuIkb)
    await state.set_state(SendAllClassRu.text.state)

@dp.message_handler(state=SendAllClassRu.text)
async def send_all_finish(message: types.Message, state: FSMContext):
    if message.text != '🚫Отменить рассылку':
        text = message.text
        users = db.get_users()
        await message.answer('<b>♻Рассылка проводится...</b>')
        for i in users:
            try:
                await bot.send_message(i[0], text)
            except:
                pass
        await message.answer('<b>✅Рассылка завершена.</b>', reply_markup=get_menuRu(message.from_user.id))
        await state.finish()
    else:
        await message.answer('<b>✅Рассылка отменена.</b>', reply_markup=get_menuRu(message.from_user.id))
        await state.finish()

@dp.message_handler(Text(equals='⬅В главное меню↩'), state='*')
async def admin_panel_left(message: types.Message):
    await message.answer('<b>Вы в главном меню.</b>', reply_markup=get_menuRu(message.from_user.id))





#Українська Адмінка








@dp.message_handler(IsAdmin(), Text(equals='👤Адмін-Панель'), state='*')
async def admin_panel(message: types.Message):
    await message.answer('<b>Ви в адмін-панелі.</b>', reply_markup=AdminPanelUaIkb)


@dp.message_handler(IsAdmin(), Text(equals='📢Провести розсилку'))
async def send_all_handler(message: types.Message, state: FSMContext):
    await message.answer('<b>🖊 Введіть текст розсилки:</b>', reply_markup=SendALlUaIkb)
    await state.set_state(SendAllClassUa.text.state)

@dp.message_handler(state=SendAllClassUa.text)
async def send_all_finish(message: types.Message, state: FSMContext):
    if message.text != '🚫Відмінити розсилку':
        text = message.text
        users = db.get_users()
        await message.answer('<b>♻Розсилка проводиться...</b>')
        for i in users:
            try:
                await bot.send_message(i[0], text)
            except:
                pass
        await message.answer('<b>✅Розсилку завершено.</b>', reply_markup=get_menuUa(message.from_user.id))
        await state.finish()
    else:
        await message.answer('<b>✅Розсилку відмінено.</b>', reply_markup=get_menuUa(message.from_user.id))
        await state.finish()

@dp.message_handler(Text(equals='⬅В головне меню↩'), state='*')
async def admin_panel_left(message: types.Message):
    await message.answer('<b>Ви в головному меню.</b>', reply_markup=get_menuUa(message.from_user.id))







#Знизу УКР






@dp.message_handler(lambda message: message.text == '🛍️ Категорії 🛍️')
async def process_categories_button(message: types.Message):
    with open("img/Category.jpg", "rb") as photo_file:
        await bot.send_photo(message.chat.id, photo_file, caption="<b>🛍️ Всі категорії 🛍️</b>", reply_markup=CategoriesUaIkb)
    
@dp.callback_query_handler(lambda query: query.data.startswith('leftua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Category.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Всі категорії 🛍️</b>", reply_markup=CategoriesUaIkb)

@dp.message_handler(lambda message: message.text == '✔️Відгуки☑️')
async def process_categories_button(message: types.Message):
    await message.answer("<b>✅Відгуки на БОТА🤖</b>\nhttps://t.me/Linex_otzowy")

@dp.message_handler(lambda message: message.text == '📃 Гарантії 📃')
async def start(message: types.Message):
    await message.answer('<b>⚠️Купуючи товар в нашому магазині, ви погоджуєтеся з правилами гарантії, перерахованими нижче⚠️</b>\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n1. Всі ключі, 🔑 які надані вам, дійсні до 1 травня 2025 року.\n\n2. Заміну ключа ми можемо надати, якщо ви зможете показати відео, де ключ 🔑 став не дійсним!\n\n3. ⚠️ЯКЩО У ВАС НЕМАЄ ВІДЕО, МИ НЕ МОЖЕМО ЗАМІНИТИ🔑\n\n4. Купуючи ключі 🔑, на крайній випадок знімайте все на камеру.\n\n5. Якщо ви купили у нас (Вб) Ви маєте додати в друзі в фортнайт НІК: jipo123423.\n\n6. Після купівлі ви маєте модеру відправити скріншот або відео, що гроші було відпралено.\n\n7. Після купівлі (Вб) Вам потрібно буде чекати 2 дні, тоді ми зможемо відправити вам подарунок\n\n8. Якщо ви купуєте аккаунт фотнайт БЕЗ ДОСТУПА ДО ПОШТИ, то якщо він НЕ дійсний вам його НЕ зможуть замінити.\n\n👇Якщо щось пішло не так, пишіть сюди👇\n@Moder_Linex\n\n⬇️Або сюди⬇️\n@Linex_Moder_keys')

@dp.message_handler(lambda message: message.text == '👨‍💻 Підтримка 👨‍💻')
async def start(message: types.Message):
    await message.answer('⬇️Ось наш Гл. модератор 👨‍💼 напишить йому, він дасть вам відповідь на будь-яке ваше запитання(Пов\'язане з нашим телеграм ботом)⬇️\n@Moder_Linex\n\n⬇️Ось наш модератор по ключах⬇️\n@Linex_Moder_keys')

@dp.message_handler(lambda message: message.text == '🧩Про нас 🧩')
async def start(message: types.Message):
    await message.answer('<b>@Linex_keys_bot - є найкращим магазином доповнень для гри Fortnite.</b> \n\n⁉️Чому ж він найкращий⁉️\n\n✅Тому, що ми даємо 100% гарантії, що продукт буде якісний і виданий вам протягом 10 хвилин✅\n\n☑️Максимально вічливі модератори пояснять, як правильно купити товар, або дадуть відповідь на будь-яке ваше запитання (Пов\'язане з нашим телеграм ботом)‼️\n\n⬇️Наші модератори⬇️\n\n⬇️Гл. модератор:\n@Moder_Linex\n\n⬇️Модератор по ключах:\n@Linex_Moder_keys') 

@dp.callback_query_handler(lambda query: query.data.startswith('fortniteua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Fortnite.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Категорія: Fortnite</b>", reply_markup=FortniteUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('otherua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Other.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Інші застосунки</b>", reply_markup=OtherUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('spotifyua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Spotify.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Категорія: Spotify Premium</b>", reply_markup=SpotifyUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('indua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/SpotifyIndividual.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Spotify Individual\n💸 <b>Ціна</b>: 120 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuySpotifyUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('duoua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/SpotifyDuo.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Spotify Duo\n💸 <b>Ціна</b>: 140 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuySpotifyUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('familyua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/SpotifyFamily.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Spotify Family\n💸 <b>Ціна</b>: 150 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuySpotifyUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('ytua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/YouTube.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Категорія: YouTube Premium</b>", reply_markup=YouTubeUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('indytua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/YouTubeIndividual.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: YouTube Individual\n💸 <b>Ціна</b>: 90 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyYtUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('familyytua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/YouTubeFamily.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: YouTube Family\n💸 <b>Ціна</b>: 140 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyYtUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('studentytua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/YouTubeStudent.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: YouTube Student\n💸 <b>Ціна</b>: 80 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyYtUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('nitroua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Nitro.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Категорія: Discord Nitro</b>", reply_markup=NitroUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('nbua30'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Discord Nitro Basic 30 days\n💸 <b>Ціна</b>: 110 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyNitroUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('nbua365'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Discord Nitro Basic 365 days\n💸 <b>Ціна</b>: 760 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyNitroUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('nua30'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Discord Nitro 30 days\n💸 <b>Ціна</b>: 210 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyNitroUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('nua365'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Discord Nitro 365 days\n💸 <b>Ціна</b>: 1760 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyNitroUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('codesua'))
async def process_buy_code_button(query: types.CallbackQuery):
   with open("img/Keys.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️Ключі (коди) на Fortnite:</b>", reply_markup=CodesUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('giftsua'))
async def process_buy_gift_button(query: types.CallbackQuery):
    with open("img/Gifts.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Подарунки Fortnite</b>", reply_markup=GiftsUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('accua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Accaunt.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Аккаунти Fortnite</b>", reply_markup=AccUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('randaccua'))
async def process_buy_code_button(query: types.CallbackQuery):
    #with open("img/Accaunt.jpg", "rb") as photo_file:
        await query.message.delete()
        await query.message.answer("<b>🛍️ Рандомні аккаунти Fortnite</b>", reply_markup=RandAccUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('vbucksua'))
async def process_buy_gift_button(query: types.CallbackQuery):
    with open("img/VBucks.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ V-Bucks на ваш аккаунт Fortnite</b>", reply_markup=VBucksUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('packsua'))
async def process_buy_gift_button(query: types.CallbackQuery):
    with open("img/Dodelat.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption="<b>🛍️ Набори Fortnite</b>", reply_markup=PacksUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('bioluminescensua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Bioluminescens.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Набір завдань "Біолюмінесценція"\n💸 <b>Ціна</b>: 120 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyPacksUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('temnyogonua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/TemnyOgon.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Комплект "Темний вогонь"\n💸 <b>Ціна</b>: 190 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyPacksUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('orysheynicaua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Orysheynica.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Набір "Зброярниця Кліп"\n💸 <b>Ціна</b>: 200 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyPacksUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('korolyandvoinsua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/KorolyAndVoins.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Набір "Королі і воїни"\n💸 <b>Ціна</b>: 250 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyPacksUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('otradua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Otrad.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Підписка Загін Fortnite\n💸 <b>Ціна</b>: 240 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyPacksUaIkb)
        
@dp.callback_query_handler(lambda query: query.data.startswith('buy_codeua_1'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/BatmanAHAHA.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Скін "Бетмен що сміється"\n💸 <b>Ціна</b>: 260 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyCodeUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_codeua_2'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/SpiderMan.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Скін "Людина павук з епіцентру"\n💸 <b>Ціна</b>: 135 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyCodeUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_codeua_3'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Harly.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Скін "Відроджена Харлі Квін"\n💸 <b>Ціна</b>: 170 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyCodeUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_codeua_4'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Kruk.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Інструмент "Крюк Жінки-кішки"\n💸 <b>Ціна</b>: 245 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyCodeUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_codeua_5'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/AdamantyKohty.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Інструмент "Адамантеві кігті"\n💸 <b>Ціна</b>: 95 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyCodeUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_codeua_6'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/ObertkaStarka.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Обгортка "Розробка Старка"\n💸 <b>Ціна</b>: 95 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyCodeUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_codeua_7'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/GrafytyShih.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Граффити "Ших! Ших!"\n💸 <b>Ціна</b>: 95 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyCodeUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_codeua_8'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/Batman.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Скін "Бетмен з епіцентру"\n💸 <b>Ціна</b>: 230 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyCodeUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_codeua_9'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/ZeroWar.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Екран загрузки "Битва за епіцентр"\n💸 <b>Ціна</b>: 95 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyCodeUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftua_200'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарок на 200 V-Bucks\n💸 <b>Ціна</b>: 25 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyGiftUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftua_1500'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарунок на 1500 V-Bucks\n💸 <b>Ціна</b>: 155 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyGiftUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftua_500'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарунок на 500 V-Bucks\n💸 <b>Ціна</b>: 55 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyGiftUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftua_800'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарунок на 800 V-Bucks\n💸 <b>Ціна</b>: 80 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyGiftUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftua_1200'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарунок на 1200 V-Bucks\n💸 <b>Ціна</b>: 125 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyGiftUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftua_1800'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарунок на 1800 V-Bucks\n💸 <b>Ціна</b>: 180 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyGiftUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftua_2000'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарунок на 2000 V-Bucks\n💸 <b>Ціна</b>: 210 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyGiftUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftua_2500'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарунок на 2500 V-Bucks\n💸 <b>Ціна</b>: 260 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyGiftUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('buy_giftua_3000'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Подарунок на 3000 V-Bucks\n💸 <b>Ціна</b>: 310 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyGiftUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('acc_lowua'))
async def process_buy_code_button(query: types.CallbackQuery):
    with open("img/acc_low.jpg", "rb") as photo_file:
        await query.message.delete()
        uploaded_photo = await bot.send_photo(chat_id=query.message.chat.id, photo=photo_file, caption='🏷 <b>Товар</b>: Аккаунт 17 скінів Fortnite\n💸 <b>Ціна</b>: 65 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyAccUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('rand_accua_25'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Рандом дешевий\n💸 <b>Ціна</b>: 25 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyRandomUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('rand_accua_65'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Рандом середній\n💸 <b>Ціна</b>: 65 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyRandomUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('rand_accua_120'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: Рандом дорогий\n💸 <b>Ціна</b>: 120 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyRandomUaIkb)
@dp.callback_query_handler(Text(equals='buyua'))
async def buy_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('‼️Оплатіть замовлення на номер карти💳\n<b>5168 7520 2459 2043</b>\n\n⬇️Після оплати напишіть модератору⬇️\n@Moder_Linex.')

@dp.callback_query_handler(lambda query: query.data.startswith('vbua1000'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: 1 000 V-Bucks\n💸 <b>Ціна</b>: 120 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyVbUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('vbua2800'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: 2 800 V-Bucks\n💸 <b>Ціна</b>: 240 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyVbUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('vbua5000'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: 5 000 V-Bucks\n💸 <b>Ціна</b>: 350 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyVbUaIkb)

@dp.callback_query_handler(lambda query: query.data.startswith('vbua13500'))
async def process_buy_code_button(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer('🏷 <b>Товар</b>: 13 500 V-Bucks\n💸 <b>Ціна</b>: 780 грн\n👇 Для купівлі скористуйтеся кнопкою нижче:', reply_markup=BuyVbUaIkb)

@dp.message_handler()
async def mistake(message: types.Message):
    await message.answer('<b>Невідома команда!</b>\nДля повернення на початок введіть /start')

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)