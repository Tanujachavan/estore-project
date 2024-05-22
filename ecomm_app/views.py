from django.shortcuts import render, HttpResponse 
from django.views import View
# Create your views here.



def about(request):
    return HttpResponse("This is about page.")

def home(request):
    return HttpResponse('This is Home page.')

def edit(request, rid):
    print("Id to be edit is: ",rid)

    return HttpResponse("Id to be edited is: "+rid)

def delete(request, x1,x2):
    t=int(x1)+int(x2)
    return HttpResponse("Addition of x1 and x2 is: "+ str(t))   
    #print("Id to be deleted: ",rid)
    #return HttpResponse("Id to be deleted is: "+ rid)

class SimpleView(View):
    def get(self, request):
        return HttpResponse("Hello from view class")

def hello(request):
    context={}
    context['greet']='Good morning children !, We are learning DTL'
    return render(request,'hello.html',context)

def Sweet(request):
    text={}
    text['hello']='Good morning sweetheart! You made my day'
    return render(request,'sweet.html',text)