from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView
from django.core.paginator import  Paginator
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout,login
from .models import *
from .utils import *
from .forms import RegisterUserForm, LoginUserForm
# Create your views here.
# def post_page(req, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)
#     return render(req, 'post/postpage.html', {'post':post})
class PostPage(DetailView):
    model = Post
    template_name = "post/postpage.html"
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        return context


class PostHome(DataMixin, ListView):


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Homepage"
        return context


class PostCategory(DataMixin, ListView):


    def get_context_data(self, *, object_list=None, **kwargs):
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        context = super().get_context_data(**kwargs)
        context['title'] = "Category - " +(cat.name)
        return context

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'])

#def main_page(req):
#    return render(req, 'post/posts.html')
#
# def category_page(req, cat_slug):
#     c = Category.objects.get(slug=cat_slug)
#     posts = c.post_set.all()
#     return render(req, 'post/posts.html', {'posts':posts})

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'post/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    success_url = reverse_lazy('login')
    form_class = RegisterUserForm
    template_name = 'post/register.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('home')
