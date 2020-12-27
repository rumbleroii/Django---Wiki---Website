from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<site_name>/", views.site_name, name = '<site_name>'),
    path("create_page/" , views.create_page, name='create_page'),
    path("random_page/", views.random_page, name='random_page'),
    path("wiki/<site_name>/edit", views.edit_page, name = 'edit_page'),
    path("search/", views.search, name = 'search')

 ]
