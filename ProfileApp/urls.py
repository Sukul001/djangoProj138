from django.urls import path
from ProfileApp import views
from django.contrib import admin


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
    path('updateGoods/<id>' ,views.updateGoods,name='updateGoods'),
    path('deleteGoods/<id>' ,views.deleteGoods,name='deleteGoods'),

    #ส่วนของ customer
    path('showCustomerList',views.showCustomerList,name='showCustomerList'),
    path('newCustomer',views.newCustomer,name='newCustomer'),
    path('<id>/showCustomerOne',views.showCustomerOne,name='showCustomerOne'),
    path('updateCustomer/<id>' ,views.updateCustomer,name='updateCustomer'),
    path('deleteCustomer/<id>' ,views.deleteCustomer,name='deleteCustomer'),

#-----------------ส่วนของminiproject
    #ส่วนของฺsme
    path('showSme',views.showSme,name='showSme'),
    path('addSme',views.addSme,name='addSme'),
    path('<id>/oneSme',views.oneSme,name='oneSme'),
    path('updateSme/<id>' ,views.updateSme,name='updateSme'),
    path('deleteSme/<id>' ,views.deleteSme,name='deleteSme'),
    #ส่วนของฺBorrowing
    path('showBorrowing',views.showBorrowing,name='showBorrowing'),
    path('addBorrowing',views.addBorrowing,name='addBorrowing'),
    path('<id>/oneBorrowing',views.oneBorrowing,name='oneBorrowing'),
    path('updateBorrowing/<id>' ,views.updateBorrowing,name='updateBorrowing'),
    path('deleteBorrowing/<id>' ,views.deleteBorrowing,name='deleteBorrowing'),
    #ส่วนของฺConsideration
    path('showConsideration',views.showConsideration,name='showConsideration'),
    path('addConsideration',views.addConsideration,name='addConsideration'),
    path('<id>/oneConsideration',views.oneConsideration,name='oneConsideration'),
    path('updateConsideration/<id>' ,views.updateConsideration,name='updateConsideration'),
    path('deleteConsideration/<id>' ,views.deleteConsideration,name='deleteConsideration'),
    # ส่วนของฺContract
    path('showContract', views.showContract, name='showContract'),
    path('addContract', views.addContract, name='addContract'),
    path('<id>/oneContract', views.oneContract, name='oneContract'),
    path('updateContract/<id>', views.updateContract, name='updateContract'),
    path('deleteContract/<id>', views.deleteContract, name='deleteContract'),
    # ส่วนของฺPayment
    path('showPayment', views.showPayment, name='showPayment'),
    path('addPayment', views.addPayment, name='addPayment'),
    path('<id>/onePayment', views.onePayment, name='onePayment'),
    path('updatePayment/<id>', views.updatePayment, name='updatePayment'),
    path('deletePayment/<id>', views.deletePayment, name='deletePayment'),
    # ส่วนของฺlogin
    path('userAuthen', views.userAuthen, name='userAuthen'),
    path('userLogout', views.userLogout, name='userLogout'),
    path('userChangePassword', views.userChangePassword, name='userChangePassword'),
    path('<userId>/userResetPassword', views.userResetPassword, name='userResetPassword'),
    path('customerRegister', views.customerRegistration, name='customerRegistration'),
    path('userLogout', views.userLogout, name='userLogout'),
    path('customerList', views.customerList, name='customerList'),
    path('showcustomerList', views.showcustomerList, name='showcustomerList'),
    path('customerRegister', views.customerRegistration, name='customerRegistration'),
    path('<cid>/customerUpdate', views.customerUpdate, name='customerUpdate'),
    #ส่วนของLine Notify

    #ส่วนของPDF
    path('pdfProductReport', views.pdfProductReport, name='pdfProductReport'),
    path('pdfBorrowing', views.pdfBorrowing, name='pdfBorrowing'),

    #ส่วนDashbord
    path('dashbordPie', views.dashboardPieGraph, name='dashbordPie'),


]

