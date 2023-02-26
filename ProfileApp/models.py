
from django.db import models
import datetime

class Product:
    def __init__(self,id,name,type,color,brand,price):
        self.id = id
        self.name = name
        self.type = type
        self.color = color
        self.brand = brand
        self.price = price
        self.Vat()
        self.Discount()
        self.Total()

    def Vat(self):
        self.Vat = self.price * 0.07

    def Discount(self):
        if self.price > 15000 and self.price < 19999:
            self.Discount = self.price * 0.1
        elif self.price > 20000 and self.price <34999:
            self.Discount = self.price * 0.05
        elif self.price > 35000:
            self.Discount = self.price * 0.03
        else:
            self.Discount = 0

    def Total(self):
        self.Total = self.price + self.Vat - self.Discount

    def __str__(self):
        return "ID: {},Name: {},type: {},color: {},Brand: {},Price: {},Vat: {},Discount: {},Total: {}".format(self.id,self.name,self.type,self.color,self.brand,self.price,self.Vat,self.Discount,self.Total)


# ล่าสุด
# class Catagory(models.Model):
#     name = models.CharField(max_length=50,default="")
#     desc = models.CharField(max_length=200,default="")
#
#     def __str__(self):
#         return str(self.id) + " : " +self.name + " : " +self.desc
# class ProductM(models.Model):
#     pid = models.CharField(max_length=13 , primary_key=True , default="")
#     name = models.CharField(max_length=50,default="")
#     brand = models.CharField(max_length=30,default="")
#     price = models.FloatField(default=0.00)
#     net = models.IntegerField(default=0)
#     catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, default=None)
#     def __str__(self):
#         return self.pid + ":" + self.name + ":" + self.brand + " : " + str(self.price) + " : " + str(self.net) + " : " + self.catagory.name
#
# class Employee(models.Model):
#     eid = models.CharField(max_length=5,default='')
#     name = models.CharField(max_length=35,default='')
#     surname = models.CharField(max_length=35,default='')
#     address = models.CharField(max_length=200,default='')
#     gender = models.BooleanField(default=True)
#     birthdate = models.DateTimeField(default=datetime.date.today())
#     salary = models.FloatField(default=0.00)

import  datetime
class GoodsCategory(models.Model):
    gc_name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=200,default="")
    def __str__(self):
        return str(self.id) + " : " +self.gc_name + " : " +self.desc

class Goods(models.Model):
    gid = models.CharField(max_length=13, primary_key=True, default="")
    name = models.CharField(max_length=50,default="")
    brand = models.CharField(max_length=30,default="")
    mode = models.CharField(max_length=30,default="")
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    property = models.CharField(max_length=30,default="")
    goodscategory = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.gid + ":" + self.name + ":" + self.brand + " : " + self.mode + " : " + str(self.price) + " : " + str(self.net) + " : " + self.property + " : " + self.goodscategory.gc_name

class Customer(models.Model):
    cid = models.CharField(max_length=13, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    telephone = models.CharField(max_length=10, default="")
    gender = models.CharField(max_length=10, default="")
    carreer = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=20, default="")
    def __str__(self):
        return  self.cid + ":" + self.name + ":" + self.surname + ":" + self.address + ":" + self.telephone + ":" + self.gender + ":" + self.carreer + ":" + self.password

class Order(models.Model):
    oid = models.CharField(max_length=13, primary_key=True, default="")
    date = models.CharField(max_length=20, default="")
    status = models.CharField(max_length=50, default="")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.oid + " : " + self.date + " : " + self.status + " : " + self.customer.name

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    price = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id) + " : " + self.order.oid + " : " + self.customer.name + " : " + str(self.price) + " : " + str(self.quantity)

#-----------------ส่วนของminiproject

class Customers(models.Model):
    cid = models.CharField(max_length=13, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    address = models.TextField(max_length=400, default="")
    tel = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=255, default="12345678")
    def __str__(self):
        return self.cid + ":" + self.name + ", " + self.tel

class Sme(models.Model):
    sme_id = models.CharField(max_length=13, primary_key=True, default="")
    sme_name = models.CharField(max_length=50, default="")
    sme_address = models.CharField(max_length=100, default="")
    sme_zipcode = models.CharField(max_length=5, default="")
    sme_regis = models.DateField(default=None)
    sme_history = models.CharField(max_length=1000, default="")
    sme_phone = models.CharField(max_length=10, default="")
    sme_agent = models.CharField(max_length=50, default="")
    sme_objective = models.CharField(max_length=100, default="")
    customer = models.ForeignKey(Customers, max_length=13, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.sme_id + " : " + self.sme_name + " : " + self.sme_address + " : " + self.sme_zipcode + " : " + str(self.sme_regis) + " : " + self.sme_history + " : " + self.sme_phone + " : " + self.sme_agent + " : " + self.sme_objective + " : "

class Borrowing(models.Model):
    borrow_id = models.CharField(max_length=13, primary_key=True, default="")
    borrow_date = models.DateField(default=None)
    borrow_type = models.CharField(max_length=1000, default="")
    borrow_objective = models.CharField(max_length=100, default="")
    borrow_limitmoney = models.FloatField(default=0.00)
    borrow_file = models.CharField(max_length=100, default="")
    borrow_status = models.CharField(max_length=45, default="")
    sme_id = models.ForeignKey(Sme, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.borrow_id + " : "+str(self.borrow_file)+ ":" + self.borrow_type + " : " + self.borrow_objective + " : " + str(self.borrow_limitmoney) + " : " + self.borrow_file + " : " + self. borrow_status + " : " + self.sme_id.sme_id


class Consideration(models.Model):
    csd_id = models.CharField(max_length=13, primary_key=True, default="")
    csd_date = models.DateField(default=None)
    csd_status = models.CharField(max_length=45, default="")
    br_id = models.ForeignKey(Borrowing, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.csd_id + " : " + str(self.csd_date) + " : " + str(self.csd_status) + " : " + self.br_id.borrow_id

class Contract(models.Model):
    ct_id = models.CharField(max_length=10, primary_key=True, default="")
    ct_datecontract = models.CharField(max_length=20, default="")
    ct_fine = models.CharField(max_length=50, default="")
    ct_status = models.CharField(max_length=20, default="")
    ct_payment = models.FloatField(default=0.00)
    ct_interest = models.FloatField(default=0.00)
    ct_amount = models.IntegerField(default=0)
    ct_datepayment = models.CharField(max_length=20, default="")
    ct_dept = models.FloatField(default=0.00)
    ct_limit = models.FloatField(default=0.00)
    br_id = models.ForeignKey(Borrowing, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.ct_id + " : " + " : " + self.ct_datecontract + " : " + self.ct_fine + " : " + self.ct_status + " : " + str(self.ct_payment) + " : " + str(self.ct_interest) + " : " + str(self.ct_amount) + " : " + self.ct_datepayment + " : " + str(self.ct_dept) + " : " + str(self.ct_limit) +" : "+ self.br_id.borrow_id

class Payment(models.Model):
    pm_id = models.CharField(max_length=10, primary_key=True, default="")
    pm_fine = models.FloatField(default=0.00)
    pm_status = models.CharField(max_length=20, default="")
    pm_file = models.CharField(max_length=100, default="")
    pm_bank = models.CharField(max_length=50, default="")
    pm_tranfernumber = models.CharField(max_length=15, default="")
    pm_payment = models.FloatField(default=0.00)
    pm_installment = models.IntegerField(default=0)
    pm_datepayment = models.CharField(max_length=50, default="")
    ct_id = models.ForeignKey(Contract, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.pm_id + " : " + str(self.pm_fine) + " : " + self.pm_status + " : " + self.pm_file + " : " + self.pm_bank + " : " + self.pm_tranfernumber + " : " + str(self.pm_payment) + " : " + str(self.pm_installment) + " : " + self.pm_datepayment + " : " + self.ct_id.ct_id

#----------login---------------
class Employees(models.Model):
    eid = models.CharField(max_length=13, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    birthdate = models.DateField(default=None)
    position = models.CharField(max_length=50, default="")
    password=models.CharField(max_length=255, default="12345678")
    def __str__(self):
        return self.eid + ":" + self.name + ", " + self.position
    # def getCountConfirm(self):
    #     count = Confirms.objects.filter(employee=self).aggregate(count=Count('id'))
    #     return count['count']
    # def getCountAccept(self):
    #     count = Accepts.objects.filter(employee=self).aggregate(count=Count('id'))
    #     return count['count']
    # def getCountSend(self):
    #     count = Send.objects.filter(employee=self).aggregate(count=Count('id'))
    #     return count['count']


