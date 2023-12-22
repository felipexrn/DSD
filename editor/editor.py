import asyncio
import websockets

# Lista para armazenar todos os clientes conectados
clients = set()

async def server(websocket, path):
    # Adiciona o novo cliente à lista
    clients.add(websocket)
    
    try:
        async for message in websocket:
            # Envie a mensagem recebida para todos os clientes conectados
            for client in clients:
                await client.send(message)
    finally:
        # Remove o cliente da lista quando desconectado
        clients.remove(websocket)

# Inicia o servidor WebSocket
start_server = websockets.serve(server, "10.25.2.30", 8765)

# Executa o loop de eventos
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
