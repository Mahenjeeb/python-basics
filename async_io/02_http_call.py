import asyncio
import aiohttp

async def call_httpBun(url):
     async with aiohttp.ClientSession() as session:
         async with session.get(url) as response:
             print(f"Fetched {url} with status {response.status}")
async def main():
    urls = ["https://httpbin.org/delay/3"]*3
    tasks = [call_httpBun(url) for url in urls]
    await asyncio.gather(*tasks)
    
asyncio.run(main())