from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def hello_world(request):
    """
    A simple API endpoint that returns a JSON response with a greeting.
    """
    data = {
        'message': 'Hello, world!'
    }
    return JsonResponse(data)
