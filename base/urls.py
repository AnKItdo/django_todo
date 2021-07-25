from django.urls import path
from .views import taskList, taskDetail, taskCreate, taskUpdate ,DeleteView, CustomLoginView,RegisterPage

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(),name = 'login.html'),
    path('logout/', LogoutView.as_view(next_page='login.html'),name = 'logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('',taskList.as_view(), name='task_list.html'),
    path('task/<int:pk>/',taskDetail.as_view(), name='task_detail.html'),
    path('task-create',taskCreate.as_view(), name='task_form.html'),
    path('task-update/<int:pk>/',taskUpdate.as_view(), name='task_detail.html'),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name='task_confirm_delete.html'),


]