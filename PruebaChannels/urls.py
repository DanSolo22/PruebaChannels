from django.contrib import admin
from django.urls import path
from chat.consumers import ChatConsumer
from chat.views import chat_view

websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', chat_view, name='chat'),
]

# Agrega las URLs de WebSocket
urlpatterns += websocket_urlpatterns