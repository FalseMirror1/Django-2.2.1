from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'

    student_objects = Student.objects.order_by(ordering)
    students = list({'name': st.name, 'teachers': Teacher.objects, 'group': st.group} for st in student_objects)

    context = {
        'object_list': students
    }
    return render(request, template, context)
