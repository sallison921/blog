"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from JamieBlog import views
from .views import AllPostsView
from .views import ArticleView
from .views import AddPostView
from .views import UpdatePostView
from .views import DeletePostView
from .views import AboutView
from .views import HomeView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('allPosts/', AllPostsView.as_view(), name='allPosts'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('addPost/', AddPostView.as_view(), name="addPost"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="updatePost"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="deletePost"),
    path('about/', AboutView.as_view(), name = "about"),
   
]

urlpatterns += staticfiles_urlpatterns()