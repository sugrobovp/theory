import asyncio


async def main1():
    await asyncio.sleep(5)
    print('main1')


async def main2():
    print('main2')


async def main():
    task1 = asyncio.create_task(main1())
    task2 = asyncio.create_task(main2())

    await task1
    await task2


asyncio.run(main())
