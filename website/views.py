from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .models import Contact, Blogs
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import render

# from .forms import InputForm


def index(request):
    return render(request,'website/index.html',)

class HomePageView(CreateView):
    template_name ='website/index.html'
  
    model = Contact
    fields = '__all__'
    
    def get_success_url(self):
        return '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Yogita's Portfolio"
        context["blogs"]= Blogs.objects.filter(status=1).order_by("id")
        return context
    
def delete(request, pk):
	queryset = Contact.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('website:index')
	return render(request, 'website/delete.html')

class BlogDetailView(generic.DetailView):
    model = Blogs
    template_name= "dashboard/blog_home.html"
    context_object_name= "blog"
    
    def get_context_data(self, **kwargs):
         context= super().get_context_data(**kwargs)
         context["blogs"]= Blogs.objects.filter(status=1).order_by("id")
         return context
     



