from django.db import models
from django.contrib.auth.models import User


class ChatUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.TextField()

    def __str__(self):
        return self.user.username


class ChatMessage(models.Model):
    sender = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.receiver}: {self.message}'
