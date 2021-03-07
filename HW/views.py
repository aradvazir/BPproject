from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *
# Create your views here.
def Home(request):
    return render(request, 'home.html')

def student (request):
    return render(request,'student.html')

def teacher (request):
    return render(request,'teacher.html')

def student_hw (request):
    Homework= homework.objects.all()
    validcheck=open('userfile.txt', 'r')
    d=validcheck.read()
    validcheck.close()
    Answer=answer.objects.filter(student_nu=d)
    return render(request,'student_hw.html', { 'hw': Homework, 'answer': Answer, 'username': d })

def techer_hw(request):
    Homework=homework.objects.all()
    return render(request, 'teacher_hw.html', {'hw':Homework})

def view_ans(request, hw_title):
    Answer=answer.objects.filter(ans_title=hw_title)
    return render(request, 'teacher_view_ans.html', {'Answer': Answer})

def upload_hw(request):
    form=creat_hw()
    if request.method=='POST':
        form=creat_hw(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('your HomeWork File has been uploaded')
    return render(request, 'upload_hw.html', {'form': form})

def uplaod_ans(request):
    form=creat_answer()
    if request.method=='POST':
        form=creat_answer(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Your answer has been uploaded')
    return render(request, 'upload_ans.html', {'form':form})