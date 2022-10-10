from django.urls import path

from . import views


urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>', views.article, name='article'),
    path('<slug:slug>', views.category, name='category'),
]