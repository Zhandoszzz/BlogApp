from django.urls import path
from .views import *

urlpatterns = [
    path('', PostHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', PostPage.as_view(), name='post_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
]
