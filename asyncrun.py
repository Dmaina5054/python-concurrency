import asyncio


async def main():
    print('Hello intro...')
    await asyncio.sleep(1)
    print('Completed task...')
    
if __name__ == '__main__':
    asyncio.run(main())