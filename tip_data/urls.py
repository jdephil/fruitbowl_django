from django.conf.urls import url
from tip_data import views

urlpatterns = [
    url('', views.api, name='api'),
    url('', views.index, name='index')
]
