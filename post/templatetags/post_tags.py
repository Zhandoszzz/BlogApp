from django import template
from post.models import *

register = template.Library()

# @register.simple_tag()
# def get_posts():
#     return Post.objects.all()

