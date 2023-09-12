from django.urls import path

from . import views
app_name= "dashboard"
urlpatterns = [
    path("", views.DashboardView.as_view(), name="msg"),
    path("Blog/", views.BlogView.as_view(), name="blog"),
    path("add_blog/", views.add_blog, name="add_blog"),
     path("<int:pk>/delete_blog/", views.delete_blog, name="delete_blog"),
]