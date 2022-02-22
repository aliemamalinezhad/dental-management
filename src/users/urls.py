from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.GetAllApiView.as_view(), name='get_all_users'),
    path('create/', views.CreateUserApiView.as_view(), name='create_new_user'),
    path('update/<str:username>/', views.UpdateUserApiView.as_view(), name='update_user'),
]
