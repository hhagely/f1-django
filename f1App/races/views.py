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

  return render(request, "races/index.html", context)

def about(request):
  return render(request, "races/about.html")

def detail(request, event_name):
  schedule = fastf1.get_event_schedule(2023)
  event = schedule.get_event_by_name(event_name)

  print(event)

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

  return render(request, "races/detail.html", context=context)

# def qualifying(request, event_name, session):
#   sesh = fastf1.get_session(2023, event_name, session)
#   sesh.load()

#   results = sesh.results

#   session_data = list(zip(
#     results['DriverNumber'],
#     results['Abbreviation'],
#     results['Position'],
#     results['Q1'].fillna('Eliminated'),
#     results['Q2'].fillna('Eliminated'),
#     results['Q3'].fillna('Eliminated')
#   ))

#   return render(request, "races/qualifying.html", context={"session_info": session_data})

def race_session(request, event_name, session):
  sesh = fastf1.get_session(2023, event_name, session)
  sesh.load()

  results = sesh.results

  print(results)

  session_data = list(zip(
    results['DriverNumber'],
    results['Abbreviation'],
    results['Position'],
    results['Q1'].fillna('Eliminated'),
    results['Q2'].fillna('Eliminated'),
    results['Q3'].fillna('Eliminated')
  ))

  # todo: need to modify the session data based on the session type
  # todo: ex: race session data should not have q1, q2, q3 columns on it
  match session:
    case "Practice 1":
      template = "races/practice.html"
    case "Practice 2":
      template = "races/practice.html"
    case "Practice 3":
      template = "races/practice.html"
    case "Qualifying":
      template = "races/qualifying.html"
      session_data = list(zip(
        results['DriverNumber'],
        results['Abbreviation'],
        results['Position'],
        results['Q1'].fillna('Eliminated'),
        results['Q2'].fillna('Eliminated'),
        results['Q3'].fillna('Eliminated')
      ))
    case "Sprint Shootout":
      template = "races/qualifying.html"
      session_data = list(zip(
        results['DriverNumber'],
        results['Abbreviation'],
        results['Position'],
        results['Q1'].fillna('Eliminated'),
        results['Q2'].fillna('Eliminated'),
        results['Q3'].fillna('Eliminated')
      ))
    case _:
      template = "races/race_session.html"
      session_data = list(zip(
        results['DriverNumber'],
        results['Abbreviation'],
        results['ClassifiedPosition'],
        results['GridPosition'],
        results['Status'],
        results['Points'],
      ))


  return render(request, template, context={
    "event_name": event_name,
    "session_type": session,
    "session_info": session_data,
    }
  )

def driver_laps(request, event_name, session_type, driver_abbr):
  session = fastf1.get_session(2023, event_name, session_type)

  session.load()

  driver_lap_info =  session.laps.pick_driver(driver_abbr)

  lap_info = list(zip(
    driver_lap_info['LapNumber'], # todo: convert to int
    driver_lap_info['Stint'],
    driver_lap_info['LapTime'],
    driver_lap_info['Position'],
    driver_lap_info['Deleted'],
    driver_lap_info['DeletedReason'],
  ))

  return render(request, "races/driver_laps.html", context={
    "lap_info": lap_info,
    "driver_abbr": driver_abbr,
    "event_name": event_name
  })
