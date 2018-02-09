from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from .views import my_first_view, \
    question_list, \
    edit_choice, \
    model_detail, \
    model_list, \
    question_list_view, \
    RssFeed, \
    pdf_generator
from .models import Question, Choice

urlpatterns = [
    url('question/$', question_list, name='question_list'),
    url('question/(?P<pk>\d+)/$', DetailView.as_view(model=Question), name='question_detail'),
    url('rss/', RssFeed(), name='rss_feed'),
    url('pdf/', pdf_generator, name='pdf'),
    # url('<model>/', model_list, name='object_list'),
    # path('<model>/<int:pk>/', model_detail, name='object_detail'),
    url('choice/(?P<pk>\d+)/edit/', edit_choice, name='edit_choice'),
    url('', login_required(my_first_view), name='my_first_view'),

    # path('choice/', ListView.as_view(model=Choice, template_name='main/object_list.html'), name='choice_list'),
    # path('choice/add/', choice_form, name='add_choice'),
    url('choice/(?P<pk>\d+)/', DetailView.as_view(model=Choice), name='choice_detail'),
]

