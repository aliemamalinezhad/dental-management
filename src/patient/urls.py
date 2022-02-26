from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.GetAllAPIView.as_view(), name='get_all_patients'),
    path('create/', views.CreateApiView.as_view(), name='CreateApiView'),
    path('update/<int:id>/', views.UpdatePatientApiView.as_view(), name='update_patient'),

]
