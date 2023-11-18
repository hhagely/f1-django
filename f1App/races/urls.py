from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    # path("/races/", views.race_schedule, name="race_schedule"),
    path("<str:event_name>/", views.detail, name="detail"),
    path("<str:event_name>/<str:session>/", views.race_session, name="race_session")
]
