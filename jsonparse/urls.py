from django.conf.urls import url
from . import views

app_name = 'task'
urlpatterns = [
    url(r'^$', views.data_processing),
    url(r'^(?P<group_id>\d+)/$', views.data_container),

]
