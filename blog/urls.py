

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list),url(r'^pranav$', views.post_list),
    url(r'^post/new/$', views.post_new, name='post_new'),url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),url(r'^login/$', 'django.contrib.auth.views.login'),
url(r'^logout/$',views.logout_view),
    
url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': views.logout_view}),
    url(r'^accounts',views.post_list),
]
