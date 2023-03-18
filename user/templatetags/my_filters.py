from django import template

register = template.Library()

@register.filter
def test(obj):
    return obj.total_likes()

@register.filter
def views_count(obj):
    return obj.total_views()