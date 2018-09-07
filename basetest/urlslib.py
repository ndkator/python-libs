from django.urls import path
from django.urls import re_path
from basetest import views
from basetest.views import LibraryListView, LibfilterListViewZ
from basetest.views import SearchView, SearchViewPy2, SearchViewPy3
from basetest.views import SearchTrue
from basetest.views import LibfilterListView
from basetest.views import Py2filterListView
from basetest.views import Py3filterListView

# Конструктор URL адресов, начинающихся с /libs/

urlpatterns = [
    path('', LibraryListView.as_view()),
    path('<pk>', views.liblocal), #    url('(?P<pk>\d+)', views.liblocal),
    re_path(r'^search/$', SearchView.as_view(), name='search_path'),
    re_path(r'^search/FULL/$', SearchTrue.as_view(), name='search_true'),
    re_path(r'^search/filter/py2/$', SearchViewPy2.as_view(), name='search_pathPy2'),
    re_path(r'^search/filter/py3/$', SearchViewPy3.as_view(), name='search_pathPy3'),
    path('filter/name/', LibfilterListView.as_view()),
    path('filter/libreversename/', LibfilterListViewZ.as_view()),
    path('filter/py2/', Py2filterListView.as_view()),
    path('filter/py3/', Py3filterListView.as_view()),
    ]