from django.shortcuts import render,HttpResponse,redirect

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
    return render(request, 'showMyData.html' ,{'name':name,'surname':surname,'gender':gender,'status':status,'work':work,'education':education})

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
    myproduct = [["Canon 1 Dx Mark iii","199000","images/idx3.png"],
                 ["Canon 5D Marl iv","89900","images/5d4.png" ],
                 ["Canon 6D Mark ii","79000","images/6d2.png"],
                 ["Canon R5", "159000","images/canonr5.png"],
                 ["Canon R6","119900","images/canonr6.png"],
                 ["Canon R3 ","199000","images/r3.png"],
                 ["Canon Eos M50 Mark ii","45000","images/m50.png"],
                 ["Canon EOS M6 Mark II","35000","images/m62.png"],
                 ["Canon EOS RP", "75000","images/rp.png"],
                 ["Canon EOS R","85000","images/r.png"]]
    return render(request,'showMydatas.html',{'nickname':nickname,'firstname':firstname,'lastname':lastname,'telephone':telephone,'gender':gender,'address':address,'Studying':Studying,'learn':learn,'level':level,'room':room,'myproduct':myproduct})

# from ProfileApp.models import *
# productlist = []
# def showourproduct(request):
#     context = {'product': productlist}
#     return render(request ,'showourproduct.html', context)
#
# def newProduct(request):
#     if request.method == 'POST':
#         id = request.POST['id']
#         name = request.POST['name']
#         brand = request.POST['brand']
#         price = request.POST['price']
#         net = request.POST['net']
#         product = Product(id,name,brand,price,net)
#         productlist.append(product)
#         return redirect('showourproduct')
#     else:
#         return render(request, 'formProductNomal.html')
#
# from ProfileApp.form import *
# def frmproduct(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form = form.cleaned_data
#             id = form.get('id')
#             name = form.get('name')
#             brand = form.get('brand')
#             price = form.get('price')
#             net = form.get('net')
#             product = Product(id,name,brand,price,net)
#             productlist.append(product)
#             return  redirect('showourproduct')
#         else:
#             form = ProductForm(form)
#             context = {'form': form}
#             return render(request, 'formProductNomal.html', context)
#     else:
#         form = ProductForm()
#         context = {'form': form}
#         return  render(request,'formProductNomal.html',context)

