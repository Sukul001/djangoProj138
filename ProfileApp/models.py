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



# class Product:
#     def __init__(self, id, name, brand, price, net):
#         self.id = id
#         self.name = name
#         self.brand = brand
#         self.price = price
#         self.net = net
#
#     def __str__(self):
#         return "ID:{}, Name:{}, Brand:{}, Price:{}, Net:{}".format(self.id, self.name, self.brand, self.price, self.net)
