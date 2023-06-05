from django.shortcuts import render

def chat_view(request):
    # Aquí puedes agregar la lógica necesaria para obtener los mensajes del chat
    chat_messages = []  # Reemplaza esto con la lógica para obtener los mensajes del chat desde tu modelo

    context = {
        'chat_messages': chat_messages,
    }

    return render(request, 'chat.html', context)
