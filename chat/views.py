from cgitb import text
from email.message import Message
from pyexpat.errors import messages
from urllib.request import Request
from django.shortcuts import render
from .models import Chat, Message

# Create your views here.
def index(request):
    if request.method == "POST":
        print("Received a Data " + request.POST["textmessage"])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(
            text=request.POST["textmessage"],
            author=request.user,
            chat=myChat,
            receiver=request.user,
        )
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, "chat/index.html", {"messages": chatMessages})
