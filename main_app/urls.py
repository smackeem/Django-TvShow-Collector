from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shows/', views.shows_index, name='index'),
    path('shows/<int:show_id>', views.show_details, name='detail'),
    path('shows/create', views.ShowCreate.as_view(), name='create')
]