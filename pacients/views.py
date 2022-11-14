from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from pacients.models import Pacient
from pacients.forms import PacientForm
# Create your views here.

class PacientListView(LoginRequiredMixin, ListView):
    model = Pacient
    template_name = 'pacients_list.html'

class PacientDetailView(LoginRequiredMixin, DetailView):
    model = Pacient
    template_name = 'pacients_detail.html'

class PacientCreateView(LoginRequiredMixin, CreateView):
    model = Pacient
    template_name = 'pacients_form.html'
    success_url = reverse_lazy('pacients:pacients-list')
    fields = '__all__'

class PacientUpdateView(LoginRequiredMixin, UpdateView):
    model = Pacient
    template_name = 'pacients_form.html'
    success_url = reverse_lazy('pacients:pacients-list')
    fields = '__all__'

class PacientDeleteView(LoginRequiredMixin, DeleteView):
    model = Pacient
    template_name = 'pacients_confirm_delete.html'
    success_url = reverse_lazy('pacients:pacients-list')