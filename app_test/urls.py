from django.urls import path
from .views import AppViewIdx, AppViewPage01
from . import views

app_name = 'app_name_01'

urlpatterns = [
    path('ns_idx/',
         AppViewIdx.as_view(template_name='app_test/index.html'),
         name='name_idx'),
    path('ns_pg01/',
         AppViewPage01.as_view(template_name='app_test/page01.html'),
         name='name_pg01'),
    path('', views.post_list, name='post_list'),
]