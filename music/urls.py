from django.conf.urls import url

from . import views
app_name = 'music' #for namespacing url, which prevent conflicts between two url of different app with same name
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$',views.details, name='detail')
]