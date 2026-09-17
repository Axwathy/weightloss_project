from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-weight/', views.add_weight, name='add_weight'),
    path('view-weight/', views.view_weight, name='view_weight'),
    path('edit/<int:id>/', views.edit_weight, name='edit_weight'),
    path('delete/<int:id>/', views.delete_weight, name='delete_weight'),
]