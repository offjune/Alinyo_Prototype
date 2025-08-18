import json
import uuid
import markdown
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.html import linebreaks
from .models import Messages
from .services import Chatbot
from .prompts import START_QUESTIONS

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
    context = {
        'uuid': str(uuid.uuid4()),
        'start_questions': linebreaks(markdown.markdown(START_QUESTIONS))
    }
    return render(request, "chat.html", context)

def get_history(request):
    session_id = request.GET.get("session_id")
    if not session_id:
        return JsonResponse({"error": "Session ID not found."}, status=400)

    messages = Messages.objects.filter(session_id=session_id).order_by('timestamp')
    history = [{"sender": msg.sender, "content": msg.content, "timestamp": msg.timestamp} 
               for msg in messages]
    return JsonResponse({"history": history})