from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
	
def hello(request):
    return HttpResponse("Hello world")


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return render(request, 'hours_ahead.html', {'hour_offset': offset,'next_time': dt})
	#HttpResponse(html)
#return render(request, 'hours_ahead.html', {'hour_offset':offset,'next_time':dt})