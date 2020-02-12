
import websocket

import asyncio, ssl
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.open_connection('10.87.0.34', 11443, ssl=ssl.SSLContext()))
print("the end..")


async def test_conn(host, port):
    _, writer = await asyncio.open_connection(host, port, ssl=ssl.SSLContext())

    writer.write(b'ping\n')
    print("the end..")

asyncio.get_event_loop().run_until_complete(test_conn('10.87.0.34', 11443))