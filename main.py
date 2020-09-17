import discord
import asyncio
import json
import sys
import time

print(r"""\                                                                       |
                                                                          |
           ____________
       ___/ ___________\
      / ___/           _____
     / /              (____ \
    | |  E V 1 L           \ \
    | |      1 N 5 1 D E    ) )
     \ \__           xo  __/ /           __
      \__ \_____________/ __/        ___/  \
         \_______________/       ___/       \_
                             ___/             \
                         ___/   __/            \
                     ___/   __  \__/\           \
                 ___/    __/        _\      ___/|
            ____/    __     \      /    ___/ _  (
           /        \ /_     \      ___/ _   \\ |
           |\  __    \  /       ___/ _   \\  _H_/
           | \/  \    \/    ___/ _   \\  _H_/ Y
           |`|  _/      ___/ _   \\  _H_/ Y   !   MEPH.
            \|_|\   ___/ _   \\  _H_/ Y   !   !   xo#1111
            !  | \_/ _   \\  _H_/ Y   !   !
            !  \` |  \\  _H_/ Y   !   !
                \`|  _H_/ Y   !   !
                 \|_/ Y   !   !
                      !   !
                      !
            """)

client = discord.Client()
token = input('please enter your token : ')
delp = input("please enter the phrase you want to use to clear your dms : ")
print("type !help anywhere to print what you can do terminal")
@client.event
async def on_message(message):
    if message.content.startswith("!help"):
        print(f"To clear all messages just type {delp} in the channel")
        print(f"To clear n messages just type {delp} n in the channel")
        print("Contact `xo#1111` for requests/help")
    
    elif message.content.startswith(str(delp)) and message.author == client.user and len(message.content.split()) == 1:
        counter = 0
        async for message in message.channel.history(limit=99999):
            if message.author == client.user:
                await message.delete()
                counter += 1
            print(counter)
        msg = "✅`Deleted " + str(counter) + " messages.`"
        print(msg + "\nMade by xo#1111")
        await asyncio.sleep(1)
    
    elif message.content.startswith(str(delp)) and message.author == client.user and len(message.content.split()) == 2:
        try:
            counter = 0
            todel = int(message.content.split()[1])
            async for message in message.channel.history(limit=99999):
                if message.author == client.user:
                    await message.delete()
                    counter += 1
                    if counter >= todel:
                        msg = "✅`Deleted " + str(counter) + " messages.`"
                        print(msg + "\nMade by xo#1111")
                        break
        except Exception as e:
            print(e)
            print(f"please make n a number {message.content.split()[1]} is not a number")
            

                        
client.run(token, bot=False)