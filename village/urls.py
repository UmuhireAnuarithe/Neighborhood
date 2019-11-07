from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.hood,name = 'index'),
    url(r'^new/post$', views.new_events, name='new-events'),
    url(r'^new/business$', views.new_business, name='new-business'),
    url(r'^business$', views.business, name='business'),
    url(r'^events$', views.events, name='events'),
    url(r'^new/hood$', views.hoods, name='hoods'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^new/edit_profile/$', views.edit_profile, name = 'edit_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)