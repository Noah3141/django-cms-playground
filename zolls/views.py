from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
async def zoll(req: HttpRequest) -> HttpResponse:
    return render(req, 'polls/index.html')