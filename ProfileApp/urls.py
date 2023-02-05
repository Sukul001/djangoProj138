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

    # path('showourproduct',views.showourproduct, name = "showourproduct"),
    # path('newProduct',views.newProduct, name = 'formProductNomal'),
    # path('frmProduct',views.frmProduct, name='frmproduct'),
    # คนละส่วน
    path('listProduct',views.listProduct, name='outputProduct'),
    path('newProduct',views.newProduct,name='inputProduct'),
    path('inputProduct',views.inputProduct,name='listProduct'),
    # คนละส่วน
    # path('retrieveallproduct',views.productRetrieveall,name='retrieveallproduct'),
    # path('createproduct',views.createProduct,name='createproduct'),
    # path('<id>/retrieveoneproduct',views.productRetieveOne,name='retrieveoneproduct'),
    # คนละส่วน good
    path('showGoodsList',views.showGoodsList,name='showGoodsList'),
    path('newGoods',views.newGoods,name='newGoods'),
    path('<id>/showGoodsOne',views.showGoodsOne,name='showGoodsOne'),

    #ส่วนของ customer
    path('showCustomerList',views.showCustomerList,name='showCustomerList'),
    path('newCustomer',views.newCustomer,name='newCustomer'),
    path('<id>/showCustomerOne',views.showCustomerOne,name='showCustomerOne'),

]
