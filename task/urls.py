from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='delete'),
]
