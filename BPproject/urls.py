"""BPproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from VID.views import *
from HW.views import *
from login_page.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='Home'),
    path('student/', student, name='student'),
    path('student/videos/', student_video, name='student_videos'),
    path('teacher/',teacher, name='teacher'),
    path('teacher/videos/', teacher_video, name='teacher_videos'),
    path('teacher/videos/upload/', upload_video, name='upload_video'),
    path('student/homework/',student_hw, name='student_homework'),
    path('student/homework/upload/', uplaod_ans, name='upload_answer'),
    path('teacher/homework/',techer_hw, name='teacher_homework'),
    path('teacher/homework/upload/',upload_hw,name='upload_homework'),
    path('teacher/homework/<str:hw_title>/', view_ans, name='view_answer'),
    path('teacher/login/', teacher_login_view, name='teacher_login'),
    path('student/login/', student_login_view, name='student_login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
