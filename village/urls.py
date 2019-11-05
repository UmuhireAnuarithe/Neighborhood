from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.hood,name = 'index'),
    url(r'^new/post$', views.events, name='events'),
]