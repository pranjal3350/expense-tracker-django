from django.urls import path
from . import views

urlpatterns = [
   path('', views.dashboard, name='dashboard'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('edit/<int:id>/', views.edit_transaction, name='edit_transaction'),
    path('delete/<int:id>/', views.delete_transaction, name='delete_transaction'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]