from distutils.command.config import config
from operator import itemgetter
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import pyrebase

config = {
  "apiKey": "AIzaSyA8fDBldeWNHHfLCNLPH7toGLKZ7f1lB3s",
  "authDomain": "dencemaster-76f1f.firebaseapp.com",
  "databaseURL": "https://dencemaster-76f1f-default-rtdb.firebaseio.com",
  "projectId": "dencemaster-76f1f",
  "storageBucket": "dencemaster-76f1f.appspot.com",
  "messagingSenderId": "173109183753",
  "appId": "1:173109183753:web:a8fc439f39f31013aa3fd8",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()



def myFunc(e):
    return e['Score']

def say_hello(request):
    scoreboard_list = []
    some_variable = database.child('Scoreboard').get()
    items = some_variable.each()
    # print(items)
    for i in items:
        x = i.val()
        nam = x['PlayerName']
        score = x['Score']
        scoreboard_list.append({"name":nam,"score":score})
        
        # using list comprehension
        # to remove duplicated 
        # from list 
       

        # perfectScoreboard = sorted(perfectScoreboard, key=lambda d: d['score'])
        scoreboard_list = sorted(scoreboard_list, key=itemgetter('score'), reverse=True)

        

        # print(f"x{x}")
        # print(x["Score"])
        # y = x["Score"].sort()
        # print("XXX",scoreboard_list)
        
        # print(scoreboard_list)
    
    # print(some_variable.val())
    

    return render(request, 'home.html',{'name':scoreboard_list})
    