import asyncio
import websockets

async def client():
    uri = 'ws://localhost:8765'
    async with websockets.connect(uri) as websocket:
        message = input()
        for i in range(1, 6):
            print(f'{i} Сообщение пользователя: {message}')
        await websocket.send(message)

asyncio.run(client())