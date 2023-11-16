from django.shortcuts import render
from django.http import HttpResponse
import fastf1


def index(request):
  schedule = fastf1.get_event_schedule(2023)
  countries = schedule['Country']
  locations = schedule['Location']
  event_name = schedule['EventName']
  places = zip(countries, locations, event_name)
  context = {
    "places": places
  }

  print(type(places))
  print(places)

  return render(request, "races/index.html", context)

def about(request):
  return render(request, "races/about.html")

def detail(request, event_name):
  schedule = fastf1.get_event_schedule(2023)
  event = schedule.get_event_by_name(event_name)

  print(event)

  return render(request, "races/detail.html", context = { "event": event })
