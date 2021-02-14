from django.urls import path
from .views import home_list,home_detail_view, categoricalSorting, search
urlpatterns = [
    path('',home_list,name='home'),
    path('search/',search,name='search'),
    path('<slug:slug>',home_detail_view,name='detail_view'),
    path('categories/<slug:slug>',categoricalSorting, name='categories'),
]