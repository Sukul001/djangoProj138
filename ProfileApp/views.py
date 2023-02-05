from django.shortcuts import render, HttpResponse, redirect ,get_object_or_404


# Create your views here.

def test(request):
    return HttpResponse("<H1>Hello world <br> This is My World  Wide web </H1>")


def home(request):
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def story(request):
    return render(request, 'story.html')


def salecamera(request):
    return render(request, 'salecamera.html')


def canon(request):
    return render(request, 'canon.html')


def sony(request):
    return render(request, 'sony.html')


def nikon(request):
    return render(request, 'nikon.html')


def camera(request):
    return render(request, 'camera.html')


def copyname(request):
    return render(request, 'copyname.html')


def storystudy(request):
    return render(request, 'storystudy.html')


def hpy(request):
    return render(request, 'hpy.html')


def showMyData(request):
    name = "sukul"
    surname = "khuridi"
    gender = "male"
    status = "Lecture"
    work = "RMUTI"
    education = "sukul_khuridi"
    return render(request, 'showMyData.html',
                  {'name': name, 'surname': surname, 'gender': gender, 'status': status, 'work': work,
                   'education': education})


def showMydatas(request):
    nickname = "Moo"
    firstname = "Sukul"
    lastname = "Khuridi"
    telephone = "0931305056"
    gender = "Male"
    address = "128/6 "
    Studying = "RMUTI"
    learn = "BIS"
    level = "3"
    room = "1"
    myproduct = [["Canon 1 Dx Mark iii", "199000", "images/idx3.png"],
                 ["Canon 5D Marl iv", "89900", "images/5d4.png"],
                 ["Canon 6D Mark ii", "79000", "images/6d2.png"],
                 ["Canon R5", "159000", "images/canonr5.png"],
                 ["Canon R6", "119900", "images/canonr6.png"],
                 ["Canon R3 ", "199000", "images/r3.png"],
                 ["Canon Eos M50 Mark ii", "45000", "images/m50.png"],
                 ["Canon EOS M6 Mark II", "35000", "images/m62.png"],
                 ["Canon EOS RP", "75000", "images/rp.png"],
                 ["Canon EOS R", "85000", "images/r.png"]]
    return render(request, 'showMydatas.html',
                  {'nickname': nickname, 'firstname': firstname, 'lastname': lastname, 'telephone': telephone,
                   'gender': gender, 'address': address, 'Studying': Studying, 'learn': learn, 'level': level,
                   'room': room, 'myproduct': myproduct})


from ProfileApp.models import *

lstoutproduct = []


def listProduct(request):
    # product = Product('p0001','mouse', 'Aser', 'black', '1canon','4500','7','5','4100')
    # lstoutproduct.append(product)
    context = {'product': lstoutproduct}
    return render(request, 'outputProduct.html', context)


def newProduct(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        type = request.POST['type']
        color = request.POST['color']
        brand = request.POST['brand']
        price = request.POST['price']
        product = Product(id, name, type, color, brand, price)
        lstoutproduct.append(product)
        return redirect('outputProduct')
    else:
        return render(request, 'listProduct.html')
#
#
from ProfileApp.form import *
#
#
def inputProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            name = form.get('name')
            type = form.get('type')
            color = form.get('color')
            brand = form.get('brand')
            price = form.get('price')
            product = Product(id, name, type, color, brand, price)
            lstoutproduct.append(product)
            return redirect('outputProduct')
        else:
            form = ProductForm(form)
            context = {'form': form}
            return render(request, 'inputProduct.html', context)
    else:
        form = ProductForm()
        context = {'form': form}
        return render(request, 'inputProduct.html', context)


from ProfileApp.models import *
# productList = []
# def showourproduct(request):
#     # product = Product('p0001','mouse', 'Aser', '500.00', '120')
#     # productList.append(product)
#     # product = Product('p0002', 'keyboard', 'Aser', '1200.00', '120')
#     # productList.append(product)
#     # product = Product('p0003', 'screen', 'Samsung', '3700.00', '120')
#     # productList.append(product)
#     context = {'products': productList}
#     return render(request,'showourproduct.html',context)
#
# def newProduct(request):
#     if request.method == 'POST': #submit ข้อมูลจากฟอร์มมา
#         id = request.POST['id']
#         name = request.POST['name']
#         brand = request.POST['brand']
#         price = request.POST['price']
#         net = request.POST['net']
#         product = Product(id, name, brand, price, net)
#         productList.append(product)
#         return  redirect ('showourproduct')
#     else: return render(request,'formProductNomal.html')
#
# from ProfileApp.form import *
# def frmProduct(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form = form.cleaned_data
#             id = form.get('id')
#             name = form.get('name')
#             brand = form.get('brand')
#             price = form.get('price')
#             net = form.get('net')
#             product = Product(id, name, brand,price, net)
#             productList.append(product)
#             return redirect('showourproduct')
#         else:
#             form = ProductForm(form)
#
#     else:
#         form = ProductForm ()
#     context = {'form':form}
#     return render(request,'frmproduct.html',context)

# curd
from .models import *
from django.contrib import messages
# def productRetrieveall(request):
#     products = ProductM.objects.all()
#     context = {'products': products}
#     return render(request, 'Product/retrieveallproduct.html', context)
#
#
# def productRetieveOne(request, id):
#     product = ProductM.objects.get(pid=id)  # เช็ค pk
#     context = {'product': product}
#     return render(request, 'Product/retrieveoneproduct.html', context)
#
#
# def createProduct(request):
#     if request.method == 'POST':
#         form = ProductMFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request,messages.SUCCESS,'บันทุกสินค้าใหม่เรียบร้อย.........')
#             return redirect('retrieveallproduct')
#         else:
#             product = ProductM.objects.get(pid=request.POST['pid'])
#             if product:
#                 messages.add_message(request, messages.SUCCESS, 'รหัสสินค้าที่่กำหนดซ้ำกับที่มีอยู่')
#             messages.add_message(request, messages.SUCCESS, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้.........')
#
#     else:
#         form = ProductMFrom()
#     context = {'form':form}
#     return render(request,'Product/createproduct.html',context)

# คนละส่วนกันอีกกกกกกกกก

def showGoodsList(request):
    products = Goods.objects.all()
    context = {'products': products}
    return render(request, 'work/showGoodsList.html', context)


def showGoodsOne(request, id):
    product = Goods.objects.get(gid=id)  # เช็ค pk
    context = {'product': product}
    return render(request, 'work/showGoodsOne.html', context)


def newGoods(request):
    if request.method == 'POST':
        form = showgoodsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'บันทุกสินค้าใหม่เรียบร้อย.........')
            return redirect('showGoodsList')
        else:
            product = Goods.objects.get(gid=request.POST['gid'])
            if product:
                messages.add_message(request, messages.SUCCESS, 'รหัสสินค้าที่่กำหนดซ้ำกับที่มีอยู่')
            messages.add_message(request, messages.SUCCESS, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้.........')

    else:
        form = showgoodsForm()
    context = {'form':form}
    return render(request,'work/newGoods.html',context)

# คนละส่วนกันอีกกกกกกกกก
def showCustomerList(request):
    products = Customer.objects.all()
    context = {'products': products}
    return render(request, 'work/showCustomerList.html', context)


def showCustomerOne(request, id):
    product = Customer.objects.get(cid=id)  # เช็ค pk
    context = {'product': product}
    return render(request, 'work/showCustomerOne.html', context)


def newCustomer(request):
    if request.method == 'POST':
        form = showcustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'บันทุกสินค้าใหม่เรียบร้อย.........')
            return redirect('showCustomerList')
        else:
            product = Customer.objects.get(cid=request.POST['gid'])
            if product:
                messages.add_message(request, messages.SUCCESS, 'รหัสสินค้าที่่กำหนดซ้ำกับที่มีอยู่')
            messages.add_message(request, messages.SUCCESS, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้.........')

    else:
        form = showcustomerForm()
    context = {'form':form}
    return render(request,'work/newCustomer.html',context)