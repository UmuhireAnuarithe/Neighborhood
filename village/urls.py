from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.hood,name = 'index'),
]