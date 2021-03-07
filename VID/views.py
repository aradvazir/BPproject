from django.shortcuts import render
from .form import creat_vid
from django.http import HttpResponse
from .models import teachvideos

def teacher_video(request):
    videos= teachvideos.objects.all()
    return render(request,'teacher_vid.html', { 'video': videos })

def student_video (request):
    videos= teachvideos.objects.all()
    return render(request,'student_vid.html', { 'video': videos })


def upload_video (request):
    form = creat_vid()
    if request.method=='POST':
        form= creat_vid(request.POST,request.FILES)
        if form .is_valid():
            form.save()
            return HttpResponse('Uploaded')
    return render(request,'upload_vid.html', { 'form':form })
