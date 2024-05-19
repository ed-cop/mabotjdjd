from telethon import *
import asyncio
import time
import ping3
from time import sleep


api_id = 22944684
api_hash = "dc7040803e2e7594dd7002ef1d7302a8"


tejas = TelegramClient("botku",api_id=api_id,api_hash=api_hash)
list_group = []
list_group_name = []
with open('chat.txt', 'r') as file:
            message = file.read()
#PERLU DIKEMBANGKAN BAGIAN INI
@tejas.on(events.NewMessage(outgoing=True ,pattern=r'.grup'))
async def hello(event):
    chat = await event.get_chat()
    dialogs = await tejas.get_dialogs()
    for dialog in dialogs:
        if dialog.is_group:
            print("Group:", dialog.name, "ID:", dialog.id)
            list_group.append(dialog.id)
            list_group_name.append(dialog.name)

#send meseg
@tejas.on(events.NewMessage(outgoing=True ,pattern=r'.tayo'))
async def hello(event):
    chat = await event.get_chat()
    while True :     
        l = 0
        for i in list_group:
            try :
                await tejas.send_message(i,message )
                print(f"send to {list_group_name[l]}")
                l += 1

            except:
                print( f"error send to {list_group_name[l]}")

            sleep(10)
        # await tejas.send_message('yelowcorp','sleep 5 menit')
        sleep(300)


@tejas.on(events.NewMessage(outgoing=True ,pattern=r'.testing'))
async def hello(event):
    chat = await event.get_chat()
    with open('chat.txt', 'r') as file:
            message = file.read()
    await tejas.send_message('Chloeehnd',message)


@tejas.on(events.NewMessage(outgoing=True ,pattern=r'.clear'))
async def hello(event):
    chat = await event.get_chat()
    list_group.clear()
    list_group_name.clear()



@tejas.on(events.NewMessage(outgoing=True ,pattern=r'.ping'))
async def ping_website(event):
    chat = await event.get_chat()
    start_time = time.time()
    result = ping3.ping('google.com')
    end_time = time.time()
    if result is not None:
        ping_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f'Ping to google.com: {result} ms')
        await tejas.send_message(chat,f'Ping to google.com: {round(result,3)} ms')

    else:
        await tejas.send_message(chat,f'gagal ping google')

tejas.start()
print("bot started")

tejas.run_until_disconnected()