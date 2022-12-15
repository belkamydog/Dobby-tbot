import telebot

bot = telebot.TeleBot('token')
# open images
dobby = open('media/dobby.png', 'rb')
# smiles is here
prezent = "\U0001F601"


@bot.message_handler(commands=['start'])
def send_welcome(m):
    data_base = open('users_name.txt', 'w')
    print(m.chat.id)
    data_base.write(str(m.chat.id))
    data_base.close()
    bot.send_message(m.from_user.id, f'Добро пожаловать {m.chat.first_name}! Меня зовут Добби"!!!')
    bot.send_photo(m.from_user.id, dobby)
    bot.send_message(m.from_user.id, 'Мой хозяни призвал меня из сказочного мира чтобы сыграть с тобой в игру!')
    bot.send_message(m.from_user.id, 'По мере прохождения игры ты будешь получать задания! И отвечать на вопросы!')
    bot.send_message(m.from_user.id, f'Если преодолеешь все испытания тебя ждет "волшебный подарок"{prezent}!')
    bot.send_message(m.from_user.id, 'Сейчас поговорим о правилах игры:')
    bot.send_message(m.from_user.id, '- Цель игры собрать слова-подсказки!')
    bot.send_message(m.from_user.id, '- ты получаешь задание, отгадываешь слово и вводишь его сюда')
    bot.send_message(m.from_user.id, '- я проверяю')
    bot.send_message(m.from_user.id, '- если все хорошо приступаем к следующему испытанию')
    bot.send_message(m.from_user.id, '- чем больше слов у тебя будет тем легче будет откадать финальное слово')
    bot.send_message(m.from_user.id, '- Удачи тебе!')
    bot.send_message(m.from_user.id, 'Для начала игры набери заклинание "патронус" и мы начннем!')


words_list = ['вместе', 'забота', 'дерево', 'дом', 'близкие', 'люблю']

Family = 'семья'
together = 'Мудрец в нем видел мудреца,\nГлупец глупца,\nБаран барана,\nОвцу в нем видела овца,\nЧто видишь ты там, в нашей ванной'
relatives = 'Гадание на курином бульоне! 137:4  146:4  146:3  139:28  63:14 289:11  115:7'
candlelight = 'чистый****Миша3 09 широта:ель высота: колено хобби: белка вода цвет'
love = 'Это то, на чем наша с тобой основа, она ...последняя...но между тем и 280-я и 5-ое'
house = 'Сейчас я пришлю тебе несколько фотографий на это места где лежат буквы, найди все буквы и составь слово!'
care = 'Под елочкой я оставил тебе послание тебе придется постараться чтобы расшифровать его!'

question = [together, relatives, candlelight, love, house, care]
counter = 0


@bot.message_handler(content_types=['text'])
def user_answer(m):
    global counter
    if m.text == 'патронус':
        bot.send_message(m.from_user.id, question[counter])
    elif m.text in words_list:
        counter += 1
        if len(words_list) > 0:
            bot.send_message(m.from_user.id, "Ты просто умничка, переходим на новый уровень!")
            words_list.remove(m.text)
        else:
            bot.send_message(m.from_user.id, "Поздравляю ты дошла до финала!")
            bot.send_message(m.from_user.id, "Посмотри внимательно на все слова и напиши слово которое их обьединяет!")
    elif m.text == Family:
        bot.send_message(m.from_user.id, "Урааа! Победа, подарок ожидает тебя под елочкой!")
    else:
        bot.send_message(m.from_user.id, "Попробуй снова!")


bot.polling(none_stop=True, interval=0)
