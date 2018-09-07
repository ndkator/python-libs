from django.urls import path, re_path
from basetest import views
from basetest.views import CreatorListView, CreatorSearchView
from basetest.views import CreatorfilterListView, CreatorCountryfilterListView
from basetest.views import CreatorfilterListViewZ, CreatorCountryfilterListViewZ

# Конструктор URL адресов, начинающихся с /creators/

urlpatterns = [
    path('', CreatorListView.as_view()),
    path('<pk>', views.creatorlocal),
    re_path(r'^search/$', CreatorSearchView.as_view(), name='Creator_search_path'),
    path('filter/name/', CreatorfilterListView.as_view()),
    path('filter/country/', CreatorCountryfilterListView.as_view()),
    path('filter/reversename/', CreatorfilterListViewZ.as_view()),
    path('filter/reversecountry/', CreatorCountryfilterListViewZ.as_view()),
    ]



