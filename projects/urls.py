from django.urls import path
from .views import PatientCreate, PatientDelete, PatientDetail, PatientList, PatientUpdate,CustomLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
   
      path('login/',CustomLoginView.as_view(),name='login'),
      path('logout/',LogoutView.as_view(next_page ='login'),name='logout'),
      path('',PatientList.as_view(),name='patientsList'),
      path('patientDetail/<str:pk>/',PatientDetail.as_view(),name='patientDetail'),
      path('new-patient/',PatientCreate.as_view(),name='new-patient'),
      path('edit-patient/<str:pk>/',PatientUpdate.as_view(),name='edit-patient'),
      path('delete-patient/<str:pk>/',PatientDelete.as_view(),name='delete-patient'),
   
]
