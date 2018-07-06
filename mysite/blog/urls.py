from django.conf.urls import url, include
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import re_path
from blog.models import Post
from django.urls import path

urlpatterns = [ 
                url(r'', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],template_name="blog/blog.html")), #passing all elements in post table to the ListView
				path('<int:pk>', DetailView.as_view(
                                    model = Post,
                                    template_name="blog/post.html")),
       
]