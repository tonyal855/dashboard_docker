from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^start/$', views.start, name='start'),
    url(r'^stop/$', views.stop, name='stop'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^get_images/$', views.get_images, name='get_images'),

]