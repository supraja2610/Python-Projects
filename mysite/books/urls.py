from mysite.books import views
from mysite.views import search_form
urlpatterns = patterns('',
    # ...
    url(r'^search-form/$', views.search_form),
	url(r'^admin/', include(admin.site.urls)),
    # ...
)