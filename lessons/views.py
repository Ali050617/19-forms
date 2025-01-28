from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Lesson
from .forms import LessonForm


def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson-list.html', {'lessons': lessons})


def lesson_create(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson created successfully.')
            return redirect('lessons:lesson_list')
    else:
        form = LessonForm()
    return render(request, 'lessons/lesson-create.html', {'form': form})


def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lessons/lesson-detail.html', {'lesson': lesson})


def lesson_edit(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson updated successfully.')
            return redirect('lessons:lesson_list')
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'lessons/lesson-create.html', {'form': form, 'lesson': lesson})


def delete_lesson(request, pk):
    test = get_object_or_404(Lesson, pk=pk)
    test.delete()
    return redirect('lessons:lesson_list')
