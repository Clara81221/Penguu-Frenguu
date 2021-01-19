import asyncio
import aioconsole

var = 1000

async def decrease_vars():
    global var
    while True:
        await asyncio.sleep(60)
        var = var - 1

async def loop():
    while True:
        userInput = await aioconsole.ainput('> ')
        if userInput == "1":
            print("One")
        elif userInput == "2":
            print("two")
        elif userInput == "quit":
            break
        elif userInput == "printtime":
            print(var)

async def main():
    task1 = asyncio.create_task(decrease_vars())
    task2 = asyncio.create_task(loop())
    await task2

asyncio.run(main())