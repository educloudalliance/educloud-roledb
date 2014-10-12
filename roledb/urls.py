from django.conf.urls import patterns, include, url
from django.contrib import admin
from roledb.views import UserGetView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'roledb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/1/user$', UserGetView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
