from django.urls import path

from . import views

app_name = 'spidermanstopwatch'
urlpatterns = [
    # ex: /
    path('', views.StopWatchView.as_view(), name='stopwatch'),
]