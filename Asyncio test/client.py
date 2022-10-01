import asyncio
import socket
import threading
import time

async def tcp_echo_client(message):
    HOST, PORT = '127.0.0.1', 28015
    reader, writer = await asyncio.open_connection(
        HOST, PORT)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    
def start_async():
    loop = asyncio.new_event_loop()
    threading.Thread(target=loop.run_forever).start()
    return loop

_loop = start_async()

# Submits awaitable to the event loop, but *doesn't* wait for it to
# complete. Returns a concurrent.futures.Future which *may* be used to
# wait for and retrieve the result (or exception, if one was raised)
def submit_async(awaitable):
    return asyncio.run_coroutine_threadsafe(awaitable, _loop)

submit_async('sex')
print("I luv u <3")
def stop_async():
    _loop.call_soon_threadsafe(_loop.stop)