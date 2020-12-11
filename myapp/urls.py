from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('codes/', views.codes, name = 'codes'),
    path('snakegame/', views.snakegame, name = 'snakegame'),
    path('wtrgn/', views.wtrgn, name = 'watergun'),
    path('calc/', views.calc, name = 'calculator'),
    path('contact/', views.contact, name = 'contactus'),

]