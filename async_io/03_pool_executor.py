import asyncio, time
from concurrent.futures import ThreadPoolExecutor
# Without Executor
# async def heavy_Math():
#     start = time.time()
#     print(f"Starting Heavy Math...")
#     result = 0
#     for i in range(100000000):
#         result += i * i
#     print(f"Total Result {result}")
#     end = time.time()
#     print(f"Total Time Taken {end - start:.2f} seconds") # 7.02 seconds
# async def main():
#     await heavy_Math()

# Using ThreadPoolExecutor
def heavy_math_worker():
    start = time.time()
    print(f"Starting Heavy Math...")
    result = 0
    for i in range(100000000):
        result += i * i
    print(f"Total Result {result}")
    end = time.time()
    print(f"Total Time Taken {end - start:.2f} seconds")
    
async def heavy_math():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,heavy_math_worker)
    print("Heavy Workers Done")
    return result

async def main():
    print("Hello")
    result = await heavy_math()
    print(result)
    
asyncio.run(main())