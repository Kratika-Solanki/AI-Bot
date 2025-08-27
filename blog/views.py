from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

bot=ChatBot('chatbot', read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])


# list_to_train=[
#     "Hi",  #question
#     "Yes, how may I help you?",  #answer
#     "Are you gay?",
#     "I am just a good and healthy machine..",
#     "How are you?",
#     "I doing great hope same for you..",
#     "What is your name?",
#     "My name is Tokyo *_* ",
# ]

Trainer=ChatterBotCorpusTrainer(bot)
# List_trainer=ListTrainer(bot)
# List_trainer.train(list_to_train)

Trainer.train('chatterbot.corpus.english')

def index(request):
    return render(request, 'index.html')

def getResponse(request):
    Message=request.GET.get('Message')
    chatResponse=str(bot.get_response(Message))
    return HttpResponse(chatResponse)

# Create your views here.   => 23