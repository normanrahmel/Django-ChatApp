from cgitb import text
from email.message import Message
from http.client import HTTPResponse
from django.shortcuts import redirect
from pickle import TRUE
from pyexpat.errors import messages
from urllib.request import Request
from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.core import serializers


@login_required(login_url="/login/")
def index(request):
    if request.method == "POST":
        print("Received a Data " + request.POST["textmessage"])
        # print("Received a Data " + request.POST.get("textmessage"))
        myChat = Chat.objects.get(id=2)
        new_message = Message.objects.create(
            text=request.POST["textmessage"],
            author=request.user,
            chat=myChat,
            receiver=request.user,
        )
        serialized_obj = serializers.serialize(
            "json",
            [
                new_message,
            ],
        )
        # return JsonResponse(serialized_obj, safe=False)
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=2)
    return render(request, "chat/index.html", {"messages": chatMessages})


def login_view(request):
    redirect = request.GET.get("next")
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username"), password=request.POST.get("password")
        )

        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get("redirect"))
        else:
            return render(
                request,
                "auth/login.html",
                {"wrongPassword": True, "redirect": redirect},
            )
    return render(request, "auth/login.html", {"redirect": redirect})
