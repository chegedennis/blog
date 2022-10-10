from django.urls import path


from . import views

urlpatterns = [
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
    path('cookies-policy', views.cookies_policy, name='cookies_policy'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('contact', views.contact, name='contact'),
]