from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Here is your home page")


def about(request):
    return HttpResponse("Here is your about page")


def contact(request):
    return HttpResponse("Here is your contact page")



def services(request):
    return HttpResponse("Here is your services page")


