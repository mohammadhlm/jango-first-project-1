from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm,LoginForm

def home_page(request):
    myname="mohammad"
    context={
        "myname":"mohammad"
    }
    return render(request,"home_page.html",context)

def contact_page(request):
    contact_form=ContactForm(request.POST or None)
    context={
        "title" : "درباره ما",
        "content" : "این یک متن تستی است",
        "form" : contact_form
    }
    if contact_form.is_valid():
        result = contact_form.cleaned_data
        print(result)
        print(result["fullname"])
    # if request.method =="POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('message'))
    return render(request,'contact/view.html',context)
def login_page(request):
    print(request.user.is_authenticated)
    form=LoginForm(request.POST or None)
    context={
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,"auth/login.html",context)

def register_page(request):
    return render(request,"auth/login.html",{})
