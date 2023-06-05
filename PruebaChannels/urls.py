from django.contrib import admin
from django.urls import path
from chat.consumers import ChatConsumer
from chat.views import register_view, login_view, select_receiver, chat_view, send_message

websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('select-receiver/', select_receiver, name='select_receiver'),
    path('chat/<int:receiver_id>/', chat_view, name='chat_view'),
    path('send_message/', send_message, name='send_message'),
]

# Agrega las URLs de WebSocket
urlpatterns += websocket_urlpatterns
