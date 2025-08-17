from multiprocessing import context
from django.shortcuts import render
from httplib2 import Response
from .models import Messages
from .services import Chatbot
from django.views import View
import json
from django.http import JsonResponse

class ChatApi(View):
    def __init__(self):
        self.chatbot = Chatbot()

    def post(self, request):
        data = json.loads(request.body)
        session_id = data.get("session_id")
        user_message = data.get("message", "")
        response = self.chatbot.get_response(user_message)
        Messages.objects.create(sender="user", content=user_message, session_id=session_id)
        Messages.objects.create(sender="bot", content=response, session_id=session_id)
        return JsonResponse({"message": response})

def chat(request):
    return render(request, "chat.html")

def get_history(request):
    session_id = request.GET.get("session_id")
    if not session_id:
        return JsonResponse({"error": "Session ID not found."}, status=400)

    messages = Messages.objects.filter(session_id=session_id).order_by('timestamp')
    history = [{"sender": msg.sender, "content": msg.content, "timestamp": msg.timestamp} 
               for msg in messages]
    return JsonResponse({"history": history})