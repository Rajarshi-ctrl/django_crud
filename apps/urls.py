from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("dash", views.dash, name='dashboard'),
    path('delete/<int:id>', views.destroy, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
]
