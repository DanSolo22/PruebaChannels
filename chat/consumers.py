from channels.generic.websocket import AsyncWebsocketConsumer
import json

from chat.models import ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Realizar la conexión
        await self.accept()

    async def disconnect(self, close_code):
        # Desconectar al cliente
        pass

    async def receive(self, text_data):
        # Procesar los mensajes recibidos
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Guardar el mensaje en la base de datos
        ChatMessage.objects.create(sender=self.scope['user'], content=message)

        # Enviar el mensaje a todos los clientes conectados
        await self.send_message(message)

    async def send_message(self, message):
        # Enviar el mensaje a todos los clientes conectados
        await self.send(text_data=json.dumps({
            'message': message,
        }))

    async def chat_message(self, event):
        # Transmitir el mensaje a los clientes conectados
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message,
        }))
