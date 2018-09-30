from django.shortcuts import render, redirect
from apps.course.models import Course
from apps.course.form import CourseForm
from django.db.models import Q
from sweetify import *
from apps.home.pagination import paginate


def index(request):
    courses = paginate(request, Course.objects.all(), 5)
    return render(request, 'course/index.html', {
        'object_list': courses,
        'title': 'Cursos',
    })


def create(request):
    if request.method == 'POST':
        CourseForm(request.POST).save()
        success(request, 'Curso guardado correctamente!', toast=True, position='top', timer=2000)
        return redirect('course:index')

    return render(request, 'course/create.html', {
        'form': CourseForm,
        'title': 'Registrar',
    })


def edit(request, id_course):
    course = Course.objects.get(pk=id_course)
    if request.method == 'POST':
        CourseForm(request.POST, instance=course).save()
        success(request, 'Editado correctamente!', toast=True, position='top', timer=2000)
        return redirect('course:index')

    return render(request, 'course/edit.html', {
        'form': CourseForm(instance=course),
        'title': 'Editar',
    })


def show(request, id_course):
    course = Course.objects.get(pk=id_course)
    return render(request, 'course/show.html', {'object_list': course})


def delete(request, id_course):
    Course.objects.get(pk=id_course).delete()
    return render(request, 'course/table.html')


def table(request):
    courses = paginate(request, Course.objects.all(), 5)
    return render(request, 'course/table.html', {'object_list': courses})


def search(request, find):
    courses_list = Course.objects.filter(
        Q(name__icontains=find))
    courses = paginate(request, courses_list, 5)
    return render(request, 'course/table.html', {'object_list': courses})
