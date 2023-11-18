from django.shortcuts import render
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

  context = {
    "event_name": event['OfficialEventName'],
    "session_list": [
      event['Session1'],
      event['Session2'],
      event['Session3'],
      event['Session4'],
      event['Session5'],
    ]
  }


  print(event)

  return render(request, "races/detail.html", context=context)

def race_session(request, event_name, session):
  sesh = fastf1.get_session(2023, event_name, session)
  sesh.load()

  results = sesh.results

  print(results['q2'])

  session_data = list(zip(
    results['DriverNumber'],
    results['Abbreviation'],
    results['Position'],
    results['Q1'],
    # results['Q2'],
    # results['Q3']
  ))

  print(sesh.results)

  return render(request, "races/race_session.html", context={"session_info": session_data})

# def load_drivers(request, event_name):
#   return render(request, "races/load_drivers.html")
