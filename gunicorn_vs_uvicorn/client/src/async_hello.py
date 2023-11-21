import asyncio
import time

async def main1():
    print('hello')
    await asyncio.sleep(1)
    print('world')


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main2():
    print(f"started at {time.strftime('%X')}")

    await say_after(2, 'hello')
    print("hoge")
    await say_after(1, 'world')

    print(f"finished at {time.strftime('%X')}. 3 sec.")

async def main3():
    task1 = asyncio.create_task(
        say_after(2, 'hello'))

    task2 = asyncio.create_task(
        say_after(1, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    print("hoge")
    await task2

    print(f"finished at {time.strftime('%X')}. 2 sec.")


async def main4():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(main1())
asyncio.run(main2())
asyncio.run(main3())
