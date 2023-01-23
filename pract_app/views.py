from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def details(request):
    return HttpResponse("<b>This is detail page<b>")


def course(request):
    return HttpResponse("<b>Choose your course accordingly<b>")


def about(request, aboutId):
    return HttpResponse(aboutId)


def homePage(request):
    data = {
        'title': 'Lenovo-HP',
        'bdata': 'Welcome to Brainworks',
        'clist': ['Git', 'Python', 'Django'],
        'student_details': [
            {'Name': 'Pradeep', 'Phone': 7897897890},
            {'Name': 'Mangesh', 'Phone': 8908908908}
        ],
        'numbers': [10, 20, 30, 40, 50]
    }
    return render(request, "index.html", data)


