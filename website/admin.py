from django.contrib import admin
from .models import Contact, Blogs

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created')
    list_filter = ("status",)
    search_fields = ['title', 'content']
   

admin.site.register(Contact)
admin.site.register(Blogs, BlogAdmin)


