import asyncio
from utils import set_v, get_v
<<<<<<< HEAD
while True:
    print(get_v())
    set_v(get_v()+1)

=======

async def main():
    while True:
        set_v(get_v() + 1)
        await asyncio.sleep(1)  # Wait for 1 second
        print(await get_v())  # Print the updated value

asyncio.run(main())
>>>>>>> fe9ea72ddf44988ed4c2ff6ccd7cdfa7cdf3dbc1
