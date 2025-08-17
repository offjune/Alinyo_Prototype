from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.ChatApi.as_view(), name="chat_api"),
    path("", views.chat, name="chat_page"),
    path("get_history/", views.get_history, name="get_history"),
]
