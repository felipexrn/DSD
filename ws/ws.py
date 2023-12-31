import asyncio
import websockets

clientes = set()
lances = []

async def notificar_lances(cliente, nome_usuario):
    if lances:
        maior_lance = max(lances, key=lambda x: x["valor"])
        mensagem_maior_lance = f"{maior_lance['cliente']} fez o maior lance no momento: {maior_lance['valor']}"
    else:
        mensagem_maior_lance = f"{nome_usuario}: Nenhum lance até agora."

    #await cliente.send(mensagem_maior_lance)

    if lances:
        mensagem_todos_lances = "\n".join([f"{lance['cliente']}: {lance['valor']}" for lance in lances])
        await cliente.send(mensagem_maior_lance + "\n" + mensagem_todos_lances)

async def lida_com_cliente(websocket, path):
    # Adiciona o cliente à lista de clientes
    clientes.add(websocket)
    print(f"Novo cliente conectado {websocket.remote_address}. Total de clientes: {len(clientes)}")

    # Recebe o nome do usuário
    nome_usuario = await websocket.recv()
    nome_usuario = nome_usuario.split(":")[0]
    print(f"Cliente {nome_usuario} conectado.")

    try:
        async for mensagem in websocket:
            # Processa o lance recebido do cliente
            valor_lance = float(mensagem.split(":")[-1])
            lance = {"cliente": nome_usuario, "valor": valor_lance}
            lances.append(lance)
            print("lance registrado")

            # Notifica todos os clientes sobre o novo lance
            for cliente in clientes:
                await notificar_lances(cliente, nome_usuario)

    except websockets.ConnectionClosed:
        pass

    finally:
        # Remove o cliente da lista quando a conexão é fechada
        clientes.remove(websocket)
        print(f"Cliente {nome_usuario} desconectado. Total de clientes: {len(clientes)}")

async def main():
    # Inicia o servidor WebSocket
    servidor = await websockets.serve(lida_com_cliente, 'localhost', 8765)

    print("Servidor de leilão iniciado. Aguardando conexões...")

    # Aguarda até que o servidor seja encerrado
    await servidor.wait_closed()

# Inicia o loop de eventos assíncronos
asyncio.run(main())
