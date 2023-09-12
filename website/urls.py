from django.urls import path
from .views import index,HomePageView, delete, BlogDetailView
from . import views

app_name='website'
urlpatterns = [
    path('',HomePageView.as_view(), name= "index"),
    # path('<int:pk>/Blog/',BlogDetailView.as_view(), name= "Blog"),
    path('<int:pk>/delete/', views.delete, name="delete"),
]
