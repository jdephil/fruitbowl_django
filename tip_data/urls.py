from django.conf.urls import url
from tip_data import views

urlpatterns = [
    url('api/tips/', views.TipListCreate.as_view()),
    # url('api/favorites/', views.)
    # url('', views.api, name='api'),
    # url('', views.index, name='index')
]
