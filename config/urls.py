from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:pk>/', views.edit_task, name='edit'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
    path('admin/', admin.site.urls),
]