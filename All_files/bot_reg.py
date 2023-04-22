from bot_reg_methods import create_guard_for_bot, add_trade_id_token, add_username_password

while True:
    username = input('Введите логин:')
    print('')
    password = input('Введите пароль:')
    print('')

    print('Перейдите по ссылке: https://steamcommunity.com/dev/apikey и скопируйте API_KEY')
    api_key = input('Введите API ключ:')
    print('')

    print('Перейдите по это ссылке: https://steamcommunity.com/profiles/76561198842369121/tradeoffers/privacy \nи скопируйте трейд-ссылку на ваш аккаунт')
    trade_link = input('Трейд-ссылка:')
    print('')

    print('Узнайти SteamID64 своего аккаунта. Далее в SDA в папке maFiles Найдите файл с этим ID в названии и скопируйте оттуда:\nshared_secret и identity_secret')
    SteamID64 = input('SteamID64:')
    shared_secret = input('shared_secret:')
    identity_secret = input('identity_secret:')
    print('')

    create_guard_for_bot(SteamID64, shared_secret, identity_secret)
    add_username_password(username, password)
    add_trade_id_token(trade_link, api_key)
    

    bots_amount_raiser()

    flag = input('Добавать еще один аккаунт?\n Y - Да, N - Нет\n')
    if flag.lower() == 'n':
        print('Осталось запустить Sbot_run.bat')
        break
    print('')