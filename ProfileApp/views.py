from django.shortcuts import render,HttpResponse

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

