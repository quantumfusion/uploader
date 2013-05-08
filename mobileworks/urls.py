from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from mobileworks.views import FileUpload
from mobileworks.views import Success

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mobileworks.views.home', name='home'),
    # url(r'^mobileworks/', include('mobileworks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', csrf_exempt(FileUpload.as_view()), name='upload'),
    url(r'^success/$', csrf_exempt(Success.as_view())),
)

urlpatterns += staticfiles_urlpatterns()
