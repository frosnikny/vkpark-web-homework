from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from . import models


# Create your views here.

def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    page_obj = paginate(models.QUESTIONS, request, 5)
    context = {
        'questions': models.QUESTIONS[page_obj.start_index() - 1: page_obj.end_index()],
        'new_questions': "new_questions",
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context=context)


def hot(request):
    hot_questions = [i for i in models.QUESTIONS if i['id'] in models.TOP]
    page_obj = paginate(hot_questions, request, 5)
    context = {
        'questions': hot_questions[page_obj.start_index() - 1: page_obj.end_index()],
        'page_obj': page_obj,
    }
    return render(request, 'index_hot.html', context=context)


def index_tag(request, tag):
    tag_questions = [x for x in models.QUESTIONS if tag in x['tags']]
    page_obj = paginate(tag_questions, request, 5)
    context = {
        'questions': tag_questions[page_obj.start_index() - 1: page_obj.end_index()],
        'tag': tag,
        'page_obj': page_obj,
    }
    return render(request, 'index_tag.html', context=context)


def question(request, question_id):
    if question_id >= len(models.QUESTIONS):
        raise Http404
    context = {'question': models.QUESTIONS[question_id]}
    return render(request, 'question.html', context=context)


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def settings(request):
    return render(request, 'settings.html')
