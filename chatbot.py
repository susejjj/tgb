import telebot

leg = telebot.TeleBot('6345516386:AAEYV63mihplEnQLlOndflegNvAQtzCJVGw')


@leg.message_handler(commands=['start'])
def func(message):
    leg.send_message(message.chat.id, f'доброго времени суток, {message.from_user.first_name}! как делишки?\nитак, я знаю всякие команды, например, /com1 и /com2\nps: не забудь /but и /end')


@leg.message_handler(commands=['but'])
def func(message):
    leg.send_message(message.chat.id, 'сейчас будет прикольчик🦆')
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    but1 = telebot.types.InlineKeyboardButton('Первая', callback_data='first')
    but2 = telebot.types.InlineKeyboardButton('Вторая', callback_data='second')
    markup.add(but1, but2)

    leg.send_message(message.chat.id, 'выбери кнопку, пж:', reply_markup=markup)


@leg.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'first':
            leg.send_message(call.message.chat.id, 'ф-ф-функционал бота еще не расширен. когда-нибудь потом')
        if call.data == 'second':
            leg.send_message(call.message.chat.id, 'Можешь попрощаться, /bye')


@leg.message_handler(commands=['com1', 'command1'])
def func(message):
    leg.send_message(message.chat.id, 'здесь пусто, броу 😢')


@leg.message_handler(commands=['com2', 'command2'])
def func(message):
    leg.send_message(message.chat.id, '*здесь* тоже😭', parse_mode='MarkdownV2')
    leg.send_message(message.chat.id, 'хахахахах, я шучу\n[физику любить надо, это база🧠](https://www.youtube.com/watch?v=R15JBUgkVqQ)', parse_mode='MarkdownV2')


@leg.message_handler(commands=['hohoho', 'susej', 'furry'])
def func(message):
    leg.send_message(message.chat.id, 'ого, да *ты* хитрый\n_Откуда команду взял?🫣🫣🫣_\n*фуррифуррифурри*', parse_mode='MarkdownV2')


@leg.message_handler(commands=['end'])
def func(message):
    leg.send_message(message.chat.id, f'спасибо за уделенное время, но не могу же я оставить тебя без сюрприза. ведь так?\nа вот и он 🍒{message.from_user.id}🍒\nтеперь я знаю о тебе всеее😈')
    leg.send_message(message.chat.id, 'ладно, не смею задерживать🫚\nесли хочешь попрощаться, пиши /bye')


@leg.message_handler(commands=['bye'])
def func(message):
    leg.send_message(message.chat.id,'покааа🎉')
    leg.send_message(message.chat.id, 'буду ждать в другой раз💋\nя ведь еще и анонимный бот, поэтому пиши что хочешь: тебя никто не рассекретит 😏')


@leg.message_handler()
def func(message):
    leg.send_message(5053913148, f'{message.from_user.username} написал: {message.text}')





leg.infinity_polling()