from django.shortcuts import render

from .models import Teacher


def teachers_list(request):
    teachers = list(Teacher.objects.values())
    return render(request, "teachers_list.html", context={"teachers": teachers})
