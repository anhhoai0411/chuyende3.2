# EnglishLearningApp/views.py
from django.shortcuts import render
from .models import EnglishCourse

def english_course_list(request):
    courses = EnglishCourse.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

