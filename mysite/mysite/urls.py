from django.conf.urls.defaults import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead
from django.contrib import admin
from django.conf.urls import patterns, url

from polls import views
from books import views

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^hello/$', hello),
	url(r'^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^search-form/$', views.search_form),
	url(r'^search/$', views.search),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	#url(r'^$', views.index, name='index'),
    # url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)