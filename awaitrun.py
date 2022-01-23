import asyncio
import time

async def say_after(delay, tosay):
    await asyncio.sleep(delay)
    print(tosay)
    
async def main():
    print(f"started at {time.strftime('%X')}")
    
    await say_after(1,'Hey')
    await say_after(3,'Hello...')
    
    print(f"finished at {time.strftime('%X')}")
if __name__ == '__main__':
    asyncio.run(main(), debug=True)