from django.conf.urls import patterns, include, url

from yushen import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yushen_django_1_0.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^yushen/', include('yushen.urls', namespace = 'yushen')),
    url(r'^admin/', include(admin.site.urls)),
)
