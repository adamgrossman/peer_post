from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from feed.v1.urls import router
from peer_post import settings
from django.conf.urls.static import static
from feed import views


urlpatterns = [
    # Registration, Login, and Logout
    url(r'^register/$', views.register, name='register'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),    

    # Django Rest API
    url(r'^api/v1/', include(router.urls)),

    url(r'^home/', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
