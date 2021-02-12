from django.urls import path
from .views import epay,success,failed

urlpatterns = [
    path('detail/<slug:slug>/',epay,name='epay'),
    path('success/',success,name='success'),
    path('failed/',failed,name='failed'),
]