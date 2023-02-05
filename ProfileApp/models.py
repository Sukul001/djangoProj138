
from django.db import models


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