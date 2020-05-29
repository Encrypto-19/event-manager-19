from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('board/', views.BoardListView.as_view(), name='board-list'),
    path('board/new/', views.BoardCreateView.as_view(), name='board-create'),
    path('board/<int:pk>', views.BoardDetailView.as_view(), name='board-detail'),
    path('board/<int:pk>/update', views.BoardUpdateView.as_view(),name='board-update'),
    path('board/<int:pk>/delete', views.BoardDeleteView.as_view(),name='board-delete'),
    path('board/task/new/<int:pk>', views.TaskCreateView.as_view(), name='task-create'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update', views.TaskUpdateView.as_view(), name='task-update'),
]
