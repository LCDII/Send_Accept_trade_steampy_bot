from steampy_rework.client import SteamClient, Asset
from steampy_rework.utils import GameOptions, get_key_value_from_url, account_id_to_steam_id



import steam_static
import Steam_guards
from bot_reg_methods import bots_amount_checker

import requests
import json as js

import time

import random

import os

def find_item_in_inventory(item_hash_name, items):
    for item in items.values():
        market_hash_name = item['market_hash_name']
        if market_hash_name != item_hash_name:
            continue
        return {
            'market_hash_name': market_hash_name,
            'id': item['id']
        }

def find_case_in_inventory(items):
    for case_hash_name in steam_static.cases_hash_names:
        for item in items.values():
            market_hash_name = item['market_hash_name']
            if case_hash_name != market_hash_name:
                continue
            return{
                'market_hash_name': market_hash_name,
                'id': item['id']
                }       


def make_trade_1_item(waste_item, trade_link):
    game1 = GameOptions.DOTA2
    game2 = GameOptions.CS

    my_items = steam_client.get_my_inventory(game1)
    my_item_give = find_item_in_inventory(waste_item, my_items)
    my_asset = [Asset(my_item_give['id'], game1)]

    partner_account_id = get_key_value_from_url(trade_link, 'partner', True)
    partner_steam_id = account_id_to_steam_id(partner_account_id)
    partner_items = steam_client.get_partner_inventory(partner_steam_id, game2)
        
    partner_item_give = find_case_in_inventory(partner_items)
    partner_asset = [Asset(partner_item_give['id'], game2)]

    steam_client.make_offer_with_url(my_asset, partner_asset, trade_link)


def send_trades(waste_item):
    for i in range(1, len(bots_amount_checker())):
        with open(f'LPITA_K/trade_id_token_BOT{i}.json', 'r') as json_file:
            data = json.load(json_file)
        ID = data['ID']
        TOKEN = data['TOKEN']
        trade_link = f'https://steamcommunity.com/tradeoffer/new/?partner={ID}&token={TOKEN}'
        try:
            make_trade_1_item(waste_item, trade_link)

            print('Трейд  отправлен на аккаунт с ID:', ID)
            print('')
        except:
            print('Какой - то мудак менял стим гуард или нет кейса, проблема на аккаунте с ID:', ID)
            print('')
            continue 
    print('Все возможные запросы на трейд отправлены')


def create_proxie(rand_seed):
    f = open('C:/Users/Лев/Desktop/Steam_bot2/All_files/proxies.txt', 'r')
    proxie_list = []
    for line in f:
        line = line.replace('\n', '').split(':')
        proxie_list.append(line)
    f.close()

    random.shuffle(proxie_list)
    proxie = proxie_list[rand_seed]

    login = proxie[2]
    password = proxie[3]
    ip = proxie[0]

    return {"http":f"http://{login}:{password}@{ip}",
    "https:":f"https://{login}:{password}@{ip}"
    }

def accept_trade():
    for i in range(1, len(bots_amount_checker())):
        steam_guard_bot = f"Steam_guards/steam_guard_bot{i}.json"
        steam_client_bot = SteamClient(steam_guard=steam_guard_bot)

        with open(f"LPITA_K/BOT_{i}.json", 'r') as json_file:
            data_1 = json.load(json_file)

        with open(f'LPITA_K/trade_id_token_BOT{i}.json', 'r') as json_file:
            data_2 = json.load(json_file)

        username = data_1['USERNAME']
        password =data_1['PASSWORD']
        API_KEY = data_2['API_KEY']

        steam_client_bot.login(username, password)
        steam_client_bot._session.proxies.update(create_proxie(i))
        try:
            trade_link = requests.get(f'https://api.steampowered.com/IEconService/GetTradeOffers/v1/?key={API_KEY}&get_received_offers=1').json()
            trade_id = trade_link['response']['trade_offers_received'][0]['tradeofferid']
            steam_client_bot.accept_trade_offer(trade_id)
            print('Трейд принят на аккаунте с Username:', username)
            print('')
            time.sleep(steam_static.between_reg_time)
        except:
            print(f'Нет запросов на трейд на аккаунте с Username:', username)
            print('')
            time.sleep(steam_static.between_reg_time)
            continue
    print('Все возможные трейды приняты')
    print('')




steam_client = SteamClient(steam_guard="Steam_guards/steam_guard_main.json")
steam_client.login(os.getenv('USERNAME'), os.getenv('PASSWORD'))
steam_client._session.proxies.update(create_proxie(1))
print('Logged into main account')
send_trades("name")


steam_client.logout()
print('Logged out of main account')
time.sleep(steam_static.between_reg_time)

accept_trade()

