from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Test, Question
from lessons.forms import QuestionForm, QuestionFormSet, AnswerFormSet
from tests.forms import TestForm


def index(request):
    return render(request, 'index.html')


def test_list(request):
    tests = Test.objects.all()
    return render(request, 'tests/test-list.html', {'tests': tests})


def test_create(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        question_formset = QuestionFormSet(request.POST)
        if form.is_valid() and question_formset.is_valid():
            test = form.save()
            question_formset.instance = test
            question_formset.save()
            messages.success(request, 'Test created successfully.')
            return redirect('tests:test_list')
    else:
        form = TestForm()
        question_formset = QuestionFormSet()
    return render(request, 'tests/test-create.html', {'form': form, 'question_formset': question_formset})


def test_edit(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        question_formset = QuestionFormSet(request.POST, instance=test)
        if form.is_valid() and question_formset.is_valid():
            form.save()
            question_formset.save()
            messages.success(request, 'Test updated successfully.')
            return redirect('tests:test_list')
    else:
        form = TestForm(instance=test)
        question_formset = QuestionFormSet(instance=test)
    return render(request, 'tests/test-edit.html', {'form': form, 'question_formset': question_formset})


def delete(request, pk):
    test = get_object_or_404(Test, pk=pk)
    test.delete()
    return redirect('tests:test_list')


def question_edit(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        answer_formset = AnswerFormSet(request.POST, instance=question)
        if form.is_valid() and answer_formset.is_valid():
            form.save()
            answer_formset.save()
            messages.success(request, 'Question updated successfully.')
            return redirect('tests:test_edit', pk=question.test.pk)
    else:
        form = QuestionForm(instance=question)
        answer_formset = AnswerFormSet(instance=question)
    return render(request, 'tests/test-edit.html', {'form': form, 'answer_formset': answer_formset})

