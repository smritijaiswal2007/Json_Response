from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def json_response(req):
    # data = {
    #     'active1' : True,
    #     'active2' : False,
    #     'active3' : None,   
    # }
    data = 30
    # data = True (only set and frozen set datatype cannot be send in json )
    # data = None
    # data = [ 10,20,20,40,] list 
    # data = [ 10,20,20,40,'smriti'] list with string value
    # data = (10,20,20,40,'smriti') tupple  
    # //important = json data bhejte time chahe list me bhejo ya tupple mai output hmesha list format mai aayega
    return JsonResponse(data,safe=False)