from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Hi this is my first app')

def post_detail(request,post_id):
    return HttpResponse(f'The asked post id is(post_id')
