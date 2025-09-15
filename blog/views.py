from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot('chatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3',
    logic_adapters=['chatterbot.logic.BestMatch'],
    read_only=True)

if not os.path.exists('db.sqlite3'):
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')

def index(request):
    return render(request, 'index.html')

def getResponse(request):
    user_message = request.GET.get('Message', '').strip()
    if user_message:
        response = str(bot.get_response(user_message))
    else:
        response = "Please enter a message."
    return HttpResponse(response)



