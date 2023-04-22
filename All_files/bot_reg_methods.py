import requests
import json

import time

import random

import steam_static

def create_guard_for_bot(SteamID64: str, shared_secret: str, identity_secret: str):
    data = {
        "steamid": SteamID64,
        "shared_secret": shared_secret,
        "identity_secret": identity_secret
    }
    number = bots_amount_checker()
    with open(f"Steam_guards/steam_guard_bot{number}.json", "w") as write_file:
        json.dump(data, write_file)


def add_username_password(USERNAME: str, PASSWORD: str):
    data = {
        "USERNAME": USERNAME,
        "PASSWORD": PASSWORD
    }
    number = bots_amount_checker()
    with open(f"LPITA_K/BOT_{number}.json", "w") as write_file:
        json.dump(data, write_file)


#https://steamcommunity.com/tradeoffer/new/?partner=ID&token=TOKEN
def add_trade_id_token(link : str, API_KEY):
    partner = link.split('/')[-1]
    partner = partner.split('&')
    ID = partner[0].replace('?partner=', '')
    TOKEN = partner[-1].replace('token=', '')

    data =  {
        'ID': ID,
        'TOKEN': TOKEN,
        'API_KEY': API_KEY
    }

    number = bots_amount_checker()
    with open(f"LPITA_K/trade_id_token_BOT{number}.json", "w") as write_file:
        json.dump(data, write_file)


def bots_amount_raiser():
    file_counter = open('bot_counter.txt', 'r')

    line = file_counter.read().replace('\n', '')
    number = int(line)
    new_number = str(number + 1)
    file_counter.close()

    file_counter = open('bot_counter.txt', 'w')
    file_counter.write(new_number)
    file_counter.close()


def bots_amount_checker() -> str:
    file_counter = open('bot_counter.txt', 'r')

    line = file_counter.read().replace('\n', '')
    number = line

    file_counter.close()

    return number



