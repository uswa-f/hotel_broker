from django.shortcuts import render , HttpResponse

# Create your views here.
def index (request):
    return render(request , 'index.html')
   # return HttpResponse("this is home page")

def about (request):
    return render(request , 'index.html')
    #return HttpResponse("this is about page")

def services (request):
    return render(request , 'signIn.html')
    #return HttpResponse("this is services page")

def contact (request):
    return render(request , 'signUp.html')
    #return HttpResponse("this is contact page")

