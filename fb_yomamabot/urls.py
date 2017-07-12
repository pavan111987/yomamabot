# yomamabot/fb_yomamabot/urls.py
from django.conf.urls import include, url
from .views import YoMamaBotView
urlpatterns = [
                  url(r'^555/?$', YoMamaBotView.as_view()) 
               ]
