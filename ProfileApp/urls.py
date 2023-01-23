from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('home', views.home, name='home'),
    path('base', views.base, name='base'),
    path('story', views.story, name='story'),
    path('salecamera', views.salecamera, name='salecamera'),
    path('canon', views.canon, name='canon'),
    path('sony', views.sony, name='sony'),
    path('nikon', views.nikon, name='nikon'),
    path('camera', views.camera, name='camera'),
    path('copyname', views.copyname, name='copyname'),
    path('storystudy', views.storystudy, name='storystudy'),
    path('hpy', views.hpy, name='hpy'),
    path('showMyData',views.showMyData, name='showMyData'),
    path('showMydatas',views.showMydatas, name='showMydatas'),

]
