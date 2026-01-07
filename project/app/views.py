from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def json_response(req):
    data = {
        'active1' : True,
        'active2' : False,
        'active3' : None,
        
    }
    return JsonResponse(data)