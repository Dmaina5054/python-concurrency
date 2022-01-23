import asyncio
import time

async def main():
    task1 = asyncio.create_task(
        say_after(1,'Hey')
    )
    
    task2 = asyncio.create_task(
        say_after(3,'Hello...')
    )
    
    print(f"started at {time.strftime('%X')}")
    
    #wait for task to run
    await task1
    await task2
    
    print(f"Completed at {time.strftime('%X')}")
    
async  def say_after(delay,say):
    await asyncio.sleep(delay)
    print(say)
    
if __name__ == '__main__':
    asyncio.run(main())