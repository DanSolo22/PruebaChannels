from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from chat.forms import LoginForm, RegistrationForm
from chat.models import ChatMessage, ChatUser


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ChatUser.objects.create(user=user, username=user.username)
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'html/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('select_receiver')
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'html/login.html', context)


def select_receiver(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver')

        return redirect('chat_view', receiver_id=receiver_id)

    elif request.method == 'GET':
        users = ChatUser.objects.exclude(user=request.user)  # Obtén todos los usuarios excepto el usuario actual

        context = {
            'users': users
        }

        '''data = serializers.serialize('json', users)
        return JsonResponse(data, safe=False)'''
        return render(request, 'html/select_recipient.html', context)


def chat_view(request, receiver_id):
    # Obtener mensajes de chat entre el usuario actual y el destinatario
    user = ChatUser.objects.get(user=request.user).id
    receiver = ChatUser.objects.get(id=receiver_id).username

    messages = ChatMessage.objects.filter(
        (Q(sender=user) & Q(receiver_id=receiver_id)) |
        (Q(sender_id=receiver_id) & Q(receiver=user))
    ).order_by('timestamp')

    context = {
        'receiver_id': receiver_id,
        'receiver': receiver,
        'messages': messages,
    }

    return render(request, 'html/chat.html', context)


@login_required
def send_message(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver_id')
        message = request.POST.get('message')

        # Crea una nueva instancia de ChatMessage
        chat_message = ChatMessage.objects.create(
            sender=ChatUser.objects.get(user=request.user),
            receiver=ChatUser.objects.get(id=receiver_id),
            message=message
        )

        return redirect('chat_view', receiver_id=receiver_id)
