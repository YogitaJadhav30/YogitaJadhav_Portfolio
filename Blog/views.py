from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views import generic
from website.models import Contact, Blogs

class BlogView(generic.ListView):
    model = Blogs
    template_name = 'dashboard/blog.html'
    context_object_name= "blogs"
    
    def get_queryset(self):
        return Blogs.objects.order_by("id")
    
