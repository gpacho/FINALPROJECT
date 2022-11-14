from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from extra.models import Turns
from extra.forms import TurnsForm
# Create your views here.

class TurnsListView(LoginRequiredMixin, ListView):
    model = Turns
    template_name = 'turns_list.html'

class TurnsDetailView(LoginRequiredMixin, DetailView):
    model = Turns
    template_name = 'turns_detail.html'

class TurnsCreateView(LoginRequiredMixin, CreateView):
    form_class = TurnsForm
    template_name = 'turns_form.html'
    success_url = reverse_lazy('extra:turns-list')

class TurnsUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TurnsForm
    model = Turns
    template_name = 'turns_form.html'
    success_url = reverse_lazy('extra:turns-list')
    

class TurnsDeleteView(LoginRequiredMixin, DeleteView):
    model = Turns
    template_name = 'turns_confirm_delete.html'
    success_url = reverse_lazy('extra:turns-list')
