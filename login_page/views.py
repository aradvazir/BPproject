from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse

# Create your views here.
def teacher_login_view(request):
    if request.method=='POST':
        user_name=request.POST['username']
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            validcheck=open('userfile.txt', 'w').write(user_name)
            validcheck.close()
            return redirect('/teacher')
    form=AuthenticationForm()
    return render(request, 'login_form.html', {'form':form})

def student_login_view(request):
    if request.method=='POST':
        user_name=request.POST['username']
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            validcheck=open('userfile.txt', 'w').write(user_name)
            validcheck.close()
            return redirect('/teacher')
    form=AuthenticationForm()
    return render(request, 'login_form.html', {'form':form})

def users(request):
    form=AuthenticationForm(data=request.POST)
    user=form.get_user()
    return render(request, 'student_hw.html', {'user':user})