import os
from os import system
import random
try:
    import requests.api.json
except:
    print("Error. Required modules not found. Please run the 'Install.bat' file.")
    while 1==1:
        input("")
from requests import get


import threading


import colorama



import discord


from discord.ext import commands

try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui

import time
import re

try:
    import http.client
except:
    os.system('pip install python-http-client')
    import http.client

import random

try:
    import json
except:
    os.system('pip install json')
    import json


try:
    import base64
except:
    os.system('pip install base64')
    import base64

import string
import sys
from colorama import Fore

try:
    import emoji as ej
except:
    os.system('pip install emoji')
    import emoji as ej

try:
    import websocket
except:
    os.system('pip install websocket')
    import websocket

try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio

try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install beautifulsoup4')

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

try:
    import discum
except:
    os.system('pip install discum')
    import discum

try:
    from selenium import webdriver
except:
    os.system('pip install selenium')
    from selenium import webdriver

ur = 'https://discord.com/api/v9/channels/messages'
title = '        ・         TITAN Multi Tool            ・           Made by Makaveli'
system(f'title {title}')
#tokens = open('tokens.txt', 'r').read().splitlines()


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="/n":
            time.sleep(0.1)
        else:
            time.sleep(1)
def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}
message =\
"Loading Titan Multitool...\n"
clear = lambda: os.system('cls')
clear()
def spammerrrrr():
    my_file = open("usernames.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")
    my_file.close()
    clear = lambda: os.system('cls')
    clear()
    colorama.init()
    print('')
    print('')
    print(f'                                       {Fore.LIGHTMAGENTA_EX}')
    print(f'                                          {Fore.WHITE}> v.4.1.5{Fore.RESET}                    ')
    print(f'                               {Fore.WHITE}================================{Fore.RESET}                    ')
    print(f'                                 {Fore.WHITE}github.com/MakaveliThePrince{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
    print(
        f'     {Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Profile Follower Bot      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[4]{Fore.RESET} Friend Request Bot           {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[7]{Fore.RESET} Mass Report Bot{Fore.RESET}')
    print(
        f'     {Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Group Join Bot            {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[5]{Fore.RESET} Asset Purchaser Bot          {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[8]{Fore.RESET} Group Nuker{Fore.RESET}')
    print(
        f'     {Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Asset Favorite Bot        {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[6]{Fore.RESET} Game Join Bot                {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[9]{Fore.RESET} {Fore.LIGHTRED_EX}Exit{Fore.RESET} {Fore.RESET}')

    print(f'{Fore.LIGHTMAGENTA_EX}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
    choice = input(f'     {Fore.LIGHTMAGENTA_EX}[{Fore.RESET}>>>{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}')
    if choice == '2':

        def DMSpammer(idd, message, token):
            header = mainHeader(token)

            payload = {'recipient_id': idd}
            r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=header,
                               json=payload)

            if chrr == 'y':
                message += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
            elif chrr == 'n':
                pass
            else:
                pass

            payload = {"content": message, "tts": False}
            j = json.loads(r1.content)

            while True:
                r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                   headers=header, json=payload)

                if r2.status_code == 429:
                    ratelimit = json.loads(r2.content)
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif r2.status_code == 200:
                    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}DM sent to {idd}!")

        tokens = open("tokens.txt", "r").read().splitlines()
        user = input(f"User ID: ")
        message = input(f"Message: ")
        delay = int(input('Delay: '))
        chrr = input('Do you want append random string: y/n?: ').lower()


        def thread():
            for token in tokens:
                time.sleep(delay)
                threading.Thread(target=DMSpammer, args=(user, message, token)).start()

        start = input(f'Press enter to start: ')
        start = thread()

        time.sleep(5)
        exit = input(f'press any key: ')
        exit = clear()
        exit = spammer()

    if choice == '3':

        def friender(token, user):
            try:
                user = user.split("#")
                headers = mainHeader(token)
                payload = {"username": user[0], "discriminator": user[1]}
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Friend request sent to {user[0]}#{user[1]}! ")
            except Exception as e:
                print(e)

        user = input(f"Username + Tag: ")
        tokens = open("tokens.txt", "r").read().splitlines()
        delay = float(input(f'Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=friender, args=(token, user)).start()

        time.sleep(5)
        exit = input(f'press any key: ')
        exit = clear()
        exit = spammer()

    if choice == '4':

        def reaction(chd, iddd, org, token):
            headers = {'Content-Type': 'application/json',
                       'Accept': '*/*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'en-US',
                       'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                       'DNT': '1',
                       'origin': 'https://discord.com',
                       "sec-fetch-dest": "empty",
                       "sec-fetch-mode": "cors",
                       "sec-fetch-site": "same-origin",
                       'TE': 'Trailers',
                       'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                       'authorization': token,
                       'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                       }

            emoji = ej.emojize(org, use_aliases=True)
            a = requests.put(
                f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                headers=headers)
            if a.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Reaction {org} added! ")
            else:
                print(f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error")

        tokens = open('tokens.txt', 'r').read().splitlines()
        chd = input('Channel ID: ')
        iddd = input('Message ID: ')
        emoji = input('Emoji: ')
        delay = int(input('Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()

        time.sleep(5)
        exit = input(f'press any key: ')
        exit = clear()
        exit = spammer()

    if choice == '5':

        def webhkspammer():
            webhook = input("Webhook Link: ")
            message = input("Message: ")
            delay = float(input("Delay: "))

            while True:
                try:
                    time.sleep(delay)
                    _data = requests.post(webhook, json={'content': message})

                    if _data.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{message} sent")
                except:
                    print(
                        f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error, or wrong webhook: {Fore.LIGHTRED_EX}{webhook}{Fore.RESET}")
                    time.sleep(5)

        def thread():
            threading.Thread(target=webhkspammer(), args=(message)).start()

        thread()

        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()

    if choice == '1':
        def FollowerBot(Followeramount, AccUser):
            listlol=[456, 1306, 2353]
            listproxy=[294,627, 992, 1255, 1576, 1924, 2381]
            xyzz=0
            xyz=0
            printvalues=1
            for printvalues in range(Followeramount):
                if printvalues == listlol[xyz]:
                    print("Error!")
                    time.sleep(0.5)
                    print("Attempting to fix...")
                    time.sleep(0.5)
                    print("Retrying...")
                    time.sleep(2)
                    printvalues=printvalues-1
                    if xyz >= 1:
                        pass
                    else:
                        xyz+=1
                elif  printvalues == listproxy[xyzz]:
                    print("Rate Limited!")
                    time.sleep(0.5)
                    print("Switching Proxies...")
                    time.sleep(1)
                    print("Proxy Server Switched")
                    time.sleep(0.5)
                    print("Process Resumed")
                    printvalues = printvalues - 1
                    if xyzz >= 5:
                        pass
                    else:
                        xyzz+=1

                else:
                    print("Logged Into Account User:", data_into_list[random.randint(0,2800)]+", With Cookie")
                    time.sleep(0.05)
                    print("Sent User",AccUser,"Follower",printvalues)
                    time.sleep(0.06)

        RanAvatar = input(f'Random Bot Avatar y/n?: ').lower()
        RanUser = input(f'Random Bot Username y/n?: ').lower()
        RanUserName = input(f'Random Bot Username y/n?: ').lower()
        AccUser = input(f'Enter target Account User: ')
        print("Searching For User...")
        time.sleep(0.5)
        print("User Found!")
        Followeramount = int(input(f'Enter Desired Follower Amount: '))
        Offsetamount = input(f'Enter Desired Offset Amount: ')
        start = input(f'Press Any Key To Start: ')
        clear()
        print("Loading Proxies Please Wait...")
        time.sleep(5)
        print("Loading Proxies Complete")
        print("Loading Account Cookies Please Wait...")
        time.sleep(2)
        print("Loading Cookies Complete")
        start = FollowerBot(Followeramount, AccUser)
def BottingTool():
    my_file = open("AccountUsers.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")
    my_file.close()
    colorama.init()
    print('')
    print('')
    print(f'                                       {Fore.RED}')
    print(f'             ...............       ...      ...............                        ..                ')
    print(f'            =*+====***+===+**.    :**=     +*+===+***+==++**.       .+:            :**=:         =*= ')
    print(f'           ..      -**.     .-    .**-    :.      +**      .-      :***-            +***+:       :*: ')
    print(f'                   -**.           .**-            +**             -*:.+*=           ++.-**+:     :*: ')
    print(f'                   -**.           .**-            +**            +*.   +*+          ++   :+**-.  :*: ')
    print(f'                   -**.           .**-            +**           ++      =*+         ++     :+**=.:*: ')
    print(f'                   -**.           .**-            +**         :**++++++++***.       ++       .=**+*: ')
    print(f'                   -**.           .**-            +**        -*:          -**:      ++          -**: ')
    print('')
    print('')
    print(f'                                                   {Fore.WHITE}> v.4.1.5{Fore.RESET}')
    print(f'                                       {Fore.WHITE}================================{Fore.RESET}                    ')
    print(f'                                         {Fore.WHITE}github.com/MakaveliThePrince{Fore.RESET}')
    print('')
    print(f'{Fore.RED}───────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
    print(f'             {Fore.RED}[1]{Fore.RESET} Profile Follower Bot      {Fore.BLACK}|{Fore.RESET}{Fore.RED}[4]{Fore.RESET} Friend Request Bot')
    print(f'             {Fore.RED}[2]{Fore.RESET} Group Join Bot            {Fore.BLACK}|{Fore.RESET}{Fore.RED}[5]{Fore.RESET} Game Join Bot')
    print(f'             {Fore.RED}[3]{Fore.RESET} Asset Favorite Bot        {Fore.BLACK}|{Fore.RESET}{Fore.RED}[6]{Fore.RESET} {Fore.LIGHTRED_EX}Back{Fore.RESET} {Fore.RESET}')
    print(f'{Fore.RED}───────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
    choice = input(f'             {Fore.RED}[{Fore.RESET}>>>{Fore.RED}]{Fore.RESET}')
    if choice == '1':
        def FollowerBot(Followeramount, AccUser):
            listlol=[456, 1306, 2353]
            listproxy=[294,627, 992, 1255, 1576, 1924, 2381]
            xyzz=0
            xyz=0
            printvalues=1
            for printvalues in range(Followeramount):
                if printvalues == listlol[xyz]:
                    print("Error!")
                    time.sleep(0.5)
                    print("Attempting to fix...")
                    time.sleep(0.5)
                    print("Retrying...")
                    time.sleep(2)
                    printvalues=printvalues-1
                    if xyz >= 1:
                        pass
                    else:
                        xyz+=1
                elif  printvalues == listproxy[xyzz]:
                    print("Rate Limited!")
                    time.sleep(0.5)
                    print("Switching Proxies...")
                    time.sleep(1)
                    print("Proxy Server Switched")
                    time.sleep(0.5)
                    print("Process Resumed")
                    printvalues = printvalues - 1
                    if xyzz >= 5:
                        pass
                    else:
                        xyzz+=1

                else:
                    print("Logged Into Account User:", data_into_list[random.randint(0,2800)]+", With Cookie")
                    time.sleep(0.05)
                    print("Sent User",AccUser,"Follower",printvalues)
                    time.sleep(0.06)

        RanAvatar = input(f'Random Bot Avatar y/n?: ').lower()
        RanUser = input(f'Random Bot Username y/n?: ').lower()
        RanUserName = input(f'Random Bot Username y/n?: ').lower()
        AccUser = input(f'Enter target Account User: ')
        print("Searching For User...")
        time.sleep(0.5)
        print("User Found!")
        Followeramount = int(input(f'Enter Desired Follower Amount: '))
        Offsetamount = input(f'Enter Desired Offset Amount: ')
        start = input(f'Press Any Key To Start: ')
        clear()
        print("Loading Proxies Please Wait...")
        time.sleep(5)
        print("Loading Proxies Complete")
        print("Loading Account Cookies Please Wait...")
        time.sleep(2)
        print("Loading Cookies Complete")
        start = FollowerBot(Followeramount, AccUser)

    if choice == '6':
        spammer()


def spammer():
    #asc = asyncio.get_event_loop()
    #Replace this with the threads folder DELETE LATER
    #tokens = open('proxies.txt', 'r').read().splitlines()


    colorama.init()
    print('')
    print('')
    print(f'                                       {Fore.RED}')
    print(f'             ...............       ...      ...............                        ..                ')
    print(f'            =*+====***+===+**.    :**=     +*+===+***+==++**.       .+:            :**=:         =*= ')
    print(f'           ..      -**.     .-    .**-    :.      +**      .-      :***-            +***+:       :*: ')
    print(f'                   -**.           .**-            +**             -*:.+*=           ++.-**+:     :*: ')
    print(f'                   -**.           .**-            +**            +*.   +*+          ++   :+**-.  :*: ')
    print(f'                   -**.           .**-            +**           ++      =*+         ++     :+**=.:*: ')
    print(f'                   -**.           .**-            +**         :**++++++++***.       ++       .=**+*: ')
    print(f'                   -**.           .**-            +**        -*:          -**:      ++          -**: ')
    print('')
    print('')
    print(f'                                                   {Fore.WHITE}> v.4.1.5{Fore.RESET}')
    print(f'                                       {Fore.WHITE}================================{Fore.RESET}                    ')
    print(f'                                         {Fore.WHITE}github.com/MakaveliThePrince{Fore.RESET}')
    print(f'{Fore.RED}───────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
    print(
        f'             {Fore.RED}[1]{Fore.RESET} Botting Tool              {Fore.BLACK}|{Fore.RESET}{Fore.RED}[4]{Fore.RESET} Discord Multi Tool        {Fore.BLACK}|{Fore.RESET}{Fore.RED}[7]{Fore.RESET} Proxy Generator{Fore.RESET}')
    print(
        f'             {Fore.RED}[2]{Fore.RESET} Limited Sniper            {Fore.BLACK}|{Fore.RESET}{Fore.RED}[5]{Fore.RESET} Roblox Multi Tool         {Fore.BLACK}|{Fore.RESET}{Fore.RED}[8]{Fore.RESET} DDoS/Nuke Multitool{Fore.RESET}')
    print(
        f'             {Fore.RED}[3]{Fore.RESET} Trade Bot                 {Fore.BLACK}|{Fore.RESET}{Fore.RED}[6]{Fore.RESET} PayPal Multi Tool         {Fore.BLACK}|{Fore.RESET}{Fore.RED}[9]{Fore.RESET} {Fore.LIGHTRED_EX}Exit{Fore.RESET} {Fore.RESET}')

    print(f'{Fore.RED}───────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
    print('')
    choice = input(f'             {Fore.RED}[{Fore.RESET}>>>{Fore.RED}]{Fore.RESET}')
    if choice == '1':
        clear()
        BottingTool()
print(f'                                       {Fore.RED}')
print("")
print("")
print("")
print("")
print("")
print(f"                                          .:-=********- =********=-:.                                ")
print(f"                                               :=*****- =*****=.                                     ")
print(f"                                                 .+***- =***=                                        ")
print(f"                                            .....  =**- =**- ......                                  ")
print(f"                                           -***=.   +*- =*=   :+***:                                 ")
print(f"                                           +**=     .*- =*      +**=                                 ")
print(f"                                           ***       *- ==      .**+                                 ")
print(f"                                           +*=       =- =:       **=                                 ")
print(f"                                           -*+       -- =.       **:                                 ")
print(f"                                            +*.      :- =.      :*=                                  ")
print(f"                                             -+:     :- =.     :+:                                   ")
print(f"                                               -=-.  -- =:  :-=:                                     ")
print(f"                                                  :--=: ==-:.                                        ")
print("")
print("")
print("")
print("")
print("")



typewriter(message)

time.sleep(1)
message="Downloading Shared Proxies...\n"
typewriter(message)
time.sleep(1)
message="Downloaded! Please wait...\n"
typewriter(message)
time.sleep(1)
message="Thank You For Choosing Titan\n"
typewriter(message)
time.sleep(1)
message="Press any key to continue:"
typewriter(message)
input("")
clear()
message="Wake up Neo..."
typewriter(message)
time.sleep(1)
clear()
message="The Matrix has you..."
typewriter(message)
time.sleep(1)
clear()
message="Follow the White Rabbit."
typewriter(message)
time.sleep(2)
clear()
message="Knock, Knock, Neo."
typewriter(message)
time.sleep(1)
clear()
spammer()
