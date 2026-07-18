from django.contrib import admin
from django.urls import path
from tasks import views
from accounts.views import register, user_login, user_logout

urlpatterns = [
    path('', views.home, name='home'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle_complete'),
    path('edit/<int:pk>/', views.edit_task, name='edit'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
]