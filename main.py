import asyncio
import aioconsole
import time
# Penguu Frenguu v0.1-b
# Copyright Takeout Studios 2021
print("Penguu Frenguu v0.1-b")
print()
print("Welcome to Penguu Frenguu, this is Penguu, streamer and now desktop fren!")
print("This is your command line. To get help, use 'help'.")
print()
print("Right now you can exploit the work command and get infinite money, and money doesn't do anything right now.")
print("There is also planned to be a GUI and a visual Penguu, as well as stats always on screen.")
print()
oldtime = 10
penguuHunger = 10
penguuWater = 10
penguuBills = 30
penguuMoney = 1000
async def decrease_vars():
    global penguuHunger, penguuWater, penguuBills, penguuMoney
    while True:
        await asyncio.sleep(60)
        if penguuHunger > 0:
            penguuHunger = penguuHunger - 1
        if penguuHunger == 0:
            print("Penguu has died!!!")
            time.sleep(1)
            print("YOU MONSTER!!!")
            time.sleep(9)
            break
        if penguuBills > 0:
            penguuBills = penguuBills - 1
        if penguuBills == 0:
            print("Penguu was evicted, you monster!")
            time.sleep(10)
            break
        if penguuWater > 0:
            penguuWater = penguuWater - 1
        if penguuWater == 0:
            print("Penguu has died!!!")
            time.sleep(1)
            print("YOU MONSTER!!!")
            time.sleep(9)
            break
async def loop():
    global penguuHunger
    global penguuWater
    global penguuBills
    global penguuMoney
    while True:
        userInput = await aioconsole.ainput("Penguu Frenguu Command> ")
        if userInput == "help":
            print("""
            
            Penguu Frenguu needs to be taken care of! Use some of these commands to see how they're doing!
            
            help            This message!
            stats           Show Penguu's stats!
            feed            Feed da penguu!
            hydrate         Give dem da water!
            bills           Don't get evicted!
            work            Get da money and pay da billz!
            credits         Who made this again?
            """)
        elif userInput == "stats":
            print()
            print("Hunger: ", penguuHunger)
            print("Thirst: ", penguuWater)
            print("Days until bills are due: ", penguuBills)
            print("Current money: $", penguuMoney)
            print()
        elif userInput == "feed":
            if penguuHunger <= 7:
                penguuHunger = 10
                print("Penguu has eaten.")
            elif penguuWater >= 8:
                print("They aren't hungry!")
        elif userInput == "hydrate":
            if penguuWater <= 7:
                penguuWater = 10
                print("Penguu has hydrated.")
            elif penguuWater >= 8:
                print("They aren't thirsty!")
        elif userInput == "bills":
            if penguuBills <= 5:
                penguuBills = 30
                print("Penguu paid the bills! They won't be evicted!")
                print("30 minutes until next payment")
            elif penguuBills >= 6:
                print("The bills aren't due!")
        elif userInput == "work":
            penguuMoney = penguuMoney + 10
            print("Penguu streamed and gained $10!")
            print("Penguu has: $", penguuMoney)
        elif userInput == "credits":
            print("""
            Made by Ramen, Takeout Studios
            Based on Penguu
            (C) Takeout Studios 2021
            All rights reserved.
            """)
        else:
            print("Invalid")
async def main():
    task1 = asyncio.create_task(decrease_vars())
    task2 = asyncio.create_task(loop())
    await task1
    await task2
asyncio.run(main())