from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('', views.create, name='create'),
    url(r'^$', views.URLCreate.as_view(), name='create'),
    url(r'^edition/(?P<code>\w{7}$)', views.URLUpdate.as_view(), name='url_update'),
    path('list', views.show_all, name='show_all'),
    re_path(r'^(?P<code>\w{7})', views.visit, name='visit'),
    ]