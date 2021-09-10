from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Patient
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView) :
    template_name = 'projects/login.html'
    fields = '__all__'
    redirect_authenticated_user =True

    def get_success_url(self) :
        return reverse_lazy('patientsList')

class PatientList(LoginRequiredMixin ,ListView) :
    model = Patient
    context_object_name = 'patientsList'
    fields = '__all__'
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        search_input=self.request.GET.get('search-area') or ''
        if search_input :
            context['patientsList']=context['patientsList'].filter(patient_name__startswith=search_input)
            context['search_input'] = search_input
        return context

        
class PatientDetail(LoginRequiredMixin,DetailView) :
    model = Patient
    context_object_name = 'patientDetail'
    template_name ='projects/patient_info.html'


class PatientCreate(LoginRequiredMixin,CreateView) :
    model = Patient
    fields = '__all__'
    template_name ='projects/patient_form.html'
    success_url = reverse_lazy('patientsList')




class PatientUpdate(LoginRequiredMixin,UpdateView) :
    model = Patient
    fields = '__all__'
    template_name ='projects/patient_form.html'
    success_url = reverse_lazy('patientsList')




class PatientDelete(LoginRequiredMixin,DeleteView) :
    model = Patient
    context_object_name = 'patientDetail'
    success_url = reverse_lazy('patientsList')



