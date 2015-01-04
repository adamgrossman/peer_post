from django.conf.urls import patterns, include, url
from django.contrib import admin
from feed.v1.urls import router


urlpatterns = patterns('',
    # django rest framework
    # url(r'^api/v1/', include('feed.v1.urls', namespace='v1')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)
