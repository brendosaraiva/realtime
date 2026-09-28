# Consumer -> Faz o elo de ligação entre o navegador e a aplicação, para ativar a comunicação em realtime
# Consumers -> Existem mais de um, que vão desde a conexão/desconexão ao processamento das informações
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):

    # async -> executa o método em modo assincrono. Assincrona (comunicação em tempo real), todas funções e comando que
    # for usar, entrada o saída, tem que ter o await.

    # await -> significa espere, que nada mais é: esperar algo ser executado, antes de passar para o próximo.
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["nome_sala"]  # Recuperando nome da sala
        self.room_group_name = f"chat_{self.room_name}"  # Retorna o nome da sala

        # Entrar na sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.room_name
        )

        await self.accept()

    async def disconnect(self, code):  # code -> Gera um código de saída (para avisos)
        # Sai da sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Recebe mensagem do WebSocket
    async def receive(self, text_data):  # text_data -> Irá trazer os dados recebidos
        text_data_json = json.loads(text_data)  # Transforma em json
        mensagem = text_data_json["mensagem"]  # Recupera as mensagens transformadas em json

        # Envia a mensagem para a sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": mensagem  # Exibe a mensagem
            }
        )

    # Recebe a mensagem da Sala
    async def chat_message(self, event):  # event -> Interações (click/enter)
        mensagem = event["message"]  # Recupera a mensagem

        # Envia a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            "mensagem": mensagem
        }))
