from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable_one':'var 1',
        'variable_two':'var 2',
    }
    # return HttpResponse("Here is your home page")
    return render(request,"index.html",context)


def about(request):
    # return HttpResponse("Here is your about page")
    return render(request,"about.html")


def contact(request):
    # return HttpResponse("Here is your contact page")
    return render(request,"contact.html")



def services(request):
    # return HttpResponse("Here is your services page")
    return render(request,"services.html")


