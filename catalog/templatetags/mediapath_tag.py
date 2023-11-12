from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def mediapath(object_img):
    return mark_safe(f'/media/{object_img}')


@register.simple_tag
def mediapath(object_img):
    media_url = settings.MEDIA_URL
    return f'{media_url}{object_img}'
