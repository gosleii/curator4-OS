import telebot
from telebot import types

bot = telebot.TeleBot("6069775371:AAHB7esraAjwNZ24EaLtqmbVIg6lWTchhMI")

@bot.message_handler(commands=['start'])
def start(message):
    usern = f" {message.from_user.first_name} "
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Ссылка на видио уроки по тг ботам", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')
    markup.add(button1)
    bot.send_message(message.chat.id, f'Привет {usern} \nВведи /help - чтобы получитьсписок команду', reply_markup=markup)



@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('/game')
    bt2 = types.KeyboardButton('/film')
    bt3 = types.KeyboardButton('/books')
    markup.add(bt1,bt2,bt3)
    bot.send_message(message.chat.id, 'Это все команды на данный момент.')
    bot.send_message(message.chat.id, '/help - все команды\n/start - это начало\n/im - информация о тебе\n/im_you - информация об авторе')
    bot.send_message(message.chat.id, '/game - совет по играм \n/film - советы по фильмам/сериалам\
 \n/books - советы по книгам'.format(message.from_user), reply_markup=markup)



@bot.message_handler(commands=["im"])
def im(message):
    bot.send_message(message.chat.id, message)
    bot.send_message(message.chat.id, "нажми на /help чтобы занаво выбрать команду", parse_mode='Markdown')
@bot.message_handler(commands=["im_you"])
def im_you(message):
    bot.send_message(message.chat.id, 'Я Олег. Мне сейчас 15. Разработчит игр на Godot, геймдизайнер и художник.Учу питон, учавствуюв в разных олимпиадах.\
Любитель поиграть и пообщаться. Если хотите со мной связаься, то ищите меня в тг. @lormongord')
    bot.send_message(message.chat.id, "нажми на /help чтобы занаво выбрать команду", parse_mode='Markdown')



@bot.message_handler(commands=['game'])
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('шутер')
    btn2 = types.KeyboardButton('головоломки')
    btn3 = types.KeyboardButton('рогалик')
    btn4 = types.KeyboardButton('cимулятор')
    btn5 = types.KeyboardButton('песочница ')
    btn6 = types.KeyboardButton('домой')    
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, 'Выбирай'.format(message.from_user), reply_markup=markup) 



@bot.message_handler(commands=['film'])
def film(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('аниме')
    btn2 = types.KeyboardButton('хоррор')
    btn3 = types.KeyboardButton('дорама')
    btn6 = types.KeyboardButton('домой')    
    markup.add(btn1, btn2, btn3, btn6)
    bot.send_message(message.chat.id, 'Выбирай жанр'.format(message.from_user), reply_markup=markup) 



@bot.message_handler(commands=['books'])
def books(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Фэнтези/Фантастика')
    btn2 = types.KeyboardButton('Детективы')
    btn3 = types.KeyboardButton('мои любимые')
    btn6 = types.KeyboardButton('домой')    
    markup.add(btn1, btn2, btn3, btn6)
    bot.send_message(message.chat.id, 'Выбирай жанр'.format(message.from_user), reply_markup=markup) 



@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'шутер':
        bot.send_message(message.chat.id, 'Valarant, CS:GO, Overwatch', parse_mode='Markdown')
    if message.text == 'головоломки':
        bot.send_message(message.chat.id, 'SUPERHOT, Untitled Goose Game, Portal', parse_mode='Markdown')
    if message.text == 'рогалик':
        bot.send_message(message.chat.id, 'Noita, Dead Cells, Skul', parse_mode='Markdown')
    if message.text == 'cимулятор':
        bot.send_message(message.chat.id, 'BeamNG.drive, Viscera Cleanup Detail, Raft', parse_mode='Markdown')
    if message.text == 'песочница':
        bot.send_message(message.chat.id, "Terraria, Garry's mod, Raft", parse_mode='Markdown')


    if message.text == 'аниме':
        bot.send_message(message.chat.id, 'Onepunchman, О моём перерождении в слизь, Эхо террора', parse_mode='Markdown')
    if message.text == 'хоррор':
        bot.send_message(message.chat.id, 'Чужой, Сияние, Проклятие', parse_mode='Markdown')
    if message.text == 'дорама':
        bot.send_message(message.chat.id, 'Что не так с секретарём ким, Сказание о кумихо', parse_mode='Markdown')



    if message.text == 'Фэнтези/Фантастика':
        bot.send_message(message.chat.id, 'Странная история доктора Джекила и мистера Хайда,\
 Война миров, День триффидов, Машина времени, Евгений Замятин «Мы»', parse_mode='Markdown')

    if message.text == 'Детективы':
        bot.send_message(message.chat.id, 'Дочь времени, Лунный камень, Почерк убийцы', parse_mode='Markdown')

    if message.text == 'мои любимые':
        bot.send_message(message.chat.id, 'Евгений Замятин «Мы», Трудно быть богом, Эфект бабочки', parse_mode='Markdown')



    if message.text == 'домой':
        bot.send_message(message.chat.id, "нажми на /help чтобы занаво выбрать команду", parse_mode='Markdown')



bot.polling(none_stop=True)