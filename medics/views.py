from django.shortcuts import render
from medics.models import Medic
from medics.forms import MedicForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
# Create your views here.


class MedicListView(LoginRequiredMixin, ListView):
    model = Medic
    template_name = 'medics_list.html'

class MedicDetailView(LoginRequiredMixin, DetailView):
    model = Medic
    template_name = 'medics_detail.html'

class MedicCreateView(LoginRequiredMixin, CreateView):
    model = Medic
    template_name = 'medics_form.html'
    success_url = reverse_lazy('medics:medics-list')
    fields = '__all__'

class MedicUpdateView(LoginRequiredMixin, UpdateView):
    model = Medic
    template_name = 'medics_form.html'
    success_url = reverse_lazy('medics:medics-list')
    fields = '__all__'

class MedicDeleteView(LoginRequiredMixin, DeleteView):
    model = Medic
    template_name = 'medics_confirm_delete.html'
    success_url = reverse_lazy('medics:medics-list')
    fields = '__all__'
