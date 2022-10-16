from .models import *

class DataMixin:
    paginate_by = 1
    model = Post
    template_name = 'post/posts.html'
    context_object_name = 'posts'
    allow_empty = False
