from django import template

register = template.Library()

@register.filter

def split(arg1,arg2):
    return arg1[0:arg2]