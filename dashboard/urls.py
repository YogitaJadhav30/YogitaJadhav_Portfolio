from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

from . import views
app_name= "dashboard"
urlpatterns = [
    path("", login_required(views.DashboardView.as_view()), name="msg"),
    path("Blog/", login_required(views.BlogView.as_view()), name="blog"),
    path("add_blog/", login_required(views.add_blog), name="add_blog"),
    path("<int:pk>/delete_blog/", login_required(views.delete_blog), name="delete_blog"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout")
     
]