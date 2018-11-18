from django.urls import path, re_path
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.ListeArticles.as_view(), name='blog_home'),
	url(r'^categorie/(?P<id>\d+)$', views.ListeArticles.as_view(), name='blog_categorie'),
	url(r'^article/(?P<pk>\d+)-(?P<slug>\w+)', views.LireArticle.as_view(), name='blog_lire'),


    path('home', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contactN/', views.nouveau_contact, name='contactN'),
    path('contactV/', views.voir_contacts, name='contactV'),

    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2}$)', views.list_articles, name='articles_dates'), # regular expression
    re_path(r'^articles/(?P<tag>.+)', views.list_articles_by_tag, name='article_tag'), 

    path('date', views.my_date, name='date'),
    path('addition/<int:number1>/<int:number2>/', views.addition, name='addition'),
]
