from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('article/<str:slug>', views.detail_article, name='detail'),
    path('cat/', views.categ, name='cat'),
    path('cat/<str:slug>', views.cat_detail, name='cat_detail'),
    #path('create/', BlogPostCreate.as_view(), name="create")

]