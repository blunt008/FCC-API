from django.urls import path

from .views import index, year_month_day, empty_timestamp, unix_timestamp, handler404

urlpatterns = [
    path('api/timestamp/<int:year>-<int:month>-<int:day>', year_month_day, name='timestamp'),
    path('api/timestamp/<int:timestamp>', unix_timestamp),
    path('api/timestamp/', handler404),
    path('api/timestamp', empty_timestamp),
    path('', index, name='index'),
]