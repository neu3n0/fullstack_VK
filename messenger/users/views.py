from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from messagesChat.models import Message
from chats.models import Chat
from .models import User


@require_POST
def create_user(request):
    user = User.objects.create(username=request.POST['username'], age=request.POST['age'], mobile=request.POST['mobile'], description=request.POST['description'])
    resp = JsonResponse({
        'username': user.username,
        'age': user.age,
        'mobile': user.mobile,
        'description': user.description,
    })
    return resp
