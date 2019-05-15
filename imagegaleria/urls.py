from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name ='welcome'),
    url(r'^search/', views.search_category, name='search_results'),
]