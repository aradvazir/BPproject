from django.contrib import admin
from .models import *
# Register your models here.
class answerAdmin(admin.ModelAdmin):
    list_display = ['student_nu', 'ans_title', 'ans_file', 'score', 'date']
admin.site.register(homework)
admin.site.register(answer, answerAdmin)
