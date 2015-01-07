from django.conf.urls import patterns, include, url
from django.contrib import admin
from feed.v1.urls import router
from peer_post import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    # REGISTRATION AND LOGIN
    url(r'^register/$', 'feed.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}, name='logout'),

    # DJANGO REST API
    # url(r'^api/v1/', include('feed.v1.urls', namespace='v1')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('', include('social.apps.django_app.urls', namespace='social')),


    url(r'^home/', 'feed.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
