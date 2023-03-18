from django import template

register = template.Library()

@register.filter(name='check')
def check(value):
    """
    Checking this also
    """
    return value.total_likes()