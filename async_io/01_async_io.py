import asyncio

async def async_sleep_01():
    print("Starting Async Sleep Method 01")
    await asyncio.sleep(3)
    print("Execution completed")
    
async def async_sleep_02():
    print("Starting Async Sleep Method 02")
    await asyncio.sleep(3)
    print("Execution completed")

async def main():
    await asyncio.gather(async_sleep_01(), async_sleep_02())

asyncio.run(main())