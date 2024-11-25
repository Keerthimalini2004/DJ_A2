from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def priya(request):
    return HttpResponse('<h1> priya also from tamilnadu salem </h1>')

def nithya(request):
    return HttpResponse('<h1><marquee> hello nithya </marquee></h1>')

def kala(request):
    return HttpResponse('''
        <h1> Name is kala <h1>
        <i> age is 21 </i><br>
        <b> fav actor rajini</b><br>
        <img src='https://tse2.mm.bing.net/th?id=OIP.rcRIynUsYMKN47w17X37nwHaNK&pid=Api&P=0&h=180'>
                        ''')