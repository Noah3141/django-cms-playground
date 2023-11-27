from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
async def apple(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    return render(request, "index.html")

