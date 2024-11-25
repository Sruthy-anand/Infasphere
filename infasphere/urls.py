"""
URL configuration for infasphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from infa import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("posts",views.PostViewSetView,basename="posts")

# localhost:8000/posts
# method:get

# localhost:8000/posts
# method:post

# localhost:8000/posts/1
# method:get

# localhost:8000/posts/1
# method:delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/signup/",views.SignUpApiView.as_view()),
    path("api/posts/<int:pk>/add-comment/",views.CommentCreateView.as_view()),
    path("api/post/<int:pk>/add-likes/",views.AddLikeView.as_view()),
    path("api/token/",ObtainAuthToken.as_view()),

]+router.urls
