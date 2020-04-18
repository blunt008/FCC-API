from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from datetime import datetime, timezone
import time as t
from time import time
# Create your views here.

# FORMULA now = datetime(2020, 12, 25).strftime('%a, %d %b %Y %H:%M:%S')

# Formula unix --> timestamp
# t = timestamp / 1000.0
# datetime.utcfromtimestamp(t)


def index(request):
    return render(
        request,
        'index.html'
    )


def year_month_day(request, year, month, day):
    try:
        date = datetime(year, month, day, tzinfo=timezone.utc)
        full_date = date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        unix_stamp = t.mktime(date.timetuple())
        return JsonResponse(
            {
                'unix': unix_stamp,
                'utc': full_date
            }
        )
    except:
        return JsonResponse({
            'error': 'Invalid Date'
        })


def unix_timestamp(request, timestamp):
    timestamp = timestamp / 1000.0
    try:
        date = datetime.utcfromtimestamp(
            timestamp).strftime('%a, %d %b %Y %H:%M:%S GMT')
        return JsonResponse(
            {
                'unix': timestamp * 1000,
                'utc': date
            }
        )
    except:
        return JsonResponse({
            'error': 'Invalid Date'
        })


def empty_timestamp(request):
    unix = int(time() * 1000)
    date = datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')
    return JsonResponse(
        {
            'unix': int(unix),
            'utc': date
        }
    )
