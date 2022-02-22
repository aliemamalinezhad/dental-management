from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.GetAllApiView.as_view(), name='get_all_users'),
]
