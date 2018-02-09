import os
import logging
from datetime import datetime, timedelta
from django.apps import apps
from django.contrib.auth.decorators import permission_required
from django.contrib.syndication.views import Feed
from django.core import serializers
from django.db.models import Avg, Count, Min, Max
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse
from reportlab.pdfgen import canvas

from .forms import ChoiceForm, UserForm
from .models import Question, Choice

logger = logging.getLogger('django')

def pdf_generator(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="some.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 100, 'Hello World')
    p.showPage()
    p.save()
    return response

class RssFeed(Feed):
    title = 'Question feed'
    link = '/question/'
    description = ''

    def items(self):
        return Question.objects.all()


class ProfileUpdateView(UpdateView):
    form_class = UserForm

    def get_success_url(self):
        return reverse('my_first_view')

    def get_object(self, queryset=None):
        return self.request.user


class AppListView(ListView):
    template_name = 'main/object_list.html'
    extra_context = {}

def model_detail(request, model, pk):
    model_class = apps.get_model('main', model)
    return DetailView.as_view(model=model_class)(request, pk=pk)


def model_list(request, model):
    model_class = apps.get_model('main', model)
    return AppListView.as_view(model=model_class, extra_context={'model_name': model})(request)

def my_first_view(request):
    # json_data = '{"firstName": "Ivan","lastName": "Ivanov","addresses": [{"address": "Moscow"},{"address": "Peterburg"}]}'
    # d = json.loads(json_data)
    # pass
    # path = os.path.dirname(os.path.realpath(__file__))
    # with open(os.path.join(path, 'img_fjords.jpg'), 'rb') as img:
    #     # content_types application/json application/xml application/pdf
    #     # image/jpg png
    #     return HttpResponse(content=img, content_type='image/%s' % os.path.splitext(img.raw.name)[-1][1:])
    # query_set = Question.objects.all()
    # format = request.GET.get('format')
    # data = serializers.serialize(format, query_set)
    # return HttpResponse(content=data, content_type='application/{}'.format(format))
    qs = Question.objects.all()
    try:
        a = qs[19273].id
    except Exception as exc:
        logger.error(exc)
    return render(request, template_name='main/index.html')

def question_list_view(request):
    query_set = Question.objects.order_by('-pub_date')[:2]
    # query_set.filter(type__in=['apple', 'orange'])
    # query_set.filter(pub_date__lte=datetime.today() + timedelta(days=1),
    #                                     pub_date__gt=datetime.today() - timedelta(days=1)
    #                                     ).order_by('type')

    context_object = {'object_list': query_set, 'model_name': 'question'}
    return render(request, template_name='main/object_list.html', context=context_object)


def question_detail_view(request, pk):
    obj = get_object_or_404(Question, id=pk)
    context_object = {'object': obj}
    return render(request, template_name='question_detail.html', context=context_object)

@permission_required('main.view_choice')
def choice_detail_view(request, pk):
    obj = get_object_or_404(Choice, id=pk)
    context_object = {'object': obj}
    return render(request, template_name='choice_detail.html', context=context_object)


def choice_form(request):
    context = {}
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('thank you!')
        else:
            context['errors'] = form.errors
    context['question_id'] = request.GET.get('question_id')
    return render(request=request, template_name='main/choice_form.html', context=context)

@permission_required('main.change_choice')
def edit_choice(request, pk):
    obj = Choice.objects.get(id=pk)
    form = ChoiceForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponse('edited!')
    context = {'form': form, 'pk': pk}
    return render(request=request, template_name='main/choice_edit.html', context=context)


def delete_choice(request, pk):
    obj = Choice.objects.get(id=pk)
    obj.delete()
    return HttpResponse('deleted')


def question_list(request):
    query_set = Question.objects.all()
    context = {'object_list': query_set, 'value': '<strong>lorem123ipsum</strong>'}
    return render(request=request,
                  template_name='main/question_list.html',
                  context=context)
