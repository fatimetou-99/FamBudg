from django.urls import path ,re_path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

    
urlpatterns= [
    re_path(r'^salary$', views.index , name='salary.index'),
    re_path(r'^salary/create$', views.create, name='salary.create'),
    re_path(r'^salary/edit/(?P<id>\d+)$', views.edit, name='salary.edit'),
    re_path(r'^salary/edit/update/(?P<id>\d+)$', views.update, name='salary.update'),
    re_path(r'^salary/delete/(?P<id>\d+)$', views.delete, name='salary.delete'),
    re_path(r'^category$', views.index_categ , name='category.index'),
    re_path(r'^category/create$', views.create_categ, name='category.create'),
    re_path(r'^category/edit/(?P<id>\d+)$', views.edit_categ, name='category.edit'),
    re_path(r'^category/edit/update/(?P<id>\d+)$', views.update_categ, name='category.update'),
    re_path(r'^category/delete/(?P<id>\d+)$', views.delete_categ, name='category.delete'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    
    

]