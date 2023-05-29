import asyncio
from utils import set_v, get_v

async def main():
    while True:
        set_v(get_v() + 1)
        await asyncio.sleep(1)  # Wait for 1 second
        print(await get_v())  # Print the updated value

asyncio.run(main())