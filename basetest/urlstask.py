from django.urls import path, re_path
from basetest import views
from basetest.views import TaskListView, TaskSearchView
from basetest.views import TaskfilterListView, TaskfilterListViewZ


# Конструктор URL адресов, начинающихся с /tasks/

urlpatterns = [
    path('', TaskListView.as_view()),
    path('<pk>', views.tasklocal),
    re_path(r'^search/$', TaskSearchView.as_view(), name='Task_search_path'),
    path('filter/name/', TaskfilterListView.as_view()),
    path('filter/reversename/', TaskfilterListViewZ.as_view()),
    ]