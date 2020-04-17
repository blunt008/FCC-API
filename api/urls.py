from django.urls import path

from .views import index, year_month_day, empty_timestamp, unix_timestamp

urlpatterns = [
    path('api/timestamp/<int:year>-<int:month>-<int:day>/', year_month_day, name='timestamp'),
    path('api/timestamp/<int:timestamp>/', unix_timestamp),
    path('api/timestamp/', empty_timestamp),
    path('', index, name='index'),
]