from django.urls import path
from . import views

app_name = 'short_link'

urlpatterns = [
    path('links/', views.LinkListView.as_view(),
         name='link_list'),
    path('links/<pk>/', views.LinkDetailView.as_view(),
         name='link_detail'),
]