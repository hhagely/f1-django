from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, race_id):
  return HttpResponse(f"You're viewing the detail page for race {race_id}")
