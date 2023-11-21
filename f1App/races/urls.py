from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    path("<str:event_name>/", views.detail, name="detail"),
    path("<str:event_name>/<str:session>/", views.race_session, name="race_session"),
    path("<str:event_name>/<str:session_type>/<str:driver_abbr>/", views.driver_laps, name="driver_laps"),
]
