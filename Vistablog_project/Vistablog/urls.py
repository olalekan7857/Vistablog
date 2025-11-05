from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Vistablog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('error/', views.error, name='error'),
    path('contact/', views.contact, name='contact'),
    path('post/<slug:slug>/', views.postpage, name='postpage'),
    path('category/<str:category>/', views.category, name='category'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 