from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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
            messages.add_message(request,messages.SUCCESS,'บันทึกสินค้าใหม่เรียบร้อย.........')
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

def updateGoods(request, id):
    product = get_object_or_404(Goods,gid=id)
    form = showgoodsForm(data=request.POST or None, instance=product)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'แก้ไขสินค้าใหม่เรียบร้อย.........')
            return  redirect('showGoodsList')
        else:
            context = {'form': form}
            messages.add_message(request, messages.SUCCESS, 'ข้อมูลไม่ถูกต้อง.........',context)
    else:
        form.updateGoods()
        context = {'form': form}
        return  render(request, 'work/updateGoods.html',context)

def deleteGoods(request, id):
    product = get_object_or_404(Goods,gid=id)
    if product:
        product.delete()
        messages.add_message(request, messages.SUCCESS, 'ลบข้อมูลเรียบร้อย')
        return redirect('showGoodsList')
    else:
        messages.add_message(request, messages.ERROR, 'ไม่สามารถลบข้อมูลสินค้า')
    return redirect('showGoodsList')

# def deleteGoodss(request, id=None):   ทำในหน้า deleteGoods
#     if request.method == "POST":
#         id = request.POST['gid']
#         product = Goods.objects.get(gid=id)
#         product.delete()
#         return redirect('showGoodsList')
#     else:
#         product = Goods.objects.get(gid=id)
#         context = {'product':product}
#         return render(request,'work/deleteGoods.html',context)

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
            messages.add_message(request,messages.SUCCESS,'บันทึกสินค้าใหม่เรียบร้อย.........')
            return redirect('showCustomerList')
        else:
            product = Customer.objects.get(cid=request.POST['cid'])
            if product:
                messages.add_message(request, messages.SUCCESS, 'รหัสสินค้าที่่กำหนดซ้ำกับที่มีอยู่')
            messages.add_message(request, messages.SUCCESS, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้.........')

    else:
        form = showcustomerForm()
    context = {'form':form}
    return render(request,'work/newCustomer.html',context)

def updateCustomer(request, id):
    product = get_object_or_404(Customer,cid=id)
    form = showcustomerForm(data=request.POST or None, instance=product)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'แก้ไขสินค้าใหม่เรียบร้อย.........')
            return  redirect('showCustomerList')
        else:
            context = {'form': form}
            messages.add_message(request, messages.SUCCESS, 'ข้อมูลไม่ถูกต้อง.........',context)
    else:
        form.updateCustomer()
        context = {'form': form}
        return  render(request, 'work/updateCustomer.html',context)

def deleteCustomer(request, id):
    product = get_object_or_404(Goods,cid=id)
    if product:
        product.delete()
        messages.add_message(request, messages.SUCCESS, 'ลบข้อมูลเรียบร้อย')
        return redirect('showCustomerList')
    else:
        messages.add_message(request, messages.ERROR, 'ไม่สามารถลบข้อมูลสินค้า')
    return redirect('showCustomerList')

#-----------------ส่วนของminiproject
def showSme(request):
    # return HttpResponse(request.session['userId'])

    userId = request.session.get('userId')
    customer = Customers.objects.get(cid=userId)

    products = Sme.objects.filter(customer=userId)
    context = {'products': products}
    return render(request, 'miniproject/showSme.html', context)


def oneSme(request, id):
    product = Sme.objects.get(sme_id=id)  # เช็ค pk
    context = {'product': product}
    return render(request, 'miniproject/oneSme.html', context)


def addSme(request):
    # return HttpResponse(request.session['userId'])
    # return HttpResponse("request.session['userId']")

    if request.method == 'POST':
        # return 'test'

        form = showSmeForm(request.POST)

        if form.is_valid():

            form.save()
            messages.add_message(request,messages.SUCCESS,'บันทึกสินค้าใหม่เรียบร้อย.........')
            return redirect('showSme')
        else:
            # return HttpResponse(request.POST['sme_id'])

            product = Sme.objects.get(sme_id=request.POST['sme_id'])

            if product:
                messages.add_message(request, messages.SUCCESS, 'รหัสสินค้าที่่กำหนดซ้ำกับที่มีอยู่')
            messages.add_message(request, messages.SUCCESS, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้.........')

    else:
        form = showSmeForm()

    context = {'form':form}
    return render(request,'miniproject/addSme.html',context)

def updateSme(request, id):
    product = get_object_or_404(Sme,sme_id=id)
    form = showSmeForm(data=request.POST or None, instance=product)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'แก้ไขสินค้าใหม่เรียบร้อย.........')
            return  redirect('showSme')
        else:
            context = {'form': form}
            messages.add_message(request, messages.SUCCESS, 'ข้อมูลไม่ถูกต้อง.........',context)
    else:
        form.updateSme()
        context = {'form': form}
        return  render(request, 'miniproject/updateSme.html',context)

def deleteSme(request, id):
    product = get_object_or_404(Sme,sme_id=id)
    if product:
        product.delete()
        messages.add_message(request, messages.SUCCESS, 'ลบข้อมูลเรียบร้อย')
        return redirect('showSme')
    else:
        messages.add_message(request, messages.ERROR, 'ไม่สามารถลบข้อมูลสินค้า')
    return redirect('showSme')
#--------------------------------------------------------------------------------------------
def showBorrowing(request):
    products = Borrowing.objects.all()
    context = {'products': products}
    return render(request, 'miniproject/showBorrowing.html', context)


def oneBorrowing(request, id):
    product = Borrowing.objects.get(borrow_id=id)  # เช็ค pk
    context = {'product': product}
    return render(request, 'miniproject/oneBorrowing.html', context)


def addBorrowing(request):
    if request.method == 'POST':
        form = showBorrowingForm(request.POST or None, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'บันทึกสินค้าใหม่เรียบร้อย.........')
            return redirect('showBorrowing')
        else:
            product = Borrowing.objects.get(borrow_id=request.POST['borrow_id'])
             #product = showBorrowingForm(initial={'Borrowing': Borrowing})
            if product:
                messages.add_message(request, messages.SUCCESS, 'รหัสสินค้าที่่กำหนดซ้ำกับที่มีอยู่')
            messages.add_message(request, messages.SUCCESS, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้.........')

    else:
        form = showBorrowingForm()
    context = {'form':form}
    return render(request,'miniproject/addBorrowing.html',context)

def updateBorrowing(request, id):
    product = get_object_or_404(Borrowing,borrow_id=id)
    form = showBorrowingForm(data=request.POST or None, instance=product)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'แก้ไขสินค้าใหม่เรียบร้อย.........')
            return  redirect('showBorrowing')
        else:
            context = {'form': form}
            messages.add_message(request, messages.SUCCESS, 'ข้อมูลไม่ถูกต้อง.........',context)
    else:
        form.updateBorrowing()
        context = {'form': form}
        return  render(request, 'miniproject/updateBorrowing.html',context)

def deleteBorrowing(request, id):
    product = get_object_or_404(Borrowing,borrow_id=id)
    if product:
        product.delete()
        messages.add_message(request, messages.SUCCESS, 'ลบข้อมูลเรียบร้อย')
        return redirect('showSme')
    else:
        messages.add_message(request, messages.ERROR, 'ไม่สามารถลบข้อมูลสินค้า')
    return redirect('showSme')

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            approval = form.cleaned_data['approval']
            # Do something with the approval value
    else:
        form = MyForm()
    return render(request, 'miniproject/updateBorrowing.html', {'form': form})
#--------------------------------------------------------------------------------------------
def showConsideration(request):
    products = Consideration.objects.all()
    context = {'products': products}
    return render(request, 'miniproject/showConsideration.html', context)


def oneConsideration(request, id):
    product = Consideration.objects.get(csd_id=id)  # เช็ค pk
    context = {'product': product}
    return render(request, 'miniproject/oneConsideration.html', context)


def addConsideration(request):
    if request.method == 'POST':
        form = showConsiderationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'บันทึกสินค้าใหม่เรียบร้อย.........')
            return redirect('showConsideration')
        else:
            product = Consideration.objects.get(csd_id=request.POST['csd_id'])
            if product:
                messages.add_message(request, messages.SUCCESS, 'รหัสสินค้าที่่กำหนดซ้ำกับที่มีอยู่')
            messages.add_message(request, messages.SUCCESS, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้.........')

    else:
        form = showConsiderationForm()
    context = {'form':form}
    return render(request,'miniproject/addConsideration.html',context)

def updateConsideration(request, id):
    product = get_object_or_404(Consideration,csd_id=id)
    form = showConsiderationForm(data=request.POST or None, instance=product)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'แก้ไขสินค้าใหม่เรียบร้อย.........')
            return  redirect('showConsideration')
        else:
            context = {'form': form}
            messages.add_message(request, messages.SUCCESS, 'ข้อมูลไม่ถูกต้อง.........',context)
    else:
        form.updateConsideration()
        context = {'form': form}
        return  render(request, 'miniproject/updateConsideration.html',context)

def deleteConsideration(request, id):
    product = get_object_or_404(Consideration,csd_id=id)
    if product:
        product.delete()
        messages.add_message(request, messages.SUCCESS, 'ลบข้อมูลเรียบร้อย')
        return redirect('showConsideration')
    else:
        messages.add_message(request, messages.ERROR, 'ไม่สามารถลบข้อมูลสินค้า')
    return redirect('showConsideration')
#--------------------------------------------------------------------------------------------
def showContract(request):
    products = Contract.objects.all()
    context = {'products': products}
    return render(request, 'miniproject/showContract.html', context)


def oneContract(request, id):
    product = Contract.objects.get(ct_id=id)  # เช็ค pk
    context = {'product': product}
    return render(request, 'miniproject/oneContract.html', context)


def addContract(request):
    if request.method == 'POST':
        form = showContractForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'บันทึกสินค้าใหม่เรียบร้อย.........')
            return redirect('showContract')
        else:
            product = Consideration.objects.get(ct_id=request.POST['ct_id'])
            if product:
                messages.add_message(request, messages.SUCCESS, 'รหัสสินค้าที่่กำหนดซ้ำกับที่มีอยู่')
            messages.add_message(request, messages.SUCCESS, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้.........')

    else:
        form = showContractForm()
    context = {'form':form}
    return render(request,'miniproject/addContract.html',context)

def updateContract(request, id):
    product = get_object_or_404(Contract,ct_id=id)
    form = showContractForm(data=request.POST or None, instance=product)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'แก้ไขสินค้าใหม่เรียบร้อย.........')
            return  redirect('showContract')
        else:
            context = {'form': form}
            messages.add_message(request, messages.SUCCESS, 'ข้อมูลไม่ถูกต้อง.........',context)
    else:
        form.updateContract()
        context = {'form': form}
        return  render(request, 'miniproject/updateContract.html',context)

def deleteContract(request, id):
    product = get_object_or_404(Contract,ct_id=id)
    if product:
        product.delete()
        messages.add_message(request, messages.SUCCESS, 'ลบข้อมูลเรียบร้อย')
        return redirect('showContract')
    else:
        messages.add_message(request, messages.ERROR, 'ไม่สามารถลบข้อมูลสินค้า')
    return redirect('showContract')


#--------------------------------------------------------------------------------------------
def showPayment(request):
    products = Payment.objects.all()
    context = {'products': products}
    return render(request, 'miniproject/showPayment.html', context)


def onePayment(request, id):
    product = Payment.objects.get(pm_id=id)  # เช็ค pk
    context = {'product': product}
    return render(request, 'miniproject/onePayment.html', context)


def addPayment(request):
    if request.method == 'POST':
        form = showPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'บันทึกสินค้าใหม่เรียบร้อย.........')
            return redirect('showPayment')
        else:
            product = Payment.objects.get(pm_id=request.POST['pm_id'])
            if product:
                messages.add_message(request, messages.SUCCESS, 'รหัสสินค้าที่่กำหนดซ้ำกับที่มีอยู่')
            messages.add_message(request, messages.SUCCESS, 'ไม่สามารถบันทึกข้อมูลสินค้าใหม่ได้.........')

    else:
        form = showPaymentForm()
    context = {'form':form}
    return render(request,'miniproject/addPayment.html',context)

def updatePayment(request, id):
    product = get_object_or_404(Payment,pm_id=id)
    form = showPaymentForm(data=request.POST or None, instance=product)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'แก้ไขสินค้าใหม่เรียบร้อย.........')
            return  redirect('showPayment')
        else:
            context = {'form': form}
            messages.add_message(request, messages.SUCCESS, 'ข้อมูลไม่ถูกต้อง.........',context)
    else:
        form.updatePayment()
        context = {'form': form}
        return  render(request, 'miniproject/updatePayment.html',context)

def deletePayment(request, id):
    product = get_object_or_404(Payment,pm_id=id)
    if product:
        product.delete()
        messages.add_message(request, messages.SUCCESS, 'ลบข้อมูลเรียบร้อย')
        return redirect('showPayment')
    else:
        messages.add_message(request, messages.ERROR, 'ไม่สามารถลบข้อมูลสินค้า')
    return redirect('showPayment')
# ---- login--------------------------------------------------------------------------------------------
def userChangePassword(request):
    userId = request.session.get('userId')
    user = None
    if request.method == 'POST':
        form=ChangePasswordForm(request.POST or None)
        if request.session.get('userStatus') == 'customer':
            user = get_object_or_404(Customers, cid=userId)
        else:
            user = get_object_or_404(Employees, eid=userId)
        context = {'form': form}
        if request.POST['oldPassword'] == user.password:
            if request.POST['newPassword'] == request.POST['confirmPassword']:
                user.password = request.POST['newPassword']
                user.save()
                messages.add_message(request, messages.INFO, "เปลี่ยนรหัสผ่านเสร็จเรียบร้อย...")
                return redirect('home')
            else:
                messages.add_message(request, messages.WARNING, "รหัสผ่านใหม่กับรหัสที่ยืนยันไม่ตรงกัน...")
                return render(request, 'miniproject/userChangePassword.html', context)
        else:
            messages.add_message(request, messages.ERROR, "รหัสผ่านที่ระบุไม่ถูกต้อง...")
            return render(request, 'miniproject/userChangePassword.html', context)
    else:
        form=ChangePasswordForm(initial={'userId':userId})
        context ={'form':form}
        return render(request, 'miniproject/userChangePassword.html', context)



def userResetPassword(request, userId):
    user = None
    if request.method == 'POST':
        form=ResetPasswordForm(request.POST or None)
        if request.session.get('userStatus') == 'customer':
            user = get_object_or_404(Customers, cid=userId)
        else:
            user = get_object_or_404(Employees, eid=userId)
        context = {'form': form}
        if request.POST['newPassword'] == request.POST['confirmPassword']:
            user.password = request.POST['newPassword']
            user.save()
            messages.add_message(request, messages.INFO, "เปลี่ยนรหัสผ่านเสร็จเรียบร้อย...")
            return redirect('home')
        else:
            messages.add_message(request, messages.WARNING, "รหัสผ่านใหม่กับรหัสที่ยืนยันไม่ตรงกัน...")
            return render(request, 'miniproject/userResetPassword.html', context)
    else:
        form=ResetPasswordForm(initial={'userId':userId})
        context ={'form':form}
        return render(request, 'miniproject/userResetPassword.html', context)


def userAuthen(request):
    if request.method == 'POST':
        userName = request.POST.get("userName")
        userPass = request.POST.get("userPass")
        user = Customers.objects.filter(cid=userName).filter(password=userPass).first()
        # user = get_object_or_404(Customers, cid=userName, password=userPass)
        if user:
            request.session['userId'] = user.cid
            request.session['userName'] = user.name
            request.session['userStatus'] = 'customer'
            # messages.add_message(request, messages.INFO, "Login success..")
            if request.session.get('orderActive'):
                del request.session['orderActive']
                return redirect('checkout')
            else:
                return redirect('home')
        else:
            user = Employees.objects.filter(eid=userName).filter(password=userPass).first()
            if user:
                request.session['userId'] = user.eid
                request.session['userName'] = user.name
                request.session['userStatus'] = user.position
                # messages.add_message(request, messages.INFO, "Login success..")
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, "User or Password not Correct!!!..")
                data={'userName':userName}
                return render(request, 'miniproject/userAuthen.html', data)
    else:
        data = {'userName': ''}
        return render(request, 'miniproject/userAuthen.html', data)


def userLogout(request):
    del request.session["userId"]
    del request.session["userName"]
    del request.session["userStatus"]
    return  redirect('home')

def customerList(request):
    customers = Customers.objects.all().order_by('cid')
    context = {'customers':customers}
    return render(request, 'miniproject/customerList.html', context)

def showcustomerList(request):
    customers = Customers.objects.all().order_by('cid')
    context = {'customers':customers}
    return render(request, 'miniproject/showcustomerList.html', context)

def customerRegistration(request):
    if request.method == 'POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userAuthen')
        else:
            context = {'form': form}
            return render(request, 'miniproject/customerRegister.html', context)
    else:
        form = CustomersForm()
        context = {'form': form}
        return render(request, 'miniproject/customerRegister.html', context)

def customerUpdate(request, cid):
    customer = get_object_or_404(Customers, cid=cid)
    if request.method == 'POST':
        form = CustomersForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            if request.session.get('userStatus') == 'customer':
                return redirect('home')
            else:
                return redirect('customerList')
        else:
            context = {'form': form}
            return render(request, 'miniproject/customerUpdate.html', context)
    else:
        form = CustomersForm(instance=customer)
        form.updateForm()
        context = {'form': form}
        return render(request, 'miniproject/customerUpdate.html', context)
#---------------------------------------------------------หน้าของใลน์ Notify--------------

#---------------------------------------------------------หน้าของ PDF--------------
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def pdfProductReport(request):
    pdfmetrics.registerFont(TTFont('THSarabunNew', 'thsarabunnew-webfont.ttf'))
    pdfmetrics.registerFont(TTFont('THSarabunNew-Bold', 'thsarabunnew_bold-webfont.ttf'))
    template = get_template('miniproject/pdfProductReport.html')
    products = Sme.objects.all()
    context = {"products": products}
    html = template.render(context)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("<h1><b>เกิดข้อผิดพลาด!!!</b> ไม่สามารถสร้างเอกสาร PDF ได้...</h2>", status=400)

def pdfBorrowing(request):
    pdfmetrics.registerFont(TTFont('THSarabunNew', 'thsarabunnew-webfont.ttf'))
    pdfmetrics.registerFont(TTFont('THSarabunNew-Bold', 'thsarabunnew_bold-webfont.ttf'))
    template = get_template('miniproject/pdfBorrowing.html')
    products = Borrowing.objects.all()
    context = {"products": products}
    html = template.render(context)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("<h1><b>เกิดข้อผิดพลาด!!!</b> ไม่สามารถสร้างเอกสาร PDF ได้...</h2>", status=400)
#---------------------------------------------------------กราฟ--------------
import pandas as pd
import plotly.express as px
def dashboardPieGraph(request):
    BorrowAll = Borrowing.objects.all()
    borrowID = []
    borrowlimit = []
    for item in BorrowAll:
        borrowID.append(item.borrow_id)
        borrowlimit.append(item.borrow_limitmoney)
    df = pd.DataFrame({"Product": borrowID, "Amount": borrowlimit}, columns=['Product', 'Amount'])
    fig = px.pie(df, hole=.3, names='Product', values ='Amount', title="แผนภูมิวงกลมแสดงยอดขายแยกตามรายชื่อสินค้า")
    fig.update_layout(autosize=False, width=600, height=400,
                      margin = dict(l=10, r=10, b=100, t=100, pad=5 ),
                      paper_bgcolor = "aliceblue",)
    chart = fig.to_html()
    context = {'chart':chart}
    return render(request, 'miniproject/dashbordPie.html', context)
