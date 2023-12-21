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

    if lances:
        mensagem_todos_lances = "\n".join([f"{lance['cliente']}: {lance['valor']}" for lance in lances])
        await cliente.send(mensagem_maior_lance + "\n" + mensagem_todos_lances)
    else:
        await cliente.send(mensagem_maior_lance)

async def lida_com_cliente(websocket, path):
    clientes.add(websocket)
    print(f"Novo cliente conectado {websocket.remote_address}. Total de clientes: {len(clientes)}")

    nome_usuario = await websocket.recv()
    nome_usuario = nome_usuario.split(":")[0]
    print(f"Cliente {nome_usuario} conectado.")

    # Envia uma mensagem para o cliente assim que a conexão é estabelecida
    mensagem_inicial = "ITEM LEILOADO SERÁ UM IPHONE 13"
    await websocket.send(mensagem_inicial)

    try:
        async for mensagem in websocket:
            # Corrige a formatação de moeda antes de converter para float
            valor_lance_str = mensagem.split(":")[-1].replace(' ', '').replace('R$', '').replace(',', '.')
            valor_lance = float(valor_lance_str)

            # Verifica se o novo lance é maior que o lance anterior
            if lances and valor_lance <= max(lance["valor"] for lance in lances):
                await websocket.send("O lance deve ser maior que o lance anterior.")
            else:
                lance = {"cliente": nome_usuario, "valor": valor_lance}
                lances.append(lance)
                print(f"Lance registrado - Cliente: {nome_usuario}, Valor: {valor_lance}")

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
    # servidor = await websockets.serve(lida_com_cliente, 'localhost', 8765)
    servidor = await websockets.serve(lida_com_cliente, '192.168.0.7', 8765)

    print("Servidor de leilão iniciado. Aguardando conexões...")

    # Aguarda até que o servidor seja encerrado
    await servidor.wait_closed()

# Inicia o loop de eventos assíncronos
asyncio.run(main())
