from django.shortcuts import render
from django.http import HttpResponse


CORRECT_KEY = 'TEST_KEY'

def home(request):
    return render(request, 'home.html')


def returnScript(request):
    if request.GET.get('key', None) == CORRECT_KEY:
        return HttpResponse('alert("Key Is correct");', content_type="application/x-javascript")
    else:
        return HttpResponse('', content_type="application/x-javascript")