from django.urls import path
from . import views
# from .views import blog_detail
from . import views as as_view


urlpatterns = [
    path('', views.home,name='home'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about,name='about'),
    path('blog_list/', views.blog_list,name='blog_list'),
    path('blog_detail/<int:pk>/',views.blog_detail, name='blog_detail'),


]
