from django.urls import path
from django.conf.urls import url

from .views import index, year_month_day, empty_timestamp, unix_timestamp, handler_404

urlpatterns = [
    url(r'^timestamp/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/?$', year_month_day),
    url(r'^timestamp/(?P<timestamp>\d+)/?$', unix_timestamp),
    url(r'^timestamp/.+/?$', handler_404),
    url(r'^timestamp/?$', empty_timestamp),
]