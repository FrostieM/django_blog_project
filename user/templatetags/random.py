import random
from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()

bg_colors = ['video_bg_1.png', 'video_bg_2.png']
@register.simple_tag
def random_bg_color():
    return static('general/img/') + random.choice(bg_colors)
