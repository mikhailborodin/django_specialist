import re
from django import template
from django.db.models import Avg, Sum, Min, Max

register = template.Library()

@register.filter(name='reg_cut')
def reg_cut(value, arg):
    return re.sub(arg, ' ', value)

@register.simple_tag(name='aggregate_functions')
def avg(obj):
    # https://docs.djangoproject.com/en/2.0/ref/templates/builtins/
    aggr = obj.choice_set.all().aggregate(Avg('votes'), Min('votes'), Max('votes'), Sum('votes'))
    return aggr

