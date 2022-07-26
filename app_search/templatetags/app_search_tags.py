from django import template
from django.utils.http import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, request, field, value):
    query = request.GET.copy()
    old_value = request.GET.get(field, '')
    if field in ['status', 'order_by'] or old_value == '':
        query[field] = value
    else:
        query[field] = fr'{old_value}-{value}'




    context['disabled_fields'] = request.GET.copy()
    return query.urlencode()
