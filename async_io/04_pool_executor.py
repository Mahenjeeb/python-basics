from concurrent.futures import ThreadPoolExecutor
import asyncio, time

async def pool_execute():
    # This will get us running event loop and creates a pool of workers
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        # This run in excutor assign the task to background threads
        result = await loop.run_in_executor(pool, heavy_math)
    print("Pool Executor compltes the work")
    return result

def heavy_math():
    count = 0
    for i in range(10 ** 8):
        count += i
    return count

async def main():
    start = time.time()
    res = await pool_execute()
    end = time.time()
    print(f"{res} in {end - start:.2f} seconds")

asyncio.run(main())