from django.urls import path,re_path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', PostPage.as_view(), name='post_page'),
    path('login/', cache_page(60)(LoginUser.as_view()), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', cache_page(60)(RegisterUser.as_view()), name='register'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
    path('post/<slug:post_slug>/comment/', AddComment.as_view(), name='add_comment'),
    path('search/', Search.as_view(), name='search'),
]
