from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nifty-fifty/', views.nifty_fifty, name='nifty_fifty'),
    url(r'nifty-next-fifty/', views.nifty_next_fifty, name='nifty_next_fifty'),
    url(r'nifty-small-cap/', views.nifty_mid_cap, name='nifty_mid_cap'),
    url(r'nifty-mid-cap/', views.nifty_small_cap, name='nifty_small_cap'),
]