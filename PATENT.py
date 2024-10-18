import asyncio


async def async_join(process, timeout=0):
    for i in range(100):
        await asyncio.sleep(timeout / 100)

        if not process.is_alive():
            break

    if timeout == 0:
        await async_join(process)
