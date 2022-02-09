from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import auth,messages

from .models import Member
from .forms import RegisterForm, UserEditForm

def index(request):
    return render(request, 'index.html',{
    })
    
def userinfo(request):
    if request.user.is_authenticated:
        return render(request, 'personal_info.html')
    else:
        return HttpResponseRedirect('/accounts/login/')

def useredit(request):
    member = request.user.member
    form = UserEditForm(instance=member)

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/main/userinfo')
    
    context = {'form':form}
    return render(request, 'useredit.html', context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request,user)
            
            messages.success(request, "Registration successful.")
            return HttpResponseRedirect('/main')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render(request, 'register.html', {
        'form' : form,
    })