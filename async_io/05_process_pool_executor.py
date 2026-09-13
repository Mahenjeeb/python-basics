from concurrent.futures import ProcessPoolExecutor
import asyncio

def heavy_operation():
    count = 0
    for i in range(10 ** 8):
        count += i
    return count

async def process_pool():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, heavy_operation)
    print(f"Process Completed {result}")

async def main():
    await process_pool()

if __name__ == "__main__":
    asyncio.run(main())