from django.urls import path, re_path
from basetest import views
from basetest.views import ModuleListView
from basetest.views import ModuleSearchView
from basetest.views import ModulefilterListView, ModulefilterListViewZ
from basetest.views import ModuleLibIDfilterListView, ModuleLibIDfilterListViewZ

# Конструктор URL адресов, начинающихся с /modules/

urlpatterns = [
    path('', ModuleListView.as_view()),
    path('<pk>', views.modulelocal),
    re_path(r'^search/$', ModuleSearchView.as_view(), name='Module_search_path'),
    path('filter/name/', ModulefilterListView.as_view()),
    path('filter/libsid/', ModuleLibIDfilterListView.as_view()),
    path('filter/reversename/', ModulefilterListViewZ.as_view()),
    path('filter/reverselibsid/', ModuleLibIDfilterListViewZ.as_view()),
    ]