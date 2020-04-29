from django.shortcuts import render
from django.http import HttpResponse


def codenation(request):

    #return HttpResponse('Olá Mundo!')
    return render(request, 'codenation.html')