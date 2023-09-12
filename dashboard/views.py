from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views import generic
from website.models import Contact , Blogs
from .forms import Addform
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render




class DashboardView(generic.ListView):
    model = Contact
    template_name = 'dashboard/contacts.html'
    context_object_name= "contacts"
    
    def get_queryset(self):
        return Contact.objects.order_by("id")
    
class BlogView(generic.ListView):
    model = Blogs
    template_name = 'dashboard/blog.html'
    context_object_name= "blogs"
    
    def get_queryset(self):
        return Blogs.objects.order_by("id")
    
def add_blog(request):
    
    if request.method == "POST":
        
        form= Addform(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            b = Blogs()
            b.title= form.cleaned_data["title"]
            b.author = form.cleaned_data["author"]
            b.updated = timezone.now()
            b.content = form.cleaned_data["content"]
            b.status = form.cleaned_data["status"]
            b.created = timezone.now()
            b.save()
            return redirect('dashboard:blog')
        
    else:
            form = Addform()
            
    return render(request, "dashboard/add_blog.html", {"form": form})

def delete_blog(request, pk):
	queryset = Blogs.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('dashboard:blog')
	return render(request, 'dashboard/delete_blog.html')
    
    
